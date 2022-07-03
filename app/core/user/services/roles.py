"""
Methdods related to roles of users.
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.roles.utils import are_roles_valid
from typing import List
from app.core.user.services.crud import get_by_id


def add_roles_to_user(db: Session, user_id: str, new_roles: List[str]):
    """Add new roles to a user.

    Args:
        db (Session): The db session.
        user_id (str): The id of the user the roles will be added to.
        new_roles (List[str]): The list of roles that will be added to the user.

    Raises:
        HTTPException: User not found or invalid list of roles.

    Returns:
        UserModel: The updated user object.
    """
    user = get_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='User not found'
        )
    current_roles = user.roles
    if not are_roles_valid(new_roles):
        raise HTTPException(
            status_code=400,
            detail="The role you are trying to add is not valid."
        )
    final_roles = current_roles
    for new_role in new_roles:
        if new_role in current_roles:
            return user
        final_roles = f"{final_roles},{new_role}"
    user.roles = final_roles
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
