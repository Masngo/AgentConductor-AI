# AgentConductor AI

> **Enterprise AI orchestration platform that unifies AI agents, UiPath RPA, and human-in-the-loop workflows using UiPath Maestro. Enables resilient, scalable, and governed multi-agent business process automation across enterprise systems.**

## 🌟 Core Features Built
* **FastAPI Orchestration Interface Gateway (`src/api/fastapi_app.py`)**: Central control plane exposing the multi-agent pipeline routes.
* **UiPath Maestro Controller Engine (`src/orchestration/maestro_controller.py`)**: Handles the sequential execution matrix routing AI parameters directly to local Unattended Robotic loops.
* **Data Schema Validation Middleware (`src/utils/json_validator.py`)**: Cleans, strips, and normalizes erratic LLM output responses into reliable structural parameters.
* **Resilience Framework Guard (`src/orchestration/exception_handler.py`)**: Self-healing protocol catches AI hallucination states or link drops safely.
* **Enterprise Control Dashboard (`frontend/index.html`)**: Elite dark-mode monitoring center with dynamic progress visual tracking lines.

## 🛠️ How To Run
1. Run backend server: `uvicorn src.api.fastapi_app:app --reload`
2. Open frontend application dashboard directly by opening `frontend/index.html` in Chrome or navigating directly to `http://127.0.0.1:8000`.
