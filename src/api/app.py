from fastapi import FastAPI
from src.api.routes import router
from src.api.middleware import setup_middleware

app = FastAPI(
    title="AgentConductor AI",
    description="Enterprise Multi-Agent Orchestration Platform",
    version="1.0.0"
)

# Attach middleware
setup_middleware(app)

# Register routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "status": "running",
        "system": "AgentConductor AI",
        "message": "Multi-Agent Enterprise Orchestration Platform Active"
    }