from jose import jwt
from passlib.context import CryptContext
from typing import Any, Union
from app.core.config import get_environment_var

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
        subject: Union[str, Any]
) -> str:
    """ Generate user access token

    Generate a JWT access token with the id of the user as the sub.
    """
    to_encode = {"sub": str(subject)}
    secret = get_environment_var('JWT_TOKEN')
    encoded_jwt = jwt.encode(
        to_encode, secret, algorithm=ALGORITHM)
    return encoded_jwt


def create_password_hash(password: str) -> str:
    """Hash a password.

    Args:
        password (str): The password that should be hashed.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash.

    Get password in plain version and check it against the hashed password.

    Args:
        plain_password (str): The plain password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if password is valid.
    """
    return pwd_context.verify(plain_password, hashed_password)
