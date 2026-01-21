"""
Blender Engine - Core orchestration and execution engine for the orchestrator-opencode system.

This module provides the core engine functionality for orchestrating multi-agent
workflows and executing code generation tasks.
"""

import asyncio
import json
import logging
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Protocol, Union
from dataclasses import dataclass, field
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """Enumeration of possible task statuses."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TaskType(Enum):
    """Enumeration of supported task types."""
    CODE_GENERATION = "code_generation"
    CODE_REVIEW = "code_review"
    REFACTORING = "refactoring"
    TEST_GENERATION = "test_generation"
    DOCUMENTATION = "documentation"
    ANALYSIS = "analysis"
    ORCHESTRATION = "orchestration"


@dataclass
class TaskContext:
    """Context information for a task execution."""
    task_id: str
    task_type: TaskType
    input_data: Dict[str, Any]
    user_id: Optional[str] = None
    project_path: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class TaskResult:
    """Result from a task execution."""
    task_id: str
    status: TaskStatus
    output: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    execution_time: float = 0.0
    artifacts: Dict[str, str] = field(default_factory=dict)


class AgentProtocol(Protocol):
    """Protocol defining the interface for agents in the system."""
    
    async def execute(self, context: TaskContext) -> TaskResult:
        """Execute the agent's core functionality."""
        ...
    
    @property
    def name(self) -> str:
        """Return the agent's name."""
        ...
    
    @property
    def capabilities(self) -> List[TaskType]:
        """Return the task types this agent can handle."""
        ...


class BlenderEngine:
    """
    Core engine for orchestrating multi-agent workflows.
    
    This engine manages the execution of tasks across multiple agents,
    handling task distribution, status tracking, and result aggregation.
    """
    
    def __init__(self):
        self.agents: Dict[str, AgentProtocol] = {}
        self.task_history: List[TaskResult] = []
        self.active_tasks: Dict[str, asyncio.Task] = {}
        
    def register_agent(self, agent: AgentProtocol) -> None:
        """Register an agent with the engine."""
        self.agents[agent.name] = agent
        logger.info(f"Registered agent: {agent.name}")
    
    def unregister_agent(self, agent_name: str) -> None:
        """Unregister an agent from the engine."""
        if agent_name in self.agents:
            del self.agents[agent_name]
            logger.info(f"Unregistered agent: {agent_name}")
    
    async def execute_task(
        self, 
        context: TaskContext,
        agent_name: Optional[str] = None
    ) -> TaskResult:
        """
        Execute a single task using the appropriate agent.
        
        Args:
            context: The task context containing all necessary information
            agent_name: Optional specific agent to use, otherwise auto-select
            
        Returns:
            TaskResult containing the execution outcome
        """
        start_time = datetime.now()
        task_id = context.task_id
        
        logger.info(f"Starting task {task_id} of type {context.task_type.value}")
        
        # Select agent
        if agent_name:
            if agent_name not in self.agents:
                return TaskResult(
                    task_id=task_id,
                    status=TaskStatus.FAILED,
                    error=f"Agent '{agent_name}' not registered"
                )
            agent = self.agents[agent_name]
        else:
            agent = self._select_agent(context.task_type)
            if not agent:
                return TaskResult(
                    task_id=task_id,
                    status=TaskStatus.FAILED,
                    error=f"No agent available for task type: {context.task_type.value}"
                )
        
        # Execute task
        try:
            result = await agent.execute(context)
            execution_time = (datetime.now() - start_time).total_seconds()
            result.execution_time = execution_time
            result.status = TaskStatus.COMPLETED
            
            logger.info(f"Task {task_id} completed in {execution_time:.2f}s")
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            result = TaskResult(
                task_id=task_id,
                status=TaskStatus.FAILED,
                error=str(e),
                execution_time=execution_time
            )
            logger.error(f"Task {task_id} failed: {e}")
        
        # Store result
        self.task_history.append(result)
        
        return result
    
    async def execute_workflow(
        self,
        tasks: List[TaskContext],
        parallel: bool = False
    ) -> List[TaskResult]:
        """
        Execute a workflow consisting of multiple tasks.
        
        Args:
            tasks: List of task contexts to execute
            parallel: Whether to execute tasks in parallel
            
        Returns:
            List of TaskResult objects for all tasks
        """
        logger.info(f"Executing workflow with {len(tasks)} tasks")
        
        if parallel:
            # Execute all tasks concurrently
            async def run_task(ctx: TaskContext) -> TaskResult:
                return await self.execute_task(ctx)
            
            task_coroutines = [run_task(ctx) for ctx in tasks]
            results = await asyncio.gather(*task_coroutines, return_exceptions=True)
            
            # Handle exceptions
            processed_results = []
            for result in results:
                if isinstance(result, Exception):
                    processed_results.append(TaskResult(
                        task_id="unknown",
                        status=TaskStatus.FAILED,
                        error=str(result)
                    ))
                else:
                    processed_results.append(result)
                    
            return processed_results
            
        else:
            # Execute tasks sequentially
            results = []
            for task_ctx in tasks:
                result = await self.execute_task(task_ctx)
                results.append(result)
                
                # Stop on failure if tasks are sequential
                if result.status == TaskStatus.FAILED:
                    logger.warning(f"Workflow stopped due to task failure: {task_ctx.task_id}")
                    break
                    
            return results
    
    def _select_agent(self, task_type: TaskType) -> Optional[AgentProtocol]:
        """Select an appropriate agent for the given task type."""
        for agent in self.agents.values():
            if task_type in agent.capabilities:
                return agent
        return None
    
    def get_engine_status(self) -> Dict[str, Any]:
        """Get the current status of the engine."""
        return {
            "registered_agents": list(self.agents.keys()),
            "active_tasks": len(self.active_tasks),
            "completed_tasks": len([r for r in self.task_history 
                                  if r.status == TaskStatus.COMPLETED]),
            "failed_tasks": len([r for r in self.task_history 
                                if r.status == TaskStatus.FAILED]),
        }
    
    def get_task_history(self, task_id: Optional[str] = None) -> List[TaskResult]:
        """Get task execution history, optionally filtered by task ID."""
        if task_id:
            return [r for r in self.task_history if r.task_id == task_id]
        return self.task_history


class PipelineBuilder:
    """Builder class for constructing task pipelines."""
    
    def __init__(self, engine: BlenderEngine):
        self.engine = engine
        self.pipeline: List[TaskContext] = []
    
    def add_task(
        self,
        task_type: TaskType,
        input_data: Dict[str, Any],
        agent_name: Optional[str] = None
    ) -> "PipelineBuilder":
        """Add a task to the pipeline."""
        import uuid
        context = TaskContext(
            task_id=str(uuid.uuid4()),
            task_type=task_type,
            input_data=input_data,
            agent_name=agent_name  # This should be part of TaskContext or handled separately
        )
        self.pipeline.append(context)
        return self
    
    def execute(self, parallel: bool = False) -> List[TaskResult]:
        """Execute the constructed pipeline."""
        return asyncio.run(self.engine.execute_workflow(self.pipeline, parallel))


# Example usage and simple agent implementation
class ExampleAgent:
    """Example agent implementation for demonstration."""
    
    def __init__(self, name: str, capabilities: List[TaskType]):
        self._name = name
        self._capabilities = capabilities
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def capabilities(self) -> List[TaskType]:
        return self._capabilities
    
    async def execute(self, context: TaskContext) -> TaskResult:
        """Execute the agent's functionality."""
        # Simple example: echo back with processing
        await asyncio.sleep(0.1)  # Simulate work
        
        return TaskResult(
            task_id=context.task_id,
            status=TaskStatus.COMPLETED,
            output={
                "processed_input": context.input_data,
                "agent_name": self.name,
                "task_type": context.task_type.value
            }
        )


async def main():
    """Main entry point for demonstration."""
    # Create engine
    engine = BlenderEngine()
    
    # Register example agent
    example_agent = ExampleAgent(
        name="example-agent",
        capabilities=[TaskType.CODE_GENERATION, TaskType.CODE_REVIEW]
    )
    engine.register_agent(example_agent)
    
    # Create a task
    task_context = TaskContext(
        task_id="demo-task-1",
        task_type=TaskType.CODE_GENERATION,
        input_data={"prompt": "Create a hello world function"}
    )
    
    # Execute task
    result = await engine.execute_task(task_context)
    print(f"Task result: {result.status.value}")
    print(f"Output: {result.output}")
    
    # Get engine status
    print(f"Engine status: {engine.get_engine_status()}")


if __name__ == "__main__":
    asyncio.run(main())
