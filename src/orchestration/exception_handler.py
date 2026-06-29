from src.utils.logger import get_logger
import traceback

logger = get_logger()

class ExceptionHandler:
    """
    Central error handling for all workflows
    """

    def handle(self, error: Exception, context: str = ""):
        error_msg = str(error)
        stack = traceback.format_exc()

        logger.error(f"ERROR CONTEXT: {context}")
        logger.error(f"ERROR MESSAGE: {error_msg}")
        logger.error(f"STACK TRACE:\n{stack}")

        return {
            "status": "failed",
            "context": context,
            "error": error_msg
        }