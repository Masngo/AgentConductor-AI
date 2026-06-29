import uuid
import datetime
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("AgentConductor")


class StateManager:
    """
    Tracks workflow state across AI agents, RPA bots, and human approvals.
    Acts as in-memory case management system (like UiPath Orchestrator).
    """

    def __init__(self):
        self.state_store: Dict[str, Dict[str, Any]] = {}

    def create_state(self, task: str) -> str:

        task_id = str(uuid.uuid4())

        self.state_store[task_id] = {
            "task": task,
            "status": "INITIALIZED",
            "created_at": datetime.datetime.utcnow().isoformat(),
            "history": []
        }

        logger.info(f"[STATE CREATED] task_id={task_id}")

        return task_id

    def update_state(
        self,
        task_id: str,
        message: str,
        status: Optional[str] = None,
        agent: str = "system"
    ) -> None:

        if task_id not in self.state_store:

            logger.error(f"[STATE ERROR] Invalid task_id={task_id}")

            return

        event = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "message": message,
            "agent": agent
        }

        self.state_store[task_id]["history"].append(event)

        if status:
            self.state_store[task_id]["status"] = status

        logger.info(f"[STATE UPDATED] task_id={task_id} | status={status}")

    def get_state(self, task_id: str) -> Optional[Dict[str, Any]]:

        return self.state_store.get(task_id)

    def list_states(self) -> Dict[str, Dict[str, Any]]:

        return self.state_store