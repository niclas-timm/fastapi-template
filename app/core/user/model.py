"""
Models related to the user package.
"""

from sqlalchemy import Boolean, Column, Integer, String

from app.core.db.db import Base
from app.core.roles.roles_config import DEFAULT_ROLE


class UserModel(Base):
    """The user mode class."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    roles = Column(String, default=DEFAULT_ROLE)

    class Config:
        """Config class for the user model."""
        orm_mode = True
