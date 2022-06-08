from sqlalchemy.orm import Session
from typing import Optional
from app.user.services import crud
from fastapi import HTTPException
from app.security.services import create_access_token, verify_password


def user_login(db: Session, email: str, password: str) -> Optional[str]:
    """ Log user in.

    Log user in by email and password.
    """
    user = crud.get_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Wrong email or password")
    is_password_valid = verify_password(password, user.password)
    if not is_password_valid:
        raise HTTPException(status_code=400, detail="Wrong email or password")
    return create_access_token(str(user.id))
