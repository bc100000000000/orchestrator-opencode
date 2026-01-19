# OpenCode Orchestrator System

A comprehensive multi-agent orchestration system for [OpenCode](https://opencode.ai) that coordinates specialized AI agents for complex software development tasks.

## Architecture Diagram

```
                                    ┌─────────────────────────┐
                                    │       USER INPUT        │
                                    │   (Complex Request)     │
                                    └───────────┬─────────────┘
                                                │
                                                ▼
                                    ┌─────────────────────────┐
                                    │      ORCHESTRATOR       │
                                    │  ┌───────────────────┐  │
                                    │  │ • Plans & Analyzes│  │
                                    │  │ • Delegates Tasks │  │
                                    │  │ • Validates Output│  │
                                    │  │ • Aggregates      │  │
                                    │  └───────────────────┘  │
                                    └───────────┬─────────────┘
                                                │
                                ┌───────────────┼───────────────┐
                                │               │               │
                                ▼               ▼               ▼
                    ┌─────────────────┬─────────┴─────────┬─────────────────┐
                    │                                                     │
                    ▼              TASK TOOL DELEGATION (1-to-many)         ▼
                    │                                                     │
           ┌────────┴────────┐                            ┌─────────────────┴─────────────────┐
           │                 │                            │                                   │
           ▼                 ▼                            ▼                                   ▼
        ┌──────┐        ┌──────┐                   ┌─────────────┐                   ┌─────────────┐
        │ CONSULT │      │CONSULT│                   │  CONSULT    │                   │  CONSULT    │
        │ Agent A │      │ Agent B│                   │   Agent C   │                   │   Agent D   │
        └─────────┘      └────────┘                   └─────────────┘                   └─────────────┘
       (Advice Only)   (Advice Only)                        │                                   │
                                                             │                                   │
                                                             ▼                                   ▼
                                                      ┌─────────────┐                   ┌─────────────┐
                                                      │  DELEGATE   │                   │  DELEGATE   │
                                                      │   Agent E   │                   │   Agent F   │
                                                      └─────────────┘                   └─────────────┘
                                                     (Implements)                       (Implements)
                                                             │                                   │
                                                             └─────────────┬─────────────────────┘
                                                                           │
                                                                           ▼
                                                        ┌────────────────────────────────────┐
                                                        │      ORCHESTRATOR VALIDATES        │
                                                        │   • Checks acceptance criteria     │
                                                        │   • Requests revisions if needed   │
                                                        └────────────────────────────────────┘
                                                                           │
                                                                           ▼
                                                        ┌────────────────────────────────────┐
                                                        │      FINAL DELIVERABLE(S)          │
                                                        │      Aggregated Output to User     │
                                                        └────────────────────────────────────┘
```

### Agent Tree (Merkle-Style)

```
                                    ┌─────────────────────────────┐
                                    │        ORCHESTRATOR          │ ◄── Primary Agent
                                    │       (Root Coordinator)     │     Plans & Delegates
                                    └─────────────────────────────┘
                                                 │
         ┌────┬────┬────┬────┬────┬────┬─────┬─────┬────┬────┐
         │    │    │    │    │    │    │     │     │    │    │
         ▼    ▼    ▼    ▼    ▼    ▼    ▼     ▼     ▼    ▼    ▼
   ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
   │FRONTEND││ BACKEND││ MOBILE ││   AI   ││ DEVOPS ││  RAPID ││SECURITY││ SPRINT ││  GROWTH││ CONTENT│
   │ DEVELOP││ARCHITEC││ BUILDER││ENGINEER││AUTOMAT.││PROTOTYP││ AUDITOR││PRIORIT.││  HACKER││ CREATOR│
   └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
       │        │        │        │        │        │        │        │        │        │
       ▼        ▼        ▼        ▼        ▼        ▼        ▼        ▼        ▼        ▼
   ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
   │CONSULT ││ CONSULT││ CONSULT││ CONSULT││ CONSULT││ CONSULT││ CONSULT││ CONSULT││ CONSULT││ CONSULT│
   │DELEGATE││DELEGATE││DELEGATE││DELEGATE││DELEGATE││DELEGATE││DELEGATE││DELEGATE││DELEGATE││DELEGATE│
   └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
                                          │
                                          │ (All specialists can CONSULT or DELEGATE)
                                          │
                                          ▼
                               ┌─────────────────────────────┐
                               │      VALIDATION LAYER       │
                               │  • Checks acceptance        │
                               │  • Requests revisions       │
                               │  • Aggregates results       │
                               └─────────────────────────────┘
                                          │
                                          ▼
                               ┌─────────────────────────────┐
                               │      FINAL OUTPUT           │
                               └─────────────────────────────┘
```

## Features

- 🤖 **11 Specialized Agents** - Frontend, backend, mobile, AI, DevOps, security, and more
- 📋 **Consult vs Delegate Workflow** - Get advice or get implementations
- 🎯 **User-in-the-Loop** - Approval gates at decision points and destructive actions
- 🔐 **Granular Permissions** - Specialists ask before editing or running commands
- ⚡ **Auto-Execution** - Automatically proceeds within approved plans
- 🛡️ **Smart Pause Points** - Stops at decisions, scope changes, and dangerous actions

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/orchestrator-opencode.git
cd orchestrator-opencode

# Copy agents to OpenCode
cp -r .opencode/agents ~/.config/opencode/
cp -r .opencode/plugins ~/.config/opencode/
```

Or install via npm:

```bash
npm install -g @yourusername/orchestrator-opencode
orchestrator-opencode --install
```

### Usage

1. **Start OpenCode**:
   ```bash
   opencode
   ```

2. **Switch to Orchestrator agent**:
   - Press `Tab` to cycle through agents until you reach "Orchestrator"

3. **Give a complex task**:
   ```
   > Build a REST API for user authentication with JWT tokens
   ```

4. **Approve the plan** when Orchestrator presents it

5. **Watch Orchestrator coordinate specialists** to complete the task

## Agents

### Primary Agent

| Agent | Role |
|-------|------|
| **Orchestrator** | Meta-agent that plans, delegates, and coordinates all work |

### Specialist Subagents

| Agent | Expertise |
|-------|-----------|
| **@frontend-developer** | UI components, React, Vue, accessibility, styling |
| **@backend-architect** | APIs, databases, system design, server-side implementation |
| **@mobile-app-builder** | iOS, Android, React Native, Flutter |
| **@ai-engineer** | ML models, LLMs, prompt engineering, RAG |
| **@devops-automator** | CI/CD, infrastructure, deployment, monitoring |
| **@rapid-prototyper** | Quick MVPs, proof-of-concepts, demos |
| **@sprint-prioritizer** | Backlog grooming, sprint planning, estimation |
| **@growth-hacker** | Analytics, A/B testing, conversion optimization |
| **@security-auditor** | Security auditing, vulnerability assessment, secure coding |
| **@content-creator** | Documentation, marketing copy, technical writing |

## Workflow

### 1. Analysis
Orchestrator analyzes your request and identifies required specialists.

### 2. Planning
Orchestrator presents an execution plan with CONSULT/DELEGATE steps:

```
## Execution Plan

**Request**: Build a REST API for user authentication

**Steps**:
1. [CONSULT] @backend-architect: Review auth strategy options
2. [DELEGATE] @backend-architect: Design API schema
3. [DELEGATE] @backend-architect: Implement auth endpoints

**Identified Pause Points**:
- After Step 1: Decision on authentication strategy

**Approve this plan?** [Yes / Modify / Cancel]
```

### 3. Execution
- Orchestrator auto-executes approved steps
- Pauses at decision boundaries for your input
- Pauses before destructive operations
- Aggregates results from all specialists

## Consult vs Delegate

### CONSULT Mode
Specialist provides **read-only advice** without modifying files:
```
[CONSULT] @backend-architect: What's the best auth strategy for a REST API?
```

### DELEGATE Mode
Specialist **implements** the requested task:
```
[DELEGATE] @backend-architect: Implement JWT authentication endpoints
```

## Examples

### Build a Full-Stack App
```
> Build a todo app with React frontend and Express backend
```

### Create Mobile App
```
> Create a habit tracking iOS app with SwiftUI
```

### Design Infrastructure
```
> Design a CI/CD pipeline for my Node.js project with monitoring
```

### Security Audit
```
> @security-auditor Audit this codebase for vulnerabilities
```

## Architecture

```
.opencode/
├── agents/
│   ├── orchestrator.md           # Primary coordinator agent
│   ├── frontend-developer.md     # Subagent
│   ├── backend-architect.md      # Subagent
│   ├── mobile-app-builder.md     # Subagent
│   ├── ai-engineer.md            # Subagent
│   ├── devops-automator.md       # Subagent
│   ├── rapid-prototyper.md       # Subagent
│   ├── sprint-prioritizer.md     # Subagent
│   ├── growth-hacker.md          # Subagent
│   ├── security-auditor.md       # Subagent
│   └── content-creator.md        # Subagent
└── plugins/
    └── orchestrator.ts           # Fallback validator plugin
```

## Configuration

### Permissions

All specialists have restricted permissions:
- **edit: ask** - Always asks before modifying files
- **bash: ask** - Always asks before running commands
- **task: deny** - Cannot delegate (consult only)

The Orchestrator has:
- **edit: deny** - Never implements directly
- **bash: deny** - Never runs commands
- **task: allow** - Can invoke any subagent

### Customization

Edit any agent markdown file to customize:
- System prompts
- Permission levels
- Temperature and behavior

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute

- Add new specialist agents
- Improve existing agent prompts
- Add documentation and examples
- Report bugs and issues
- Suggest features

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- [OpenCode](https://opencode.ai) - The AI coding agent platform
- [OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl) - Inspiration for multi-agent workflows

---

**Built for developers who want intelligent coordination of specialized AI agents.**
