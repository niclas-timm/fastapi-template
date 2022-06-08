from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: EmailStr = None
    is_active: bool = True
    is_admin: bool = False
    name: str = None
    email_verified: bool = False


class UserCreate(UserBase):
    email: EmailStr
    password: str


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


class UserCredentials(BaseModel):
    email: EmailStr
    password: str
