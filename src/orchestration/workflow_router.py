from agents.langchain_agent import LangChainAgent
from agents.crewai_agent import CrewAIAgent
from agents.autogen_agent import AutoGenAgent
from agents.uipath_agent import UiPathAgent

from utils.logger import get_logger

logger = get_logger()

class WorkflowRouter:
    """
    Decides which agent should handle the task
    """

    def __init__(self):
        self.langchain = LangChainAgent()
        self.crewai = CrewAIAgent()
        self.autogen = AutoGenAgent()
        self.uipath = UiPathAgent()

    def route(self, task: str, mode: str = "auto") -> str:
        logger.info(f"Routing task: {task} | mode={mode}")

        if mode == "langchain":
            return self.langchain.run(task)

        elif mode == "crewai":
            return self.crewai.run(task)

        elif mode == "autogen":
            return self.autogen.run(task)

        elif mode == "uipath":
            return self.uipath.run(task)

        # AUTO MODE (smart routing simulation)
        if "automation" in task.lower():
            return self.uipath.run(task)

        elif "plan" in task.lower():
            return self.crewai.run(task)

        elif "chat" in task.lower():
            return self.autogen.run(task)

        else:
            return self.langchain.run(task)