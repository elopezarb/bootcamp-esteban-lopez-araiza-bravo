# Config 

try:
    import os
    from dotenv import load_dotenv
    from pathlib import Path
    from typing import Optional
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise

def load_env():
    load_dotenv()  # looks for a .env file in the current and parent directories
    print(".env loaded (if present)")

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)