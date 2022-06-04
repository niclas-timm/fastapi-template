from typing import Optional
from app.core.crud_base import CRUDBase
from app.user.model import UserModel
from app.user.schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from app.security.services import SecurityService


# class UserService(CRUDBase[UserModel, UserCreate, UserUpdate]):
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
        password=SecurityService.create_password_hash(
            new_user.password),
        name=new_user.name,
        is_admin=new_user.is_admin,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
