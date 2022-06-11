# -------------------------------------------------------------------------------
# Utility function for working with roles.
# -------------------------------------------------------------------------------

from typing import List, Union
from .roles import Roles


def are_roles_valid(roles: Union[List[str], str]):
    """Check if given roles are actually valid roles used accross the app.

    Args:
        roles (Union[List[str], str]): List of roles or a string with the role separated by comma.

    Returns:
        bool: True if all given roles are valid.
    """
    roles_to_be_checked = roles if isinstance(
        roles, list) else list(roles.split(","))
    available_roles = set(role.value for role in Roles)
    validity = True
    for r in roles_to_be_checked:
        if r not in available_roles:
            validity = False
            break
    return validity
