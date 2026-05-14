#!/usr/bin/env python3
"""
agent-monitor — Observability dashboard for AI agents
Track activity, costs, performance, and alerts in real-time.
"""

import subprocess
import json
import time
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── Configuration ──────────────────────────────────────────────────────────

DASHBOARD_PORT = 9191
DASHBOARD_HTML_PATH = Path(__file__).parent / "dashboard.html"

# ── Data Collection ───────────────────────────────────────────────────────

def collect_system_metrics() -> dict:
    """Collect system-level metrics."""
    metrics = {"timestamp": datetime.now().isoformat()}
    try:
        with open("/proc/loadavg") as f:
            load = f.read().split()
            metrics["cpu_load_1m"] = float(load[0])
            metrics["cpu_load_5m"] = float(load[1])
            metrics["cpu_load_15m"] = float(load[2])
    except Exception:
        metrics["cpu_load_1m"] = 0
    try:
        result = subprocess.run(["free", "-m"], capture_output=True, text=True, timeout=5)
        lines = result.stdout.strip().split("\n")
        mem_line = lines[1].split()
        metrics["memory_total_mb"] = int(mem_line[1])
        metrics["memory_used_mb"] = int(mem_line[2])
        metrics["memory_usage_pct"] = round(int(mem_line[2]) / int(mem_line[1]) * 100, 1) if int(mem_line[1]) > 0 else 0
    except Exception:
        metrics["memory_usage_pct"] = 0
    try:
        result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, timeout=5)
        lines = result.stdout.strip().split("\n")
        disk_line = lines[1].split()
        metrics["disk_total"] = disk_line[1]
        metrics["disk_used"] = disk_line[2]
        metrics["disk_usage_pct"] = int(disk_line[3].replace("%", ""))
    except Exception:
        metrics["disk_usage_pct"] = 0
    try:
        with open("/proc/uptime") as f:
            uptime_seconds = float(f.read().split()[0])
            metrics["uptime_hours"] = round(uptime_seconds / 3600, 1)
    except Exception:
        metrics["uptime_hours"] = 0
    return metrics

def collect_pm2_metrics() -> list:
    """Collect PM2 process metrics."""
    agents = []
    try:
        result = subprocess.run(["pm2", "jlist"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            processes = json.loads(result.stdout)
            for proc in processes:
                pm2_env = proc.get("pm2_env", {})
                monit = proc.get("monit", {})
                agents.append({
                    "name": proc.get("name", "unknown"),
                    "status": pm2_env.get("status", "unknown"),
                    "pid": proc.get("pid", 0),
                    "uptime_ms": pm2_env.get("pm_uptime", 0),
                    "restarts": pm2_env.get("restart_time", 0),
                    "memory_mb": round(monit.get("memory", 0) / 1024 / 1024, 1),
                    "cpu_pct": monit.get("cpu", 0)
                })
    except Exception:
        pass
    return agents

def collect_cron_metrics() -> list:
    """Collect cron job metrics."""
    jobs = []
    try:
        result = subprocess.run(
            ["python3", "-c",
             "import json,sys; sys.path.insert(0,'/root/.hermes'); "
             "from cron.jobs import load_jobs; jobs=load_jobs(); "
             "[print(json.dumps({'name':j.get('name','?'),'enabled':j.get('enabled',False),"
             "'last_status':j.get('last_status','?'),'last_run':str(j.get('last_run_at','never'))[:16],"
             "'next_run':str(j.get('next_run_at','?'))[:16],'schedule':j.get('schedule_display','?')})) "
             "for j in jobs]"],
            capture_output=True, text=True, timeout=10
        )
        for line in result.stdout.strip().split("\n"):
            if line.strip():
                jobs.append(json.loads(line))
    except Exception:
        pass
    return jobs

def collect_log_errors(pm2_name: str, lines: int = 50) -> list:
    """Collect recent errors from PM2 logs."""
    errors = []
    log_path = f"/root/.pm2/logs/{pm2_name}-error-0.log"
    try:
        if os.path.exists(log_path):
            result = subprocess.run(["tail", f"-{lines}", log_path], capture_output=True, text=True, timeout=5)
            for line in result.stdout.strip().split("\n"):
                if "error" in line.lower() or "Error" in line or "429" in line:
                    errors.append(line[:200])
    except Exception:
        pass
    return errors[-10:]

# ── HTTP Server ───────────────────────────────────────────────────────────

class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            html = DASHBOARD_HTML_PATH.read_text() if DASHBOARD_HTML_PATH.exists() else "<h1>Dashboard HTML not found</h1>"
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode())
        elif self.path == "/api/metrics":
            data = {
                "system": collect_system_metrics(),
                "agents": collect_pm2_metrics(),
                "cron": collect_cron_metrics()
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data, default=str).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass

def start_dashboard(port: int = DASHBOARD_PORT):
    """Start the dashboard HTTP server."""
    server = HTTPServer(("0.0.0.0", port), DashboardHandler)
    print(f"Agent Monitor dashboard running at http://0.0.0.0:{port}")
    server.serve_forever()

# ── CLI ────────────────────────────────────────────────────────────────────

def cmd_start(args):
    port = args.port or DASHBOARD_PORT
    print(f"Starting Agent Monitor dashboard on port {port}...")
    start_dashboard(port)

def cmd_snapshot(args):
    data = {
        "system": collect_system_metrics(),
        "agents": collect_pm2_metrics(),
        "cron": collect_cron_metrics()
    }
    if args.json:
        print(json.dumps(data, indent=2, default=str))
    else:
        print(f"\nAgent Monitor Snapshot - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        sm = data["system"]
        print(f"System:")
        print(f"  CPU Load:    {sm.get('cpu_load_1m', '?')}")
        print(f"  Memory:      {sm.get('memory_used_mb', '?')} / {sm.get('memory_total_mb', '?')} MB ({sm.get('memory_usage_pct', '?')}%)")
        print(f"  Disk:        {sm.get('disk_used', '?')} / {sm.get('disk_total', '?')} ({sm.get('disk_usage_pct', '?')}%)")
        print(f"  Uptime:      {sm.get('uptime_hours', '?')}h")
        print(f"\nAgents (PM2):")
        for agent in data["agents"]:
            status = "OK" if agent["status"] == "online" else "DOWN"
            print(f"  [{status}] {agent['name']}: {agent['memory_mb']}MB | CPU {agent['cpu_pct']}% | Restarts: {agent['restarts']}")
        print(f"\nCron Jobs:")
        for job in data["cron"]:
            status = "OK" if job.get("last_status") == "ok" else "ERR" if job.get("last_status") == "error" else "?"
            en = "on" if job.get("enabled") else "off"
            print(f"  [{status}] [{en}] {job['name']}: {job.get('schedule','?')}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="agent-monitor - Observability dashboard for AI agents")
    subparsers = parser.add_subparsers(dest="command")
    
    start_parser = subparsers.add_parser("start", help="Start dashboard server")
    start_parser.add_argument("--port", type=int, default=DASHBOARD_PORT)
    
    snapshot_parser = subparsers.add_parser("snapshot", help="Take metrics snapshot")
    snapshot_parser.add_argument("--json", action="store_true")
    
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "start":
        cmd_start(args)
    elif args.command == "snapshot":
        cmd_snapshot(args)

if __name__ == "__main__":
    main()
