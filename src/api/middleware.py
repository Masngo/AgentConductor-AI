import time
import logging
from fastapi import Request

logger = logging.getLogger("AgentConductor")


def setup_middleware(app):

    @app.middleware("http")
    async def log_requests(request: Request, call_next):

        start_time = time.time()

        logger.info(f"Incoming request: {request.method} {request.url}")

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"Completed {request.method} {request.url} in {process_time:.4f}s"
        )

        response.headers["X-Process-Time"] = str(process_time)

        return response