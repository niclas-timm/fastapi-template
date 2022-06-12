# -------------------------------------------------------------------------------
# Import all models the app uses. Those will be imported into the
# database in the main.py file. Make sure to add "#noqa" at the end in order
# to prevent automatic code formatters (like flake8) to remove the imports.
# -------------------------------------------------------------------------------
from app.core.db.db import Base  # noqa
from app.core.user.model import UserModel  # noqa
