# -------------------------------------------------------------------------------
# Set the deufalt role a new user will receive whe signing up.
# -------------------------------------------------------------------------------
from app.core.roles.roles import Roles

default_role = Roles.USER.value
