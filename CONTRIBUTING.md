# Contributing to OpenCode Orchestrator System

Thank you for your interest in contributing! This document provides guidelines and instructions.

## Ways to Contribute

- 🐛 **Bug Reports** - Found an issue? Open an issue
- 💡 **Feature Requests** - Have an idea? Share it
- 📝 **Documentation** - Improve docs and examples
- 🤖 **New Agents** - Add specialist agents for new domains
- 🎨 **Improvements** - Enhance existing agent prompts
- 🧪 **Testing** - Test and report results

## Getting Started

### Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git
- Node.js (for npm packaging)

### Development Setup

1. **Fork the repository** on GitHub

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/orchestrator-opencode.git
   cd orchestrator-opencode
   ```

3. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make changes** to agent files in `.opencode/agents/`

5. **Test your changes**:
   ```bash
   # Copy to your OpenCode config
   cp -r .opencode/agents ~/.config/opencode/
   
   # Test in OpenCode
   opencode
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: Description of your changes"
   ```

7. **Push and create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Agent Development Guidelines

### Creating a New Agent

1. Create a new markdown file in `.opencode/agents/`:
   ```bash
   touch .opencode/agents/new-specialist.md
   ```

2. Follow the standard agent template:

```markdown
---
description: Brief description of the specialist
mode: subagent  # or "primary" for main agents
color: "#HEXCODE"  # Visual color in UI
temperature: 0.3
permission:
  edit: ask
  read: allow
  bash:
    "*": ask
  task: deny
  webfetch: ask
---

# Specialist Name Agent

## Role
[One paragraph describing the specialist]

## Interaction Modes

### When MODE: CONSULT
- What advice can they provide?

### When MODE: DELEGATE  
- What tasks can they implement?

## Core Competencies
- List key skills and technologies

## Responsibilities
- List main responsibilities

## Output Standards
- Expected deliverables and format

## Consultation Topics
- What can they advise on?

## Cross-Agent Consultation
- What other agents can they consult (not delegate)?
```

### Agent Best Practices

- Use `mode: subagent` for specialists (cannot delegate)
- Use `mode: primary` only for orchestration agents
- Always set `task: deny` for specialists (consult only)
- Use `edit: ask` and `bash: ask` for safety
- Provide clear, specific prompts
- Include examples in the output format

## Code Style

- Use consistent formatting in markdown
- Follow the existing file structure
- Use clear, descriptive names
- Include comments for complex logic

## Testing

Before submitting:

1. ✅ Test the agent in OpenCode
2. ✅ Verify permissions work correctly
3. ✅ Check CONSULT mode provides advice only
4. ✅ Check DELEGATE mode implements tasks
5. ✅ Test cross-agent consultations

## Reporting Issues

When reporting bugs, include:

- Steps to reproduce
- Expected behavior
- Actual behavior
- OpenCode version
- Relevant logs
- Screenshot if applicable

## Questions?

- Open an issue for questions
- Join the [OpenCode Discord](https://opencode.ai/discord)
- Check existing issues first

---

**Thank you for contributing!**
