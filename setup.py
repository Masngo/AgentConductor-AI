from setuptools import setup, find_packages

setup(
    name="AgentConductor-AI",
    version="1.0.0",
    description="Multi-agent orchestration system with RPA and human-in-the-loop control",
    author="AgentConductor Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "python-dotenv",
        "requests",
        "loguru",
    ],
    python_requires=">=3.9",
)