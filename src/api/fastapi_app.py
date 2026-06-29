from fastapi import FastAPI
from src.api.routes import router
from config.settings import settings
from utils.logger import get_logger

logger = get_logger()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(router)

@app.get("/")
def home():
    logger.info("Health check hit")
    return {
        "status": "AgentConductor AI is running",
        "version": settings.VERSION
    }