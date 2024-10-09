import os 
from dotenv import load_dotenv

load_dotenv()

GEMINI_API = os.getenv("GEMINI_API")
if GEMINI_API is None:
    print("Error: GEMINI_API is not set. Please configure your environment variables.")
    exit(1)
