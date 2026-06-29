from utils.logger import get_logger

logger = get_logger()

class UiPathAgent:
    """
    Bridge agent for RPA execution (UiPath or desktop automation)
    """

    def __init__(self):
        self.connected = True

    def run(self, task: str) -> str:
        logger.info(f"UiPathAgent executing automation: {task}")

        # Simulated RPA action
        action = f"UiPath Robot executed automation task: {task}"

        logger.info(action)
        return action