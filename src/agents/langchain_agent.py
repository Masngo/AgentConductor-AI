from config.settings import settings
from utils.logger import get_logger

logger = get_logger()

class LangChainAgent:
    """
    LLM-based reasoning agent (simplified LangChain-style wrapper)
    """

    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY

    def run(self, task: str) -> str:
        logger.info(f"LangChainAgent received task: {task}")

        # Simulated LLM response (replace with real OpenAI/LangChain later)
        response = f"[LangChainAgent] Processed task: {task}"

        logger.info(f"LangChainAgent response: {response}")
        return response