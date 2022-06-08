from typing import Literal, Optional
from app.core.crud_base import CRUDBase
from app.user.model import UserModel
from app.user.schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.security.services import create_access_token, verify_password, create_password_hash
from app.user.services import mail as user_mail_service


def get_by_id(db: Session, user_id: str) -> Optional[UserModel]:
    """Get user by id.

    Args:
        db (Session): The database session.
        user_id (str): The user id.

    Returns:
        Optional[UserModel]: The user.
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_by_email(db: Session, email: str) -> Optional[UserModel]:
    """Get user by email.

    Args:
        db (Session): The database session.
        email (str): The user email.

    Returns:
        Optional[UserModel]: The user object.
    """
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
    user_mail_service.send_new_account_email(db_obj.email)
    return db_obj
