import os

class Settings:
    PROJECT_NAME = "AgentConductor AI"
    VERSION = "1.0.0"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ENV = os.getenv("ENV", "development")

    UI_PATH_ENABLED = True
    HUMAN_APPROVAL_REQUIRED = True

settings = Settings()