from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
#load_dotenv(dotenv_path=env_path)
load_dotenv()


def get_environment_var(name: str) -> str:
    return os.getenv(name)
