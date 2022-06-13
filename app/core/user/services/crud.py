from fastapi import HTTPException
from typing import List, Optional

from pendulum import instance
from app.core.user.model import UserModel
from app.core.user.schema import UserCreate
from sqlalchemy.orm import Session
from app.core.security.services import create_password_hash
from app.core.user.services import mail as user_mail_service
from app.core.user.services import password
from sqlalchemy import exc
from app.core import config
from app.core.user.services import utils as user_utils


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
    db_obj = user_utils.create_user_object(new_user=new_user)
    if not isinstance(db_obj, UserModel):
        raise HTTPException(
            status_code=400,
            detail=db_obj
        )
    db.add(db_obj)
    try:
        db.commit()
        db.refresh(db_obj)
    except exc.SQLAlchemyError:
        raise HTTPException(
            status_code=401,
            detail='Email address already taken'
        )
    if config.EMAILS_ENABLED:
        user_mail_service.send_new_account_email(db_obj.email)
    return db_obj


def delete_user(db: Session, user_id: str):
    """Delete user form database.

    Args:
        db (Session): The database session.
        user_id (str): The id of the user.

    Raises:
        HTTPException: User not found.

    Returns:
        bool: True if user was deleted successfully.
    """
    user = get_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )
    db.delete(user)
    db.commit()
    return True


def create_superuser(db: Session, new_user: UserCreate):
    db_obj = user_utils.create_user_object(new_user=new_user)
    if not isinstance(db_obj, UserModel):
        raise HTTPException(
            status_code=400,
            detail=db_obj
        )
    db_obj.__setattr__('is_superuser', True)
    db.add(db_obj)
    try:
        db.commit()
        db.refresh(db_obj)
    except exc.SQLAlchemyError:
        raise HTTPException(
            status_code=401,
            detail='Email address already taken'
        )
    if config.EMAILS_ENABLED:
        user_mail_service.send_new_account_email(db_obj.email)
    return db_obj
