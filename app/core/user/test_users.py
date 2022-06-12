from pydantic import EmailStr
from sqlalchemy.orm import Session
import json

from app.core.user.services import crud
from app.core.user import schema as user_schemas
from app.core.user.services import crud
from fastapi.testclient import TestClient

TEST_USER_EMAIL = EmailStr("testuser@email.com")


def test_get_user(db: Session):
    user = crud.get_by_id(db, "1")
    if not user:
        assert False
    assert user.password


def test_create_user(db: Session, client: TestClient):
    test_password = "oweihfoiweh!"
    request_data = {
        "email": TEST_USER_EMAIL,
        "name": "TEST USER",
        "password": test_password
    }
    response = client.post("/register", json=request_data)
    assert response.status_code == 200
    new_user_id = response.json()["id"]
    assert crud.delete_user(db, new_user_id)


def test_error_upon_taken_email_signup(db: Session, client: TestClient):
    """Test if a taken email can't be registered a second time.

    Get the first user in the databse and try to sign up with
    his/her email. If the request throws an error, everything
    is fine.
    Args:
        db (Session): The database session.
        client (_type_): FastAPI test client.
    """
    fake_password = "woehfowehgoh!!"
    fake_name = "Fake name"
    user = crud.get_by_id(db, "1")
    assert hasattr(user, 'email')
    request_data = {
        "email": user.email,
        "name": fake_name,
        "password": fake_password
    }
    response = client.post(
        "/register", json=request_data)
    assert response.status_code == 400
    assert response.json() == {
        'detail': 'A user with the same email already exists.'}
