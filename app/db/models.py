"""
Import all models the app uses. Those will be imported into the
database in the main.py file.
"""
from app.db.db import Base
from app.user.model import UserModel
