# ⚡ AI Agent Monitor

> **Observability dashboard for AI agent activity** — track costs, response times, agent status, and alerts in real time.

![Dark Theme](https://img.shields.io/badge/theme-dark-1a1a2e?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Dashboard** | Total agents, active/idle count, total cost, avg response time |
| 🤖 **Agent List** | Name, status, last activity, call count, cost per agent |
| 📈 **Cost Chart** | Interactive doughnut chart (Chart.js) showing cost breakdown |
| ⏱ **Response Time Chart** | Line chart tracking avg response time over days |
| 📋 **Activity Log** | Real-time streaming log of agent actions |
| 🔔 **Alert Panel** | Budget warnings, error state alerts, high-cost notifications |
| 💰 **Budget Settings** | Configurable monthly budget limit with visual progress bar |
| 🌙 **Dark Theme** | GitHub-dark inspired color scheme |
| 📱 **Responsive** | Works on desktop, tablet, and mobile |

## 🚀 Quick Start

### Option 1: Open directly

Simply open `index.html` in your browser. No build step, no server required.

```bash
open index.html
```

### Option 2: GitHub Pages

Visit the live demo: `https://<username>.github.io/agent-monitor/`

### Option 3: Local server

```bash
cd agent-monitor
python3 -m http.server 8080
# Open http://localhost:8080
```

## 🛠 Tech Stack

- **HTML5** — Single file, zero dependencies (except CDN)
- **Chart.js 4.4** — Charts via CDN
- **CSS3** — Custom properties, grid, flexbox, animations
- **Vanilla JS** — No frameworks, no build tools

## 📁 Project Structure

```
agent-monitor/
├── index.html          # Complete dashboard (single file)
├── README.md           # This file
├── LICENSE             # MIT License
└── .github/
    └── FUNDING.yml     # GitHub Sponsors config
```

## 🎛 Configuration

Budget and alert settings are configurable directly in the UI:

- **Monthly Budget Limit** — Set your spending cap
- **Alert Threshold** — Get warned at X% of budget

## 🤝 Contributing

Contributions welcome! Areas of interest:

- [ ] WebSocket integration for real agent data
- [ ] Export logs to CSV/JSON
- [ ] Multi-workspace support
- [ ] Agent detail drill-down pages
- [ ] Slack/Discord webhook alerts

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Built to fill the AI Agent Observability gap. Inspired by the wave of AI Agent tools dominating GitHub trending.

---

*Built with ❤ for the AI engineering community.*
