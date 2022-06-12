from sqlalchemy.orm import Session
from app.core.user.services.crud import get_by_id
from app.core.roles import guard, roles


def test_admin_role(db: Session):
    """Check if user with ID 1 is an admin.

    This will not only validate if the RBAC is working. It will also
    check that user 1 is actually an admin and thus correctly has access
    to eveythin.

    Args:
        db (Session): The database session.
    """
    admin_user = get_by_id(db, "1")
    if not admin_user:
        assert False
    assert guard.has_role(admin_user, [roles.Roles.ADMIN.value])
