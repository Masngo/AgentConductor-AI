from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from src.orchestration.maestro_controller import MaestroController
from src.orchestration.workflow_router import WorkflowRouter

router = APIRouter()

maestro = MaestroController()
workflow_router = WorkflowRouter()


class TaskRequest(BaseModel):
    case_id: str
    process_name: str
    raw_input: str
    mode: str = "auto"


@router.post("/execute-case")
async def execute_case(request: TaskRequest):

    try:
        result = await maestro.execute_case_flow(request.dict())
        return {"status": "SUCCESS", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/route-task")
def route_task(task: Dict[str, Any]):

    try:
        return workflow_router.route(task.get("task", ""), task.get("mode", "auto"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))