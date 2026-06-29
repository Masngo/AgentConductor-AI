from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import os
from src.orchestration.maestro_controller import UiPathMaestroController

app = FastAPI(title="AgentConductor AI Orchestration Core")
controller = UiPathMaestroController()

class TransactionCasePayload(BaseModel):
    case_id: str
    process_name: str
    raw_input: str
    priority: Optional[str] = "Normal"

@app.get("/", response_class=HTMLResponse)
def read_root():
    frontend_path = "frontend/index.html"
    if os.path.exists(frontend_path):
        with open(frontend_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>AgentConductor API Core Online</h1>"

@app.post("/api/v1/orchestrate")
async def process_transaction_workflow(payload: TransactionCasePayload):
    try:
        result = await controller.execute_case_flow(payload.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
