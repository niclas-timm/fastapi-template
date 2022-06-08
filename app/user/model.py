from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.db.db import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)

    class Config:
        orm_mode = True
