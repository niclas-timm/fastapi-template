from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from app.core import config as settings
from jose import jwt
#from app.core.user.services.crud import get_by_email
from sqlalchemy.orm import Session
from app.core.security.services import create_password_hash
from app.core.user.model import UserModel


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


def change_password(db: Session, email: str, new_pass: str):
    """Change password of the user.

    Reset the password of a user.

    Args:
        db (Session): The database session.
        email (str): The email of the user.
        new_pass (str): The new password

    Returns:
        Optional[Literal[True]]: The updated user.
    """
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        return {"error": True, "msg": "User not found."}
    is_password_valid = password_requirements_check(new_pass)
    if is_password_valid["error"]:
        return {"error": True, "msg": is_password_valid["msg"]}
    hashed_pass = create_password_hash(new_pass)
    user.password = hashed_pass
    db.commit()
    db.refresh(user)
    return True


def password_requirements_check(password: str) -> Dict[str, Any]:
    """Password rules

    Check if a password meets a list of requirements:
    - Minimum of 8 characters
    - May not contain "passwor" or "1234"
    - May not have spaces
    - Must have at least one special character

    Args:
        password (str): The password to be checked.

    Returns:
        Dict[str, Any]: error and msg. error will be True if the password does not meet requirements.
        More detailed information will be in msg. Msg will be empty if password meets requirements.
    """
    if len(password) < 8:
        return {"error": True, "msg": "Password must have at least 8 characters."}
    if "passwor" in password:
        return {"error": True, "msg": "Your password may not contain 'passwor'"}
    if "1234" in password:
        return {"error": True, "msg": "Password may not contain '1234'"}
    if " " in password:
        return {"error": True, "msg": "Password may not have spaces."}
    if password.isalnum():
        return {"error": True, "msg": "Password must have at least 1 special character."}
    return {"error": False, "msg": ""}
