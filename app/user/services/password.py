from datetime import datetime, timedelta
from typing import Literal, Optional
from app.core import config as settings
from jose import jwt
from app.user.services.crud import get_by_email
from sqlalchemy.orm import Session
from app.security.services import create_password_hash


def generate_password_reset_token(email: str) -> str:
    """Generate jwt token for resetting password.

    Generate a JWT token with short expiration time. This token must
    be provided in the next step when the user actually tries to change
    his password.

    Args:
        email (str): The email of the user.

    Returns:
        str: the encoded JWT token.
    """
    delta = timedelta(
        hours=settings.PASSWORD_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.JWT_PASSWORD_RESET_TOKEN, algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    """Verify token that is used to reset the password.

    The JWT token as sent via email and must be provided 
    when trying to reset the password of a user.

    Args:
        token (str): The jwt token.

    Returns:
        Optional[str]: The email address that was the sob of the token. None if token invalid.
    """
    try:
        decoded = jwt.decode(
            token, settings.JWT_PASSWORD_RESET_TOKEN, algorithms="HS256")
        return decoded["sub"]
    except jwt.JWTError:
        return None


def change_password(db: Session, email: str, new_pass: str) -> Optional[Literal[True]]:
    """Change password of the user.

    Reset the password of a user.

    Args:
        db (Session): The database session.
        email (str): The email of the user.
        new_pass (str): The new password

    Returns:
        Optional[Literal[True]]: The updated user.
    """
    user = get_by_email(email=email, db=db)
    if not user:
        return None
    hashed_pass = create_password_hash(new_pass)
    user.password = hashed_pass
    db.commit()
    db.refresh(user)
    return True
