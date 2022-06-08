from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.core.config import get_environment_var
from app.security.models import TokenData
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.user.services.crud import get_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Get the currently authenticated user.

    Retrieve token from authentication header. Then, check if it is valid
    and get the corresponding user. If something goes wrong abort the request
    and send an appropriate exception to the client.

    Args:
        db (Session, optional): The DB session. Defaults to Depends(get_db).
        token (str, optional): The token from the auth header. Defaults to Depends(oauth2_scheme).

    Raises:
        credentials_exception: 401 exception.

    Returns:
        _type_: _description_
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        secret = get_environment_var('JWT_TOKEN')
        payload = jwt.decode(token, secret, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
    user = get_by_id(db, user_id=user_id)
    if user is None:
        raise credentials_exception
    return user
