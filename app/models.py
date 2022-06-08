"""
Import all models the app uses. Those will be imported into the
database in the main.py file.
"""
from app.core.db.db import Base  # noqa
from app.core.user.model import UserModel  # noqa
