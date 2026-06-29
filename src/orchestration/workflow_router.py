import logging
from typing import Any, Dict

from src.agents.langchain_agent import LangChainAgent
from src.agents.crewai_agent import CrewAIAgent
from src.agents.autogen_agent import AutoGenAgent
from src.agents.uipath_agent import UiPathAgent

logger = logging.getLogger("AgentConductor")


class WorkflowRouter:

    def __init__(self):
        self.langchain = LangChainAgent()
        self.crewai = CrewAIAgent()
        self.autogen = AutoGenAgent()
        self.uipath = UiPathAgent()

    def route(self, task: str, mode: str = "auto") -> Dict[str, Any]:

        task_lower = task.lower()

        if mode == "langchain":
            return self._wrap("langchain", self.langchain.run(task))

        if mode == "crewai":
            return self._wrap("crewai", self.crewai.run(task))

        if mode == "autogen":
            return self._wrap("autogen", self.autogen.run(task))

        if mode == "uipath":
            return self._wrap("uipath", self.uipath.run(task))

        if "erp" in task_lower or "automation" in task_lower:
            return self._wrap("uipath", self.uipath.run(task))

        if "plan" in task_lower:
            return self._wrap("crewai", self.crewai.run(task))

        if "chat" in task_lower:
            return self._wrap("autogen", self.autogen.run(task))

        return self._wrap("langchain", self.langchain.run(task))

    def _wrap(self, agent: str, result: Any) -> Dict[str, Any]:
        return {
            "agent": agent,
            "status": "SUCCESS",
            "output": result
        }