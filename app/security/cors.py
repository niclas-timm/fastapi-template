from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import config
from typing import List


def add_cors(app: FastAPI):
    """Add cors to the app object.

    Increase security of the app by adding cors.

    Args:
        app (FastAPI): The FastAPI app object cors will be added to.
    """
    origins = get_allowed_origins()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins
    )


def get_allowed_origins() -> List[str]:
    """Get allowed origins from environment config.

    In the .env file, allowed origins will be separated by comma.
    Turn this into a list.

    Returns:
        List[str]: The allowed origins in List format.
    """
    allowed_origins_as_string = config.CORS_ALLOWED_ORIGINS
    if allowed_origins_as_string is None:
        return []
    allowed_origins_as_list = list(allowed_origins_as_string.split(','))
    return allowed_origins_as_list
