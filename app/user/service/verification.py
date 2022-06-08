from datetime import datetime, timedelta
from typing import Any, Optional
from app.core import config as settings
from jose import jwt


def generate_email_verification_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.JWT_EMAIL_VERIFICATION_TOKEN, algorithm="HS256",
    )
    return encoded_jwt


def verify_email_token(token: str) -> Optional[str]:
    try:
        decoded = jwt.decode(
            token, settings.JWT_EMAIL_VERIFICATION_TOKEN, algorithms="HS256")
        return decoded["sub"]
    except jwt.JWTError:
        return None
