import logging

logger = logging.getLogger("AgentConductor")


class ResilienceManager:

    async def handle_ai_hallucination_fallback(self, payload):

        return {
            "vendor": "fallback_system",
            "total_amount": 1000,
            "confidence": 0.5,
            "fallback_used": True
        }