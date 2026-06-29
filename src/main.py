from api.fastapi_app import app
from config.env_loader import load_env
from utils.logger import get_logger

logger = get_logger()

def start():
    logger.info("Starting AgentConductor AI system...")
    load_env()

if __name__ == "__main__":
    start()