import logging
import traceback
from typing import Dict, Any

logger = logging.getLogger("AgentConductor")


class ExceptionHandler:
    """
    Centralized error handling system for all workflows.
    Used across AI agents, RPA, and orchestration engine.
    """

    def handle(self, error: Exception, context: str = "") -> Dict[str, Any]:

        error_msg = str(error)
        stack_trace = traceback.format_exc()

        logger.error("========== AGENTCONDUCTOR ERROR ==========")
        logger.error(f"CONTEXT: {context}")
        logger.error(f"ERROR MESSAGE: {error_msg}")
        logger.error(f"STACK TRACE:\n{stack_trace}")
        logger.error("==========================================")

        return {
            "status": "FAILED",
            "error_type": type(error).__name__,
            "context": context,
            "message": error_msg,
            "action": "REROUTE_TO_FALLBACK_OR_HUMAN"
        }