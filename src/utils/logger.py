from loguru import logger

def get_logger():
    logger.add("logs/agentconductor.log", rotation="10 MB")
    return logger