from typing import Dict, Any
import logging
from agents.base_agent import BaseAgent

logger = logging.getLogger("AgentConductor")


class LangChainAgent(BaseAgent):
    """
    Simulates LangChain reasoning / extraction agent
    """

    def run(self, task: str) -> Dict[str, Any]:

        logger.info(f"[LangChainAgent] processing task: {task}")

        # Simulated reasoning output
        return {
            "agent": "LangChain",
            "task": task,
            "analysis": "Extracted structured business intent",
            "entities": ["vendor", "amount", "invoice"],
            "confidence": 0.91
        }