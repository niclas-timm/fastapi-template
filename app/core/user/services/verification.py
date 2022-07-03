"""
Verification service for the users package.
"""

from datetime import datetime, timedelta
from typing import Optional
from app.core import config as settings
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Literal
from app.core.user.services import crud


def generate_email_verification_token(email: str) -> str:
    """Generate token for email verification.

    Generate a jwt token with a short expiration time with
    an email address as the sub. The token will be sent via email
    in order to verify the users email.

    Args:
        email (str): The email that will be the sub of the token.

    Returns:
        str: The token.
    """
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.JWT_EMAIL_VERIFICATION_TOKEN, algorithm="HS256",
    )
    return encoded_jwt


def verify_email_token(token: str) -> Optional[str]:
    """Verify email verification token.

    Args:
        token (str): The token to be verified.

    Returns:
        Optional[str]: If token is valid, the sub (email) from the token.
    """
    try:
        decoded = jwt.decode(
            token, settings.JWT_EMAIL_VERIFICATION_TOKEN, algorithms="HS256")
        return decoded["sub"]
    except JWTError:
        return None


def verify_email(db: Session, email: str) -> Optional[Literal[True]]:
    user = crud.get_by_email(email=email, db=db)
    if not user:
        return None
    user.email_verified = True
    db.commit()
    db.refresh(user)
    return True
