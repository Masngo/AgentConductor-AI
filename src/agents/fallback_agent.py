from typing import Dict, Any
import logging
from agents.base_agent import BaseAgent

logger = logging.getLogger("AgentConductor")


class FallbackAgent(BaseAgent):
    """
    Used when all other agents fail.
    Ensures system never breaks.
    """

    def run(self, task: str) -> Dict[str, Any]:

        logger.warning(f"[FallbackAgent] activated for task: {task}")

        return {
            "agent": "Fallback",
            "task": task,
            "status": "degraded_execution",
            "action": "escalated_to_human",
            "reason": "primary_agents_failed"
        }