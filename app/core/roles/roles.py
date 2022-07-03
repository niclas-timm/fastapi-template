"""
Enum of availale roles accross the application.
The ADMIN role has access to everything and should NEVER be changed or deleted.
"""
from enum import Enum


class Roles(Enum):
    """Enum to define the roles a user can have."""
    ADMIN = 'ADMIN'
    USER = 'USER'
