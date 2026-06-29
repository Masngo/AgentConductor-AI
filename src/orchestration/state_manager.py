from utils.logger import get_logger
import uuid
import datetime

logger = get_logger()

class StateManager:
    """
    Tracks workflow state across agents
    """

    def __init__(self):
        self.state_store = {}

    def create_state(self, task: str):
        task_id = str(uuid.uuid4())

        self.state_store[task_id] = {
            "task": task,
            "status": "initialized",
            "created_at": str(datetime.datetime.now()),
            "history": []
        }

        logger.info(f"State created for task_id={task_id}")
        return task_id

    def update_state(self, task_id: str, message: str, status: str = None):
        if task_id not in self.state_store:
            logger.error(f"Invalid task_id: {task_id}")
            return

        self.state_store[task_id]["history"].append(message)

        if status:
            self.state_store[task_id]["status"] = status

        logger.info(f"State updated for task_id={task_id}")

    def get_state(self, task_id: str):
        return self.state_store.get(task_id, None)