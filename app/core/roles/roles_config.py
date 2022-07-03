"""
Set the deufalt role a new user will receive whe signing up.
"""
from app.core.roles.roles import Roles

DEFAULT_ROLE = Roles.USER.value
