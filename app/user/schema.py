from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: EmailStr = None
    is_active: bool = True
    is_admin: bool = False
    name: str = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    id: int = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class UserResponse(UserBase):
    id: int
    email: EmailStr
    name: str

    class Config:
        orm_mode = True
