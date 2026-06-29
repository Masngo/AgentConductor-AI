from abc import ABC, abstractmethod
from typing import Any

class BaseAgent(ABC):
    """
    Base interface for all agents in AgentConductor AI
    """

    @abstractmethod
    def run(self, task: str) -> Any:
        pass