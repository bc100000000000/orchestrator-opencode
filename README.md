# OpenCode Orchestrator System

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/bc100000000000/orchestrator-opencode?style=for-the-badge)](https://github.com/bc100000000000/orchestrator-opencode/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bc100000000000/orchestrator-opencode)](https://github.com/bc100000000000/orchestrator-opencode/network)
[![MIT License](https://img.shields.io/github/license/bc100000000000/orchestrator-opencode)](https://github.com/bc100000000000/orchestrator-opencode/blob/main/LICENSE)

**Multi-agent orchestration system with anti-hallucination safeguards and 90+ reusable skills.**

[Features](#features) • [Agents](#agents) • [Skills](#skills) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## How It Works

```
USER REQUEST → ORCHESTRATOR → TASK TOOL → SPECIALISTS → VALIDATION → OUTPUT
```

**Orchestrator:**
- Analyzes request, creates execution plan
- Delegates to appropriate agents
- Enforces anti-hallucination rules
- Validates results before delivery

---

## Anti-Hallucination Standard

All agents follow strict rules for deterministic, accurate outputs.

### Priority Order

| Priority | Principle |
|----------|-----------|
| 1st | **Accuracy** - Never fabricate information |
| 2nd | **Determinism** - Reproducible behavior |
| 3rd | **Completeness** - Full task coverage |
| 4th | **Speed** - Efficient execution |

### Rules

```
✓ DO: Use user instructions, reference docs, verify outputs, ask when blocked
✗ DON'T: Invent APIs, guess missing info, assume defaults, fabricate data
```

### Execution Mode (4 Phases)

1. **ANALYSIS** - Restate task, list knowns/unknowns, identify blockers
2. **ASSUMPTIONS CHECK** - Explicitly list assumptions, STOP if unclear
3. **BUILD** - Execute with confirmed inputs only
4. **SELF-VERIFICATION** - Confirm no inventions or assumptions

### Blocked Response

```
"BLOCKED: Missing <exact information needed>"
```

### Structured Output

```json
{"inputs": [], "knowns": [], "unknowns": [], "dependencies": [], "implementation": [], "verification": []}
```

---

## Features

| Feature | Description |
|---------|-------------|
| 14 Specialized Agents | Domain-specific specialists |
| Anti-Hallucination | Deterministic, accurate outputs |
| 90+ Skills | Reusable patterns from skills.sh |
| Consult Mode | Get expert advice (no changes) |
| Delegate Mode | Get implementation (with changes) |
| Granular Permissions | Agents ask before editing |

---

## Agents

**14 Specialist Agents** with 90+ skills from skills.sh ecosystem.

```
ORCHESTRATOR (Primary Agent)
|
+-- @frontend-developer   -> UI, React, Vue (15 skills)
+-- @backend-architect    -> APIs, Databases (12 skills)
+-- @mobile-app-builder   -> iOS, Android, React Native (6 skills)
+-- @ai-engineer          -> ML, LLMs, Prompt Engineering (7 skills)
+-- @security-auditor     -> Security, Vulnerability Assessment (8 skills)
+-- @ordinals-runes       -> Bitcoin Ordinals, Runes Protocol *
+-- @devops-automator     -> CI/CD, Deployment (6 skills)
+-- @rapid-prototyper     -> Quick MVPs, Proof-of-Concepts (12 skills)
+-- @sprint-prioritizer   -> Planning, Estimation (12 skills)
+-- @growth-hacker        -> Analytics, A/B Testing, Growth (13 skills)
+-- @x-growth-operator    -> X/Twitter Growth (6 skills)
+-- @x-trend-observer     -> X/Twitter Trends (3 skills)
+-- @content-creator      -> Documentation, Copywriting (7 skills)

* Specialized domain - no general-purpose skills
```

### Consult vs Delegate

```bash
[CONSULT] @backend-architect: Best auth strategy for REST API?
[DELEGATE] @backend-architect: Implement JWT authentication
```

---

## Skills

**90+ reusable skills** installed at `.opencode/skills/individual/`

### Skills by Agent

| Agent | Skills |
|-------|--------|
| @frontend-developer | React Best Practices, Vue, Nuxt, Tailwind, Web Design |
| @backend-architect | API Routes, Convex, Better Auth, NestJS, Cloudflare |
| @ai-engineer | MCP Builder, PDF, DOCX, XLSX, PPTX |
| @security-auditor | Variant Analysis, Sharp Edges, Security Patterns |
| @devops-automator | CI/CD Workflows, Deployment |
| @content-creator | Copywriting, Copy Editing, Documentation |
| @growth-hacker | Analytics, A/B Testing, CRO, SEO, Email, Pricing |
| @mobile-app-builder | React Native, SwiftUI |
| @rapid-prototyper | React, Nuxt, Vue, Convex, Tailwind |
| @sprint-prioritizer | TDD, Code Review, Planning, Git Worktrees |
| @x-growth-operator | Post to X, Cover Image, Slide Deck |
| @x-trend-observer | Analytics Tracking, Social Content |

### Install More Skills

```bash
cd .opencode/skills
npx skills add <owner/repo>
```

---

## Quick Start

```bash
git clone https://github.com/bc100000000000/orchestrator-opencode.git
cd orchestrator-opencode
cp -r .opencode/agents ~/.config/opencode/
cp -r .opencode/skills ~/.config/opencode/
opencode  # Press Tab -> Switch to Orchestrator
```

---

## Example

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
|   +-- agents/              # 14 agent definitions
|   +-- skills/              # 90+ skills (101MB)
|   +-- plugins/
+-- README.md
+-- LICENSE
+-- CONTRIBUTING.md
```

---

## Contributing

1. Create `.opencode/agents/your-agent.md`
2. Include anti-hallucination standard section
3. Add relevant skills
4. Submit a PR

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

<div align="center">

### ⭐ Star this repo!

[GitHub](https://github.com/bc100000000000/orchestrator-opencode) • [Issues](https://github.com/bc100000000000/orchestrator-opencode/issues)

</div>
