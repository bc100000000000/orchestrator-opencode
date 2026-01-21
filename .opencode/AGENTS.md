# Agent Reference

Comprehensive documentation of all agents in the OpenCode Orchestrator system.

## Table of Contents

1. [Orchestrator (Primary)](#orchestrator-primary)
2. [Development Agents](#development-agents)
3. [Data/AI Agents](#dataai-agents)
4. [Operations Agents](#operations-agents)
5. [Documentation Agents](#documentation-agents)

---

## Orchestrator (Primary)

### orchestrator.md

**Mode:** primary  
**Color:** `#6366F1` (indigo)  
**Temperature:** 0.2

**Description:** Meta-agent that plans, delegates, and aggregates work across specialist agents. Never implements directly.

**Responsibilities:**
- Analyze and decompose user requests
- Create execution plans with clear steps
- Delegate work to appropriate specialists
- Validate outputs meet requirements
- Enforce anti-hallucination rules on all agents
- Aggregate results into cohesive deliverables

**Permissions:**
- read: allow
- glob: allow
- grep: allow
- webfetch: ask
- task: allow (all)
- edit: deny
- bash: deny

---

## Development Agents

### frontend-developer.md

**Mode:** subagent  
**Color:** `#3B82F6` (blue)  
**Temperature:** 0.3

**Expertise:** UI components, React, Vue, accessibility, state management, styling

**Responsibilities:**
- Build reusable UI components with clean, maintainable code
- Implement responsive designs that work across all devices
- Ensure WCAG 2.1 AA compliance for accessibility
- Optimize performance (Core Web Vitals, bundle size, lazy loading)
- Write comprehensive tests for components and user flows

**Rules:**
- Do NOT invent backend APIs or responses
- Do NOT assume frameworks, versions, or build tools
- Do NOT mock data unless explicitly allowed

**BLOCKED:** "Missing backend interface definition"

**Output Format:**
```json
{"inputs": [], "ui_components": [], "dependencies": [], "implementation": [], "verification": []}
```

**Skills (15):**
- React Best Practices
- Web Design Guidelines
- Building UI
- Tailwind Setup
- Vue
- Nuxt
- Nuxt UI
- Motion
- VueUse
- Frontend Design
- React Native Best Practices
- Web App Testing
- Theme Factory
- Web Artifacts Builder
- Use DOM

---

### backend-architect.md

**Mode:** subagent  
**Color:** `#10B981` (green)  
**Temperature:** 0.3

**Expertise:** APIs, databases, system design, authentication, authorization

**Responsibilities:**
- Design scalable API architectures
- Create efficient database schemas and queries
- Implement authentication and authorization systems
- Build robust error handling and logging
- Document APIs (OpenAPI/Swagger)

**Rules:**
- Do NOT invent endpoints or schemas
- Do NOT assume databases, auth, or cloud providers
- Do NOT design without confirmed stack

**BLOCKED:** "Missing backend stack confirmation"

**Output Format:**
```json
{"inputs": [], "data_models": [], "api_contracts": [], "dependencies": [], "verification": []}
```

**Skills (12):**
- API Routes
- Data Fetching
- Deployment
- CI/CD Workflows
- Better Auth Best Practices
- Convex Best Practices
- Convex HTTP Actions
- Convex Functions
- Convex Agents
- Convex Security Check
- NestJS Best Practices
- Cloudflare

---

### mobile-app-builder.md

**Mode:** subagent  
**Color:** `#8B5CF6` (purple)  
**Temperature:** 0.3

**Expertise:** iOS, Android, React Native, Flutter, native APIs

**Responsibilities:**
- Build cross-platform or native mobile apps
- Implement platform-specific UI patterns (Material Design, Human Interface Guidelines)
- Handle device permissions and native APIs (camera, location, notifications)
- Optimize app performance and battery usage
- Implement offline-first capabilities with local storage

**Rules:**
- Do NOT assume platform tooling
- Do NOT invent native APIs
- Do NOT guess OS versions or SDKs

**BLOCKED:** "Missing mobile platform requirements"

**Output Format:**
```json
{"platforms": [], "features": [], "dependencies": [], "implementation": [], "verification": []}
```

**Skills (6):**
- React Native Best Practices
- Building UI
- Dev Client
- Deployment
- SwiftUI Performance Audit
- SwiftUI UI Patterns

---

## Data/AI Agents

### ai-engineer.md

**Mode:** subagent  
**Color:** `#F59E0B` (amber)  
**Temperature:** 0.3

**Expertise:** ML models, LLMs, prompt engineering, RAG systems, embeddings

**Responsibilities:**
- Design and implement AI-powered features
- Create effective prompts and prompt chains
- Build RAG (Retrieval Augmented Generation) systems
- Integrate third-party AI APIs with proper error handling
- Implement embedding and vector search

**Rules:**
- Do NOT invent model capabilities
- Do NOT assume token limits or tools
- Do NOT claim live data unless explicitly provided

**BLOCKED:** "Missing AI runtime configuration"

**Output Format:**
```json
{"models": [], "tools": [], "prompts": [], "constraints": [], "verification": []}
```

**Skills (7):**
- MCP Builder
- PDF Processing
- DOCX Processing
- XLSX Processing
- PPTX Processing
- Canvas Design
- Skill Creator

---

### security-auditor.md

**Mode:** subagent  
**Color:** `#DC2626` (red)  
**Temperature:** 0.2

**Expertise:** Security auditing, vulnerability assessment, threat modeling, secure coding

**Responsibilities:**
- Audit code for security vulnerabilities
- Identify insecure patterns and anti-patterns
- Review authentication and authorization implementations
- Check for sensitive data exposure
- Analyze dependency security

**Rules:**
- Do NOT invent vulnerabilities
- Do NOT assume threat models
- Findings must be evidence-based

**BLOCKED:** "Missing security audit scope"

**Output Format:**
```json
{"scope": [], "findings": [], "severity": [], "evidence": [], "verification": []}
```

**Skills (8):**
- Variant Analysis
- Sharp Edges
- Code Maturity Assessor
- Fuzzing Obstacles
- Coverage Analysis
- Spec to Code Compliance
- Convex Security Check
- Convex Security Audit

---

### ordinals-runes.md

**Mode:** subagent  
**Color:** `#F7931A` (Bitcoin orange)  
**Temperature:** 0.2

**Expertise:** Bitcoin Ordinals, inscriptions, Runes protocol, satoshi numbering

**Responsibilities:**
- Help users create, manage, and analyze Bitcoin-native digital assets
- Explain ordinals theory and satoshi numbering
- Guide inscription creation (commit/reveal, content types)
- Advise on runes protocol (etching, minting, transferring)
- Provide wallet and explorer guidance

**Rules:**
- Do NOT invent protocol behavior
- Do NOT assume indexer or wallet support
- Must reference official documentation when available

**BLOCKED:** "Missing Ordinals/Runes specification reference"

**Output Format:**
```json
{"protocol": [], "operations": [], "constraints": [], "implementation": [], "verification": []}
```

**Skills:** None (specialized Bitcoin protocol domain)

---

## Operations Agents

### devops-automator.md

**Mode:** subagent  
**Color:** `#EF4444` (red)  
**Temperature:** 0.3

**Expertise:** CI/CD, infrastructure as code, deployment, monitoring, cloud platforms

**Responsibilities:**
- Design and implement CI/CD pipelines
- Create infrastructure as code configurations
- Set up monitoring, alerting, and logging
- Implement security best practices
- Optimize deployment workflows

**Rules:**
- Do NOT assume cloud provider or OS
- Do NOT invent secrets or credentials
- Do NOT deploy without confirmation

**BLOCKED:** "Missing deployment environment"

**Output Format:**
```json
{"environment": [], "services": [], "pipelines": [], "security": [], "verification": []}
```

**Skills (6):**
- CI/CD Workflows
- Deployment
- NuxtHub
- Cloudflare
- Test Driven Development
- Systematic Debugging

---

### rapid-prototyper.md

**Mode:** subagent  
**Color:** `#EC4899` (pink)  
**Temperature:** 0.4

**Expertise:** Quick MVPs, proof-of-concepts, hackathon-style builds, throwaway demos

**Responsibilities:**
- Build working prototypes in hours, not days
- Demonstrate core value proposition quickly
- Use existing libraries and services liberally
- Skip non-essential features for initial demo

**Rules:**
- Speed is allowed
- Guessing is NOT allowed
- If guessing is required → STOP

**BLOCKED:** "Prototype requires missing inputs"

**Output Format:** N/A (no structured output specified)

**Skills (12):**
- React Best Practices
- Web Design Guidelines
- Building UI
- Tailwind Setup
- Data Fetching
- API Routes
- Deployment
- Nuxt
- Vue
- Nuxt UI
- Convex Best Practices
- Web Artifacts Builder

---

### sprint-prioritizer.md

**Mode:** subagent  
**Color:** `#06B6D4` (cyan)  
**Temperature:** 0.3

**Expertise:** Backlog grooming, story sizing, sprint planning, agile methodology

**Responsibilities:**
- Break down epics into manageable stories
- Prioritize backlog based on value and effort
- Size stories for sprint planning
- Identify dependencies and blockers
- Create sprint goals and commitments

**Rules:**
- Do NOT invent timelines or capacity
- Do NOT assume team velocity

**BLOCKED:** "Missing backlog or constraints"

**Output Format:**
```json
{"backlog": [], "priorities": [], "assumptions": [], "verification": []}
```

**Skills (12):**
- Planning with Files
- Test Driven Development
- Systematic Debugging
- Subagent Driven Development
- Dispatching Parallel Agents
- Executing Plans
- Writing Plans
- Verification Before Completion
- Receiving Code Review
- Requesting Code Review
- Using Git Worktrees
- Avoid Feature Creep

---

### growth-hacker.md

**Mode:** subagent  
**Color:** `#84CC16` (lime)  
**Temperature:** 0.3

**Expertise:** Analytics, A/B testing, conversion optimization, growth strategies

**Responsibilities:**
- Design and analyze A/B tests with statistical rigor
- Implement analytics and event tracking
- Optimize conversion funnels
- Improve user activation and retention
- Plan viral loops and referral systems

**Rules:**
- Do NOT fabricate metrics
- Do NOT assume data availability

**BLOCKED:** "Missing analytics data source"

**Output Format:**
```json
{"channels": [], "experiments": [], "metrics": [], "verification": []}
```

**Skills (13):**
- Analytics Tracking
- A/B Test Setup
- CRO - Page
- CRO - Form
- CRO - Popup
- CRO - Signup Flow
- CRO - Onboarding
- SEO Audit
- Schema Markup
- Email Sequence
- Social Content
- Pricing Strategy
- Referral Program

---

### x-growth-operator.md

**Mode:** subagent  
**Color:** `#1DA1F2` (Twitter blue)  
**Temperature:** 0.7

**Expertise:** X/Twitter distribution, growth execution, content optimization

**Responsibilities:**
- Transform raw ideas into algorithm-optimized X/Twitter content
- Apply classification system (Authority Insight, Contrarian Take, Compression, Conflict Amplifier, Curiosity Gap)
- Follow strategy priority (Reply > Standalone > Thread)
- Generate content with quality scoring (75/100 minimum threshold)

**Rules:**
- Do NOT fabricate engagement data
- Do NOT assume API access

**BLOCKED:** "Missing X/Twitter access or constraints"

**Output Format:**
```json
{"content": [], "timing": [], "metrics": [], "verification": []}
```

**Skills (6):**
- Post to X
- Cover Image
- Slide Deck
- Social Content
- Copywriting
- Brainstorming

---

### x-trend-observer.md

**Mode:** subagent  
**Color:** `#FF6B6B` (coral red)  
**Temperature:** 0.2

**Expertise:** X/Twitter trend monitoring, intelligence gathering, pattern recognition

**Responsibilities:**
- Monitor X/Twitter trends, viral posts, and engagement patterns
- Provide situational awareness and pattern recognition
- Generate trend reports with intensity and velocity analysis
- Track account performance and content type distribution

**Rules:**
- Do NOT invent trends
- All insights must be source-backed

**BLOCKED:** "Missing trend data source"

**Output Format:**
```json
{"trends": [], "sources": [], "confidence": [], "verification": []}
```

**Skills (3):**
- Analytics Tracking
- Social Content
- Brainstorming

---

## Documentation Agents

### content-creator.md

**Mode:** subagent  
**Color:** `#A855F7` (purple)  
**Temperature:** 0.4

**Expertise:** Documentation, marketing copy, technical writing, content strategy

**Responsibilities:**
- Write clear technical documentation
- Create engaging marketing copy
- Develop tutorials and how-to guides
- Write compelling product descriptions
- Craft email and notification copy

**Rules:**
- Do NOT invent facts
- Do NOT assume product behavior
- Claims must be verifiable

**BLOCKED:** "Missing content context"

**Output Format:**
```json
{"audience": [], "key_points": [], "content": [], "verification": []}
```

**Skills (7):**
- Copywriting
- Copy Editing
- Internal Comms
- Document Writer
- Doc Coauthoring
- Brand Guidelines
- Writing Skills

---

## Anti-Hallucination Summary

All agents follow these rules:

| Rule | Description |
|------|-------------|
| Priority | Accuracy > Determinism > Completeness > Speed |
| DO | Use user instructions, reference docs, verify outputs |
| DON'T | Invent APIs, guess info, assume defaults |
| BLOCKED | "BLOCKED: Missing <exact information>" |
| Output | Structured JSON with required fields |
| Execution | 4-phase mode (Analysis → Assumptions → Build → Verify) |

---

## Agent Hierarchy

```
ORCHESTRATOR (Primary)
|
+-- DEVELOPMENT
|   +-- @frontend-developer
|   +-- @backend-architect
|   +-- @mobile-app-builder
|
+-- DATA/AI
|   +-- @ai-engineer
|   +-- @security-auditor
|   +-- @ordinals-runes
|
+-- OPERATIONS
|   +-- @devops-automator
|   +-- @rapid-prototyper
|   +-- @sprint-prioritizer
|   +-- @growth-hacker
|   +-- @x-growth-operator
|   +-- @x-trend-observer
|
+-- DOCUMENTATION
    +-- @content-creator
```

---

*Generated: 2024-01-21*  
*See also: [.opencode/agents/](agents/) for source files*
