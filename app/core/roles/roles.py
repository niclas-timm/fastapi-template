# -------------------------------------------------------------------------------
# Enum of availale roles accross the application.
# The ADMIN role has access to everything and should NEVER be changed or deleted.
# -------------------------------------------------------------------------------

from enum import Enum


class Roles(Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'
