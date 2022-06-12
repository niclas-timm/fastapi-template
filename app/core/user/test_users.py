from sqlalchemy.orm import Session

from app.core.user.services import crud


def test_get_user(db: Session):
    user = crud.get_by_id(db, "1")
    if not user:
        assert False
    assert user.password
