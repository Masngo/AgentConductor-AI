from fastapi import APIRouter
from src.orchestration.maestro_controller import MaestroController
from src.orchestration.state_manager import StateManager
router = APIRouter()

maestro = MaestroController()
state_manager = StateManager()

# In-memory task tracker (simple MVP)
TASK_REGISTRY = {}


@router.post("/execute-task")
def execute_task(payload: dict):
    """
    Expected JSON:
    {
        "task": "your instruction",
        "mode": "auto" | "langchain" | "crewai" | "autogen" | "uipath"
    }
    """

    task = payload.get("task")
    mode = payload.get("mode", "auto")

    result = maestro.execute(task, mode)

    TASK_REGISTRY[result["task_id"]] = result

    return result


@router.get("/status/{task_id}")
def get_status(task_id: str):
    """
    Returns execution status + history
    """

    state = state_manager.get_state(task_id)

    if not state:
        return {
            "status": "not_found",
            "message": "Invalid task_id"
        }

    return state


@router.get("/tasks")
def list_tasks():
    """
    Debug endpoint: list all tasks
    """
    return TASK_REGISTRY