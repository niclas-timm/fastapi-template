"""
User authentication service.
"""
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.core.user.services import crud
from app.core.security.services import create_jwt_access_token, verify_password


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
    return create_jwt_access_token(str(user.id))
