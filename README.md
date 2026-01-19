# OpenCode Orchestrator System

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/bc100000000000/orchestrator-opencode?style=for-the-badge)](https://github.com/bc100000000000/orchestrator-opencode/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bc100000000000/orchestrator-opencode)](https://github.com/bc100000000000/orchestrator-opencode/network)
[![MIT License](https://img.shields.io/github/license/bc100000000000/orchestrator-opencode)](https://github.com/bc100000000000/orchestrator-opencode/blob/main/LICENSE)

**A comprehensive multi-agent orchestration system for OpenCode that coordinates specialized AI agents.**

[Features](#features) • [Quick Start](#quick-start) • [Agents](#agents) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER REQUEST                             │
│         "Build a todo app with React and Express API"           │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🤖 ORCHESTRATOR                               │
│    ┌─────────────────────────────────────────────────────────┐  │
│    │ • Analyzes request                                      │  │
│    • Creates execution plan                                   │
│    • Delegates to specialists                                 │
│    • Validates results                                        │
│    └─────────────────────────────────────────────────────────┘  │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🔧 TASK TOOL                                  │
│           (Delegates to appropriate specialist agents)          │
└─────────────────────────┬───────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ 💻 DEVELOPMENT│  │ 🧠 DATA / AI  │  │ ⚙️ OPERATIONS │
├───────────────┤  ├───────────────┤  ├───────────────┤
│ • Frontend    │  │ • AI Engineer │  │ • DevOps      │
│ • Backend     │  │ • Security    │  │ • Rapid Proto │
│ • Mobile      │  │               │  │ • Sprint      │
│               │  │               │  │ • Growth      │
│               │  │               │  │               │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ✅ VALIDATION                               │
│          • Check acceptance criteria                            │
│          • Request revisions if needed                          │
│          • Ensure quality                                       │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    📄 FINAL OUTPUT                               │
│              Complete, validated solution delivered              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent Categories

```
                        ┌─────────────────────┐
                        │   🤖 ORCHESTRATOR   │  ◄── Primary Agent
                        │   (Root Coordinator)│     Plans & Delegates
                        └──────────┬──────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ 💻 DEVELOPMENT  │   │ 🧠 DATA / AI   │   │ ⚙️ OPERATIONS   │
├─────────────────┤   ├─────────────────┤   ├─────────────────┤
│ @frontend-dev   │   │ @ai-engineer    │   │ @devops-auto    │
│ @backend-arch   │   │ @security-audit │   │ @rapid-proto    │
│ @mobile-builder │   │                 │   │ @sprint-prior   │
│                 │   │                 │   │ @growth-hacker  │
└─────────────────┘   └─────────────────┘   └─────────────────┘
          │                        │                        │
          │                        │                        │
          └────────────────────────┼────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                       📝 DOCUMENTATION                           │
│                   @content-creator (Docs & Copy)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## All 10 Specialist Agents

| # | Agent | Category | Specialty |
|---|-------|----------|-----------|
| 1 | @frontend-developer | 💻 Development | UI, React, Vue, Accessibility |
| 2 | @backend-architect | 💻 Development | APIs, Databases, System Design |
| 3 | @mobile-app-builder | 💻 Development | iOS, Android, React Native |
| 4 | @ai-engineer | 🧠 Data / AI | ML, LLMs, Prompt Engineering |
| 5 | @security-auditor | 🧠 Data / AI | Security, Vulnerability Assessment |
| 6 | @devops-automator | ⚙️ Operations | CI/CD, Infrastructure, Deployment |
| 7 | @rapid-prototyper | ⚙️ Operations | MVPs, Proof-of-Concepts |
| 8 | @sprint-prioritizer | ⚙️ Operations | Planning, Estimation, Sprints |
| 9 | @growth-hacker | ⚙️ Operations | Analytics, A/B Testing, Growth |
| 10 | @content-creator | 📝 Documentation | Documentation, Marketing Copy |

---

## Quick Agent Tree

```
ORCHESTRATOR (Primary Agent)
│
├── @frontend-developer   → UI Components, React, Vue
├── @backend-architect    → APIs, Databases, System Design
├── @mobile-app-builder   → iOS, Android, React Native
├── @ai-engineer          → ML Models, LLMs, Prompt Engineering
├── @security-auditor     → Security Auditing, Vulnerability Assessment
├── @devops-automator     → CI/CD, Infrastructure, Deployment
├── @rapid-prototyper     → Quick MVPs, Proof-of-Concepts
├── @sprint-prioritizer   → Backlog, Planning, Estimation
├── @growth-hacker        → Analytics, A/B Testing, Growth
└── @content-creator      → Documentation, Marketing Copy
```

---

## Workflow: Consult vs Delegate

### CONSULT Mode (Get Advice)
```
[CONSULT] @backend-architect: What auth strategy for REST API?
```
→ Specialist provides expert advice WITHOUT making changes

### DELEGATE Mode (Get Implementation)
```
[DELEGATE] @backend-architect: Implement JWT authentication
```
→ Specialist implements the task WITH file changes

---

## Features

<div align="center">

| 🤖 | **11 Specialized Agents** |
|:---:|:---|
| 📋 | **Consult vs Delegate** - Get advice or implementation |
| 🎯 | **User-in-the-Loop** - Approval at decision points |
| 🔐 | **Granular Permissions** - Specialists ask before editing |
| ⚡ | **Auto-Execution** - Proceeds within approved plans |
| 🛡️ | **Smart Pause Points** - Stops at critical decisions |

</div>

---

## Quick Start

```bash
# Clone and install
git clone https://github.com/bc100000000000/orchestrator-opencode.git
cd orchestrator-opencode
cp -r .opencode/agents ~/.config/opencode/

# Use in OpenCode
opencode
# Press Tab → Switch to Orchestrator
# Give a task → "Build a REST API for user auth"
```

---

## Example Usage

```
You: > Build a todo app with React frontend and Express backend

Orchestrator:
1. [CONSULT] @backend-architect on database design
2. [DELEGATE] @backend-architect to build API
3. [DELEGATE] @frontend-developer to build UI
4. [CONSULT] @security-auditor for security review
5. @content-creator adds documentation

Result: Complete todo app! ✅
```

---

## Project Structure

```
orchestrator-opencode/
├── .opencode/
│   ├── agents/
│   │   ├── orchestrator.md        # Primary agent
│   │   ├── frontend-developer.md  # Subagent
│   │   ├── backend-architect.md   # Subagent
│   │   ├── mobile-app-builder.md  # Subagent
│   │   ├── ai-engineer.md         # Subagent
│   │   ├── devops-automator.md    # Subagent
│   │   ├── rapid-prototyper.md    # Subagent
│   │   ├── sprint-prioritizer.md  # Subagent
│   │   ├── growth-hacker.md       # Subagent
│   │   ├── security-auditor.md    # Subagent
│   │   └── content-creator.md     # Subagent
│   └── plugins/
│       └── orchestrator.ts        # Validator plugin
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── package.json
```

---

## Contributing

Contributions welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md).

### Add a New Agent

1. Create `.opencode/agents/your-agent.md`
2. Define mode, permissions, and prompt
3. Submit a PR

---

## License

MIT License - see [LICENSE](LICENSE).

---

<div align="center">

### ⭐ Star this repo if you found it useful!

**Built for developers who want intelligent coordination of specialized AI agents.**

[GitHub](https://github.com/bc100000000000/orchestrator-opencode) • [Report Issue](https://github.com/bc100000000000/orchestrator-opencode/issues)

</div>
