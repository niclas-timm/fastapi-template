from fastapi import HTTPException
from typing import List, Optional
from app.core.user.model import UserModel
from app.core.user.schema import UserCreate
from sqlalchemy.orm import Session
from app.core.security.services import create_password_hash
from app.core.user.services import mail as user_mail_service
from app.core.user.services import password


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
    is_password_valid = password.password_requirements_check(new_user.password)
    if is_password_valid["error"]:
        return {"error": True, "msg": is_password_valid["msg"]}
    db_obj = UserModel(
        email=new_user.email,
        password=create_password_hash(
            new_user.password),
        name=new_user.name,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    user_mail_service.send_new_account_email(db_obj.email)
    return db_obj


def add_role(db: Session, user_id: str, new_roles: List[str]):
    user = get_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )
