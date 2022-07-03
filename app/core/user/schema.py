"""
Schemas related to the user package.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: int
    email_verified: bool = False
    is_active: bool = True
    roles: str
    is_superuser: bool

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class UserCredentials(BaseModel):
    email: EmailStr
    password: str


class ResetPassword(BaseModel):
    email: str
    new_password: str
    token: str


class UpdateRoles(BaseModel):
    roles: str
