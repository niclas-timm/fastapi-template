from ctypes import Union
from fastapi import HTTPException
from typing import Union

from app.core.user import schema
from app.core.user.model import UserModel
from app.core.user.services import password
from app.core.security.services import create_password_hash


def create_user_object(new_user: schema.UserCreate) -> Union[UserModel, str]:
    is_password_valid = password.password_requirements_check(new_user.password)
    if is_password_valid["error"]:
        return "Invalid password"
    db_obj = UserModel(
        email=new_user.email,
        password=create_password_hash(
            new_user.password),
        name=new_user.name,
    )
    if not db_obj:
        return "User could not be created"
    return db_obj
