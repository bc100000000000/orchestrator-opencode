# OpenCode Orchestrator System

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/bc100000000000/orchestrator-opencode?style=for-the-badge)](https://github.com/bc100000000000/orchestrator-opencode/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bc100000000000/orchestrator-opencode)](https://github.com/bc100000000000/orchestrator-opencode/network)
[![MIT License](https://img.shields.io/github/license/bc100000000000/orchestrator-opencode)](https://github.com/bc100000000000/orchestrator-opencode/blob/main/LICENSE)

**A comprehensive multi-agent orchestration system for OpenCode that coordinates specialized AI agents with deterministic anti-hallucination safeguards.**

[Features](#features) • [Anti-Hallucination Standard](#anti-hallucination-standard) • [Agents](#agents) • [Skills](#skills) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## How It Works

```
+======================================================================+
|                          USER REQUEST                                |
|            "Build a todo app with React and Express API"             |
+--------------------------+-------------------------------------------+
                            |
                            v
+======================================================================+
|                        ORCHESTRATOR                                   |
|  +--------------------------------------------------------------------+
|  |  • Analyzes request                                                |
|  |  • Creates execution plan                                          |
|  |  • Delegates to specialists                                        |
|  |  • Validates results                                               |
|  |  • Enforces anti-hallucination rules                               |
|  +--------------------------------------------------------------------+
+--------------------------+-------------------------------------------+
                            |
                            v
+======================================================================+
|                         TASK TOOL                                     |
|              (Delegates to appropriate specialist agents)             |
+--------------------------+-------------------------------------------+
                            |
          +------------------+-------------------+
          |                  |                   |
          v                  v                   v
+-----------+         +-----------+         +-----------+
|DEVELOPMENT|         |  DATA/AI  |         | OPERATIONS|
+-----------+         +-----------+         +-----------+
| Frontend  |         |AI Engineer|         | DevOps    |
| Backend   |         |Security   |         | Rapid     |
| Mobile    |         | Auditor   |         | Sprint    |
|           |         |Ordinals   |         | Growth    |
+-----------+         +-----------+         +-----------+
          |                  |                   |
          +------------------+-------------------+
                            |
                            v
+======================================================================+
|                         VALIDATION                                   |
|       • Check acceptance criteria                                    |
|       • Request revisions if needed                                  |
|       • Ensure quality                                               |
|       • Verify no hallucinations                                     |
+--------------------------+-------------------------------------------+
                            |
                            v
+======================================================================+
|                        FINAL OUTPUT                                  |
|             Complete, validated solution delivered                   |
+======================================================================+
```

---

## Anti-Hallucination Standard

All agents operate under a strict **Anti-Hallucination Contract** that ensures deterministic, accurate outputs.

### Core Principles

| Priority | Principle | Description |
|----------|-----------|-------------|
| 1st | **Accuracy** | Never fabricate information |
| 2nd | **Determinism** | Reproducible, predictable behavior |
| 3rd | **Completeness** | Full task coverage |
| 4th | **Speed** | Efficient execution |

### Global Rules

```
✓ DO:
  - Use user-provided instructions only
  - Reference explicit documentation
  - Use verified outputs from other agents
  - Request clarification when blocked

✗ DON'T:
  - Invent APIs, libraries, or endpoints
  - Guess missing information
  - Assume environments or defaults
  - Fabricate data or metrics
```

### Execution Mode

Every agent operates in **4 phases**:

1. **ANALYSIS** - Restate task, list knowns/unknowns, identify blockers
2. **ASSUMPTIONS CHECK** - Explicitly list assumptions, STOP if unclear
3. **BUILD** - Execute with confirmed inputs only
4. **SELF-VERIFICATION** - Confirm no inventions or assumptions

### Blocked Responses

When information is missing, agents respond with:

```
"BLOCKED: Missing <exact information needed>"
```

### Structured Outputs

All agents return structured JSON:

```json
{
  "inputs": [],
  "knowns": [],
  "unknowns": [],
  "dependencies": [],
  "implementation": [],
  "verification": []
}
```

---

## Skills Integration (skills.sh)

Agents have access to **90+ reusable skills** from the [skills.sh](https://skills.sh) ecosystem.

### Skills Directory

```
.opencode/skills/
+-- individual/           # 90 installed skills
|   +-- react-best-practices/
|   +-- convex-best-practices/
|   +-- analytics-tracking/
|   +-- copywriting/
|   +-- mcp-builder/
|   +-- ...
+-- INDEX.md              # Skills catalog
```

### Skills by Agent

| Agent | Skills Available |
|-------|-----------------|
| @frontend-developer | React, Vue, Nuxt, Tailwind, Web Design (15) |
| @backend-architect | API Routes, Convex, Auth, NestJS (12) |
| @ai-engineer | MCP Builder, PDF/DOCX/XLSX (7) |
| @security-auditor | Variant Analysis, Security Patterns (8) |
| @devops-automator | CI/CD, Deployment, Cloudflare (6) |
| @content-creator | Copywriting, Docs, Brand Guidelines (7) |
| @growth-hacker | Analytics, A/B Testing, CRO, SEO (13) |
| @mobile-app-builder | React Native, SwiftUI (6) |
| @rapid-prototyper | Fast MVP Patterns (12) |
| @sprint-prioritizer | Planning, TDD, Code Review (12) |
| @x-growth-operator | Post to X, Content Patterns (6) |
| @x-trend-observer | Analytics, Social Content (3) |

### Installing More Skills

```bash
cd .opencode/skills
npx skills add <owner/repo>
```

---

## Agent Categories

```
                               +---------------------+
                               |    ORCHESTRATOR     |  <-- Primary Agent
                               |  (Root Coordinator) |
                               |  Anti-Hallucination |
                               +----------+----------+
                                          |
                      +--------------------+--------------------+
                      |                    |                    |
                      v                    v                    v
              +-----------------+  +-----------------+  +-----------------+
              |   DEVELOPMENT   |  |    DATA / AI    |  |   OPERATIONS    |
              +-----------------+  +-----------------+  +-----------------+
              | @frontend-dev   |  | @ai-engineer    |  | @devops-auto    |
              | @backend-arch   |  | @security-audit |  | @rapid-proto    |
              | @mobile-builder |  | @ordinals-runes |  | @sprint-prior   |
              |                 |  |                 |  | @growth-hacker  |
              |                 |  |                 |  | @x-growth-op    |
              |                 |  |                 |  | @x-trend-obs    |
              +-----------------+  +-----------------+  +-----------------+
                      |                    |                    |
                      |                    |                    |
                      +--------------------+--------------------+
                                           |
                                           v
                                +---------------------+
                                |   DOCUMENTATION     |
                                | @content-creator    |
                                +---------------------+
```

---

## All 14 Specialist Agents

| # | Agent | Category | Specialty | Skills |
|---|-------|----------|-----------|--------|
| 1 | @frontend-developer | DEVELOPMENT | UI, React, Vue, Accessibility | 15 |
| 2 | @backend-architect | DEVELOPMENT | APIs, Databases, System Design | 12 |
| 3 | @mobile-app-builder | DEVELOPMENT | iOS, Android, React Native | 6 |
| 4 | @ai-engineer | DATA / AI | ML, LLMs, Prompt Engineering | 7 |
| 5 | @security-auditor | DATA / AI | Security, Vulnerability Assessment | 8 |
| 6 | @ordinals-runes | DATA / AI | Bitcoin Ordinals, Runes Protocol | 0* |
| 7 | @devops-automator | OPERATIONS | CI/CD, Infrastructure, Deployment | 6 |
| 8 | @rapid-prototyper | OPERATIONS | Quick MVPs, Proof-of-Concepts | 12 |
| 9 | @sprint-prioritizer | OPERATIONS | Planning, Estimation, Sprints | 12 |
| 10 | @growth-hacker | OPERATIONS | Analytics, A/B Testing, Growth | 13 |
| 11 | @x-growth-operator | OPERATIONS | X/Twitter Distribution, Growth | 6 |
| 12 | @x-trend-observer | OPERATIONS | X/Twitter Trend Monitoring | 3 |
| 13 | @content-creator | DOCUMENTATION | Documentation, Marketing Copy | 7 |
| 14 | @security-auditor | DATA / AI | NEW: Security auditing | 8 |

*Ordinals/Runes is a specialized Bitcoin protocol domain with no general-purpose skills.

---

## Quick Agent Tree

```
ORCHESTRATOR (Primary Agent)
|
+-- @frontend-developer   -> UI Components, React, Vue, Accessibility (15 skills)
+-- @backend-architect    -> APIs, Databases, System Design (12 skills)
+-- @mobile-app-builder   -> iOS, Android, React Native (6 skills)
+-- @ai-engineer          -> ML Models, LLMs, Prompt Engineering (7 skills)
+-- @security-auditor     -> Security Auditing, Vulnerability Assessment (8 skills)
+-- @ordinals-runes       -> Bitcoin Ordinals, Inscriptions, Runes Protocol
+-- @devops-automator     -> CI/CD, Infrastructure, Deployment (6 skills)
+-- @rapid-prototyper     -> Quick MVPs, Proof-of-Concepts (12 skills)
+-- @sprint-prioritizer   -> Backlog, Planning, Estimation (12 skills)
+-- @growth-hacker        -> Analytics, A/B Testing, Growth (13 skills)
+-- @x-growth-operator    -> X/Twitter Distribution, Growth (6 skills)
+-- @x-trend-observer     -> X/Twitter Trend Monitoring, Intelligence (3 skills)
+-- @content-creator      -> Documentation, Marketing Copy (7 skills)
```

---

## Workflow: Consult vs Delegate

### CONSULT Mode (Get Advice)
```
[CONSULT] @backend-architect: What auth strategy for REST API?
```
Specialist provides expert advice WITHOUT making changes.

### DELEGATE Mode (Get Implementation)
```
[DELEGATE] @backend-architect: Implement JWT authentication
```
Specialist implements the task WITH file changes.

---

## Features

<div align="center">

| 🤖 | **14 Specialized Agents** |
|:---:|:---|
| 🛡️ | **Anti-Hallucination Standard** - Deterministic, accurate outputs |
| 📦 | **90+ Skills** - Reusable patterns from skills.sh |
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
cp -r .opencode/skills ~/.config/opencode/

# Use in OpenCode
opencode
# Press Tab -> Switch to Orchestrator
# Give a task -> "Build a REST API for user auth"
```

---

## Example Usage

```
You: > Build a todo app with React frontend and Express backend

Orchestrator:
1. [CONSULT] @backend-architect on database design
2. [DELEGATE] @backend-architect to build API
3. [CONSULT] @security-auditor for security review
4. [DELEGATE] @frontend-developer to build UI
5. [DELEGATE] @content-creator adds documentation

Result: Complete todo app! ✅
```

---

## Project Structure

```
orchestrator-opencode/
+-- .opencode/
|   +-- agents/
|   |   +-- orchestrator.md         # Primary agent
|   |   +-- frontend-developer.md   # Subagent (15 skills)
|   |   +-- backend-architect.md    # Subagent (12 skills)
|   |   +-- mobile-app-builder.md   # Subagent (6 skills)
|   |   +-- ai-engineer.md          # Subagent (7 skills)
|   |   +-- security-auditor.md     # Subagent (8 skills)
|   |   +-- ordinals-runes.md       # Subagent (specialized)
|   |   +-- devops-automator.md     # Subagent (6 skills)
|   |   +-- rapid-prototyper.md     # Subagent (12 skills)
|   |   +-- sprint-prioritizer.md   # Subagent (12 skills)
|   |   +-- growth-hacker.md        # Subagent (13 skills)
|   |   +-- x-growth-operator.md    # Subagent (6 skills)
|   |   +-- x-trend-observer.md     # Subagent (3 skills)
|   |   +-- content-creator.md      # Subagent (7 skills)
|   +-- skills/                     # Skills directory (101MB, 90 skills)
|   |   +-- individual/             # Installed skills
|   |   +-- INDEX.md                # Skills catalog
|   +-- plugins/
|       +-- orchestrator.ts         # Validator plugin
+-- README.md
+-- LICENSE
+-- CONTRIBUTING.md
+-- package.json
```

---

## Contributing

Contributions welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md).

### Add a New Agent

1. Create `.opencode/agents/your-agent.md`
2. Include anti-hallucination standard section
3. Add relevant skills from skills.sh
4. Define mode, permissions, and prompt
5. Submit a PR

### Update Skills

```bash
cd .opencode/skills
npx skills add <owner/repo>
```

---

## License

MIT License - see [LICENSE](LICENSE).

---

<div align="center">

### ⭐ Star this repo if you found it useful!

**Built for developers who want intelligent coordination of specialized AI agents with deterministic anti-hallucination safeguards.**

[GitHub](https://github.com/bc100000000000/orchestrator-opencode) • [Report Issue](https://github.com/bc100000000000/orchestrator-opencode/issues)

</div>
