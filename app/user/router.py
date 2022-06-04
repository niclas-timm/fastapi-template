from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import db
from app.user import schema as user_schema
from app.user.services import get_by_email, create_user, user_login

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/register', response_model=user_schema.UserResponse)
def register_user(*, database: Session = Depends(db.get_db), new_user: user_schema.UserCreate):
    """ Register new user

    Register new user by email and password.
    """
    existing_user = get_by_email(db=database, email=new_user.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail='A user with the same email already exists.'
        )
    user = create_user(db=database, new_user=new_user)
    return user


@router.post('/login')
def login(*, database: Session = Depends(db.get_db), credentials: user_schema.UserCredentials):
    return user_login(db=database, email=credentials.email, password=credentials.password)