from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

    required_vars = ["OPENAI_API_KEY"]

    for var in required_vars:
        if not os.getenv(var):
            print(f"[WARNING] Missing environment variable: {var}")