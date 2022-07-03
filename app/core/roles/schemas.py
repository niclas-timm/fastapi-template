"""
Schema implementations for roles. Primarily used for API interactions.
"""

from typing import List
from pydantic import BaseModel


class AddRoles(BaseModel):
    """Schema for adding roles to a user."""
    roles: List[str]
