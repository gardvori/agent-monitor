# 🤖 AI Agent Monitor

> **Observability dashboard for AI agents** — monitor activity, costs, performance, and alerts in real-time.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://yourusername.github.io/agent-monitor/)

## ✨ Features

- **📊 Dashboard Overview** — Total agents, active/idle status, total cost, and average response time at a glance
- **🤖 Agent List** — Detailed table with agent name, status (active/idle/error), last activity, total calls, and cost
- **📈 Cost Analytics** — Interactive Chart.js charts with daily/weekly/monthly spending per agent
- **📋 Activity Log** — Real-time scrolling log of all agent activities with color-coded severity
- **🔔 Alert Panel** — Automatic warnings when cost exceeds budget thresholds or agents enter error state
- **⚙ Settings** — Configurable budget limits, alert thresholds, refresh intervals, and sound alerts
- **⬇ Export** — Download all data as JSON for external analysis
- **🌙 Dark Theme** — Beautiful dark UI, fully responsive across all devices

## 🖼 Screenshots

![Dashboard Overview](https://placehold.co/1200x600/0d1117/58a6ff?text=Dashboard+Overview)
![Agent List & Activity Log](https://placehold.co/1200x600/0d1117/3fb950?text=Agent+List+%26+Activity+Log)
![Cost Chart & Alerts](https://placehold.co/1200x600/0d1117/bc8cff?text=Cost+Chart+%26+Alerts)

## 🚀 Quick Start

### View Online
Visit the live dashboard: **[yourusername.github.io/agent-monitor](https://yourusername.github.io/agent-monitor/)**

### Run Locally
```bash
# Clone the repo
git clone https://github.com/yourusername/agent-monitor.git
cd agent-monitor

# Open in browser (any static server works)
python3 -m http.server 8080
# Then open http://localhost:8080
```

Or simply open `index.html` directly in your browser.

## 🛠 Tech Stack

- **Pure HTML/CSS/JS** — Single file, zero build step
- **Chart.js 4.4** — Beautiful interactive charts via CDN
- **GitHub Pages** — Free hosting
- **No dependencies** — Works offline after first load

## 📡 API Integration

The dashboard uses simulated data by default. To connect real agent data:

1. Replace the `AGENTS` array in `index.html` with your actual agent data
2. Implement a backend endpoint that returns agent metrics
3. Update the `simulateTick()` function to fetch from your API

Example agent data structure:
```json
{
  "id": 1,
  "name": "My-Agent",
  "model": "GPT-4o",
  "status": "active",
  "calls": 12847,
  "cost": 142.38,
 "lastActivity": 1715599200000
}
```

## 💡 Why AI Agent Monitor?

AI agents are becoming critical infrastructure, but observability tools for them are scarce. This dashboard fills that gap:

- **Cost control** — Track spending per agent, set budgets, get alerts
- **Performance monitoring** — Response times, call volumes, error rates
- **Real-time visibility** — Live activity feed and status indicators
- **Open source** — Free to use, modify, and extend

## 🤝 Contributing

Contributions are welcome! Areas we'd love help with:

- [ ] Backend API integration examples
- [ ] Additional chart types (token usage, latency distribution)
- [ ] Agent detail drill-down pages
- [ ] Slack/Discord webhook alerts
- [ ] Multi-user support with authentication

## 📄 License

[MIT](LICENSE) — use it however you want.

## 💖 Support This Project

If this tool helps you, consider supporting via GitHub Sponsors:

[<img src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-ff69b4?logo=github">](https://github.com/sponsors/yourusername)

---

Built with ❤️ by the open-source AI community.
