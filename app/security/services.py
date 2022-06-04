from jose import jwt
from passlib.context import CryptContext
from typing import Any, Union
from app.core.settings import get_environment_var

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SecurityService():

    def create_access_token(
        subject: Union[str, Any]
    ) -> str:
        to_encode = {"sub": str(subject)}
        encoded_jwt = jwt.encode(
            to_encode, get_environment_var('JWT_TOKEN'), algorithm=ALGORITHM)
        return encoded_jwt

    def create_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
