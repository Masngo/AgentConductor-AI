import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from src.orchestration.maestro_controller import MaestroController
from src.orchestration.workflow_router import WorkflowRouter
from src.orchestration.state_manager import StateManager
from src.orchestration.exception_handler import ExceptionHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgentConductor")

app = FastAPI(title="AgentConductor AI", version="1.0")

# Core systems
maestro = MaestroController()
router = WorkflowRouter()
state_manager = StateManager()
error_handler = ExceptionHandler()


# -----------------------------
# Request Schema
# -----------------------------
class TaskRequest(BaseModel):
    case_id: str
    process_name: str
    raw_input: str
    mode: str = "auto"


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/")
def health_check():
    return {
        "status": "running",
        "system": "AgentConductor AI",
        "message": "Enterprise AI Orchestration Platform Active"
    }


# -----------------------------
# EXECUTE FULL CASE
# -----------------------------
@app.post("/execute-case")
async def execute_case(request: TaskRequest):

    try:
        logger.info(f"Received case: {request.case_id}")

        payload = {
            "case_id": request.case_id,
            "process_name": request.process_name,
            "raw_input": request.raw_input
        }

        result = await maestro.execute_case_flow(payload)

        return {
            "status": "SUCCESS",
            "case_id": request.case_id,
            "result": result
        }

    except Exception as e:

        error = error_handler.handle(e, "API /execute-case")

        raise HTTPException(status_code=500, detail=error)


# -----------------------------
# ROUTE TASK ONLY (DEBUG ENDPOINT)
# -----------------------------
@app.post("/route-task")
def route_task(task: Dict[str, Any]):

    try:
        task_text = task.get("task", "")

        result = router.route(task_text)

        return {
            "status": "SUCCESS",
            "task": task_text,
            "routing_result": result
        }

    except Exception as e:

        error = error_handler.handle(e, "API /route-task")

        raise HTTPException(status_code=500, detail=error)


# -----------------------------
# GET STATE (CASE TRACKING)
# -----------------------------
@app.get("/state/{task_id}")
def get_state(task_id: str):

    state = state_manager.get_state(task_id)

    if not state:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "status": "SUCCESS",
        "task_id": task_id,
        "state": state
    }