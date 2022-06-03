"""
Import all models the app uses. Those will be imported into the
database in the main.py file.
"""
from db.db import Base
from user.model import UserModel
