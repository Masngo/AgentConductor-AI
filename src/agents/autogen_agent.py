from utils.logger import get_logger

logger = get_logger()

class AutoGenAgent:
    """
    Simulates conversational multi-agent AutoGen-style loop
    """

    def __init__(self):
        self.history = []

    def run(self, task: str) -> str:
        logger.info(f"AutoGenAgent starting dialogue for: {task}")

        self.history.append({"role": "user", "content": task})

        assistant_reply = f"AutoGen reasoning completed for: {task}"
        self.history.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply