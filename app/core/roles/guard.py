# -------------------------------------------------------------------------------
# Set of guards that can be used as dependencies in order to allow access
# based on the role of the current user.
# -------------------------------------------------------------------------------
from typing import List

from app.core.user.model import UserModel
from .roles import Roles


def has_role(user: UserModel, required_roles: List[str]) -> bool:
    """Check if a user has at least on of the specified roles.

    Check if the user user has at least one of the roles that
    are given as an argument to the method. If the user has the
    admin role, the method will always return true.

    Args:
        user (UserModel): The user.
        required_roles (List[str]): The roles that will be checked against the roles of the user.

    Returns:
        bool: True if the user has at least one of the roles or is an admin.
    """
    if Roles.ADMIN.value in user.roles:
        return True
    user_has_role = False
    for required_role in required_roles:
        if required_role in user.roles:
            user_has_role = True
            break
    return user_has_role
