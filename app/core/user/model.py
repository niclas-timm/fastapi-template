from sqlalchemy import Boolean, Column, Integer, String

from app.core.db.db import Base
from app.core.roles.roles_config import default_role


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    roles = Column(String, default=default_role)

    class Config:
        orm_mode = True
