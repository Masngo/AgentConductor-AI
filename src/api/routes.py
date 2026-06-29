from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from src.orchestration.maestro_controller import MaestroController
from src.orchestration.workflow_router import WorkflowRouter
from src.orchestration.state_manager import StateManager
from src.orchestration.exception_handler import ExceptionHandler

router = APIRouter()

# Core systems
maestro = MaestroController()
workflow_router = WorkflowRouter()
state_manager = StateManager()
error_handler = ExceptionHandler()


# -----------------------
# Request Model
# -----------------------
class TaskRequest(BaseModel):
    case_id: str
    process_name: str
    raw_input: str
    mode: str = "auto"


# -----------------------
# EXECUTE FULL CASE
# -----------------------
@router.post("/execute-case")
async def execute_case(request: TaskRequest):

    try:
        payload = request.dict()

        result = await maestro.execute_case_flow(payload)

        return {
            "status": "SUCCESS",
            "case_id": request.case_id,
            "result": result
        }

    except Exception as e:
        error = error_handler.handle(e, "execute-case")
        raise HTTPException(status_code=500, detail=error)


# -----------------------
# ROUTE TASK ONLY
# -----------------------
@router.post("/route-task")
def route_task(task: Dict[str, Any]):

    try:
        result = workflow_router.route(
            task.get("task", ""),
            task.get("mode", "auto")
        )

        return {
            "status": "SUCCESS",
            "result": result
        }

    except Exception as e:
        error = error_handler.handle(e, "route-task")
        raise HTTPException(status_code=500, detail=error)


# -----------------------
# GET STATE
# -----------------------
@router.get("/state/{task_id}")
def get_state(task_id: str):

    state = state_manager.get_state(task_id)

    if not state:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "status": "SUCCESS",
        "state": state
    }