import os
from pathlib import Path
from dotenv import load_dotenv

# This finds the absolute path to the folder containing config.py
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Add this temporary print to see what's actually happening
if OPENAI_API_KEY:
    print(f"✅ Success! Key loaded (starts with: {OPENAI_API_KEY[:5]}...)")
else:
    print("❌ Failure: Key is still None. Check .env filename and content.")
