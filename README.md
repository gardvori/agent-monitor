# 🖥️ agent-monitor

Observability dashboard for AI agents. Track activity, costs, performance, and alerts in real-time.

## Features

- **Real-Time Dashboard** — Web-based dashboard with auto-refresh (30s)
- **System Metrics** — CPU, memory, disk, uptime
- **PM2 Agent Monitoring** — Status, memory, CPU, restart count per agent
- **Cron Job Monitoring** — Status, last run, next run for all cron jobs
- **Error Log Viewer** — Recent errors from PM2 logs
- **JSON API** — `/api/metrics` endpoint for programmatic access
- **Zero Dependencies** — Pure Python stdlib

## Installation

```bash
git clone https://github.com/gardvori/agent-monitor.git
cd agent-monitor
```

## Usage

```bash
# Start dashboard server
python3 agent_monitor.py start

# Start on custom port
python3 agent_monitor.py start --port 8080

# Take a snapshot
python3 agent_monitor.py snapshot

# JSON output
python3 agent_monitor.py snapshot --json
```

## Dashboard

Open `http://<server-ip>:9191` in your browser.

![Dashboard](https://via.placeholder.com/800x400/0d1117/58a6ff?text=Agent+Monitor+Dashboard)

## API

```
GET /api/metrics
```

Returns JSON with system, agents, and cron metrics.

## License

MIT
