from jose import jwt
from passlib.context import CryptContext
from typing import Any, Union
from app.core.settings import get_environment_var

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
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
