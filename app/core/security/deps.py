"""
Dependencies for the security package.
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core import config
from app.core.security.models import TokenData
from app.core.user.services.crud import get_by_id
from app.core.roles.roles import Roles
from app.core.roles.guard import user_has_role
from app.core.db.db import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"
CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
ROLE_EXEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid permissions",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_user_from_jwt(db: Session, token: str, exception=CREDENTIALS_EXCEPTION):
    """Get currently authenticated user from jwt token.

    Args:
        db (Session): The database session.
        token (str): The jwt token.
        exception (_type_, optional): If user not found or token not valid.

    Returns:
        User: The user object.
    """
    try:
        secret = config.JWT_TOKEN
        payload = jwt.decode(token, secret, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise exception
        # Check if token is valid. Throws an exception if not.
        TokenData(id=user_id)
    except JWTError:
        raise exception
    user = get_by_id(db, user_id=user_id)
    if user is None:
        raise exception
    return user


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Get the currently authenticated user.

    Retrieve token from authentication header. Then, check if it is valid
    and get the corresponding user. If something goes wrong abort the request
    and send an appropriate exception to the client.

    Args:
        db (Session, optional): The DB session. Defaults to Depends(get_db).
        token (str, optional): The token from the auth header. Defaults to Depends(oauth2_scheme).

    Raises:
        CREDENTIALS_EXCEPTION: 401 exception.

    Returns:
        UserModel: The current user.
    """
    return get_user_from_jwt(db=db, token=token)


async def admin_guard(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Grant access if the current user is an admin.

    Args:
        db (Session, optional): The database session. Defaults to Depends(get_db).
        token (str, optional): The jwt bearer token. Defaults to Depends(oauth2_scheme).

    Raises:
        CREDENTIALS_EXCEPTION: User is not authenticated.
        ROLE_EXEPTION: If the user is not an admin

    Returns:
        User: The current user.
    """
    user = get_user_from_jwt(db, token)
    has_access = user_has_role(user=user, required_roles=[Roles.ADMIN.value])
    if not has_access:
        raise ROLE_EXEPTION
    return user


async def superuser_guard(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Grant access if the current user is a superuser.

    Args:
        db (Session, optional): The database session. Defaults to Depends(get_db).
        token (str, optional): The jwt bearer token. Defaults to Depends(oauth2_scheme).

    Raises:
        CREDENTIALS_EXCEPTION: User is not authenticated.
        ROLE_EXEPTION: If the user is not a superuser.

    Returns:
        User: The current user.
    """
    user = get_user_from_jwt(db, token)
    if not user.is_superuser:
        raise ROLE_EXEPTION
    return user
