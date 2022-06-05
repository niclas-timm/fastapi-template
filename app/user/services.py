from typing import Optional
from app.core.crud_base import CRUDBase
from app.user.model import UserModel
from app.user.schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.security.services import create_access_token, verify_password, create_password_hash


def get_by_id(db: Session, user_id: str) -> Optional[UserModel]:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_by_email(db: Session, email: str) -> Optional[UserModel]:
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_user(db: Session, new_user: UserCreate):
    """ Create user

    Store a new user in the database

    args:
    db (Session): The database session.
    new_user (UserCreate): The data necessary to create a new user.

    return (UserModel): The newly stored user.
    """
    db_obj = UserModel(
        email=new_user.email,
        password=create_password_hash(
            new_user.password),
        name=new_user.name,
        is_admin=new_user.is_admin,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def user_login(db: Session, email: str, password: str) -> Optional[str]:
    """ Log user in.

    Log user in by email and password.
    """
    user = get_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Wrong email or password")
    is_password_valid = verify_password(password, user.password)
    if not is_password_valid:
        raise HTTPException(status_code=400, detail="Wrong email or password")
    return create_access_token(str(user.id))
