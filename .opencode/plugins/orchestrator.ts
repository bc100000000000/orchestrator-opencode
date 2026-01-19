import type { Plugin, Hooks } from "@opencode-ai/plugin";

/**
 * Orchestrator Validator Plugin
 * 
 * ROLE: Fallback and validation - NOT the primary agent registration path.
 * 
 * Primary agents are now defined via markdown files in .opencode/agents/
 * This plugin provides:
 * 1. Validation that expected agents are configured
 * 2. Logging of delegation events for audit trail
 * 3. Fallback agent configs if markdown files are missing
 */

// Expected agents that should be defined via markdown
const EXPECTED_AGENTS = [
  "orchestrator",
  "frontend-developer",
  "backend-architect",
  "mobile-app-builder",
  "ai-engineer",
  "devops-automator",
  "rapid-prototyper",
  "sprint-prioritizer",
  "growth-hacker",
  "content-creator",
] as const;

// Minimal fallback configs (used only if markdown agents are missing)
const FALLBACK_CONFIGS: Record<string, { description: string; mode: string; color: string }> = {
  "orchestrator": {
    description: "Meta-agent coordinator (fallback - markdown agent missing)",
    mode: "primary",
    color: "#6366F1",
  },
  "frontend-developer": {
    description: "Frontend specialist (fallback)",
    mode: "subagent",
    color: "#3B82F6",
  },
  "backend-architect": {
    description: "Backend specialist (fallback)",
    mode: "subagent",
    color: "#10B981",
  },
  "mobile-app-builder": {
    description: "Mobile specialist (fallback)",
    mode: "subagent",
    color: "#8B5CF6",
  },
  "ai-engineer": {
    description: "AI/ML specialist (fallback)",
    mode: "subagent",
    color: "#F59E0B",
  },
  "devops-automator": {
    description: "DevOps specialist (fallback)",
    mode: "subagent",
    color: "#EF4444",
  },
  "rapid-prototyper": {
    description: "Prototyping specialist (fallback)",
    mode: "subagent",
    color: "#EC4899",
  },
  "sprint-prioritizer": {
    description: "Agile/planning specialist (fallback)",
    mode: "subagent",
    color: "#06B6D4",
  },
  "growth-hacker": {
    description: "Growth specialist (fallback)",
    mode: "subagent",
    color: "#84CC16",
  },
  "content-creator": {
    description: "Content specialist (fallback)",
    mode: "subagent",
    color: "#A855F7",
  },
};

export const OrchestratorValidator: Plugin = async (ctx) => {
  const { project } = ctx;
  
  const hooks: Hooks = {
    /**
     * Config hook: Validates agent configuration and provides fallbacks
     */
    async config(config) {
      // Initialize agent config if needed
      if (!config.agent) {
        config.agent = {};
      }

      const missingAgents: string[] = [];
      const configuredAgents: string[] = [];

      // Check each expected agent
      for (const agentName of EXPECTED_AGENTS) {
        if (config.agent[agentName]) {
          configuredAgents.push(agentName);
        } else {
          missingAgents.push(agentName);
          // Apply fallback config
          const fallback = FALLBACK_CONFIGS[agentName];
          if (fallback) {
            config.agent[agentName] = {
              description: fallback.description,
              mode: fallback.mode as "primary" | "subagent" | "all",
              color: fallback.color,
              prompt: `# ${agentName} (Fallback Mode)\n\nThis agent is running in fallback mode. The markdown definition at .opencode/agents/${agentName}.md was not found.\n\nPlease ensure the agent markdown file exists for full functionality.`,
            };
          }
        }
      }

      // Log validation results (these will appear in OpenCode logs)
      if (missingAgents.length > 0) {
        console.warn(
          `[Orchestrator Validator] Missing markdown agents (using fallback): ${missingAgents.join(", ")}`
        );
        console.warn(
          `[Orchestrator Validator] Expected location: .opencode/agents/<agent-name>.md`
        );
      }

      if (configuredAgents.length > 0) {
        console.log(
          `[Orchestrator Validator] Validated agents: ${configuredAgents.join(", ")}`
        );
      }
    },

    /**
     * Tool execution hook: Log delegation events for audit trail
     */
    "tool.execute.before": async (input, output) => {
      // Track Task tool usage (agent delegations)
      if (input.tool === "task") {
        const args = output.args as { subagent_type?: string; description?: string } | undefined;
        if (args?.subagent_type) {
          console.log(
            `[Orchestrator Audit] Delegation: ${args.subagent_type} - ${args.description || "No description"}`
          );
        }
      }
    },

    /**
     * Tool execution hook: Log delegation results
     */
    "tool.execute.after": async (input, output) => {
      if (input.tool === "task") {
        console.log(
          `[Orchestrator Audit] Delegation completed: ${input.callID} - ${output.title}`
        );
      }
    },
  };

  return hooks;
};

// Default export for OpenCode plugin loader
export default OrchestratorValidator;
