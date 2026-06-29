import logging
from typing import Dict, Any

from agents.langchain_agent import LangChainAgent
from agents.crewai_agent import CrewAIAgent
from agents.autogen_agent import AutoGenAgent
from agents.uipath_agent import UiPathAgent

logger = logging.getLogger("AgentConductor")


class WorkflowRouter:
    """
    Intelligent routing layer for selecting the correct AI/RPA agent.
    Simulates enterprise decision engine used in UiPath Maestro.
    """

    def __init__(self):

        self.langchain = LangChainAgent()
        self.crewai = CrewAIAgent()
        self.autogen = AutoGenAgent()
        self.uipath = UiPathAgent()

    def route(self, task: str, mode: str = "auto") -> Dict[str, Any]:

        logger.info(f"[ROUTER] task={task} | mode={mode}")

        # Manual override mode
        if mode == "langchain":
            return self.langchain.run(task)

        if mode == "crewai":
            return self.crewai.run(task)

        if mode == "autogen":
            return self.autogen.run(task)

        if mode == "uipath":
            return self.uipath.run(task)

        # AUTO ROUTING (enterprise simulation logic)
        task_lower = task.lower()

        if any(keyword in task_lower for keyword in ["invoice", "automation", "erp", "rpa"]):
            return self._wrap_response("uipath", self.uipath.run(task))

        if any(keyword in task_lower for keyword in ["plan", "strategy", "workflow"]):
            return self._wrap_response("crewai", self.crewai.run(task))

        if any(keyword in task_lower for keyword in ["chat", "conversation", "dialog"]):
            return self._wrap_response("autogen", self.autogen.run(task))

        # DEFAULT → LangChain reasoning agent
        return self._wrap_response("langchain", self.langchain.run(task))

    def _wrap_response(self, agent_name: str, result: Any) -> Dict[str, Any]:

        return {
            "agent": agent_name,
            "status": "SUCCESS",
            "output": result
        }