from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import db
from app.user import schema as user_schema
from app.user.services import get_by_email, create_user, user_login
from app.user.model import UserModel
from app.security.deps import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.security.models import TokenModel


router = APIRouter(
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


@router.post('/token', response_model=TokenModel)
async def login(*, database: Session = Depends(db.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    token = user_login(db=database, email=form_data.username,
                       password=form_data.password)
    return {"access_token": token, "token_type": "bearer"}


@router.get('/me', response_model=user_schema.UserResponse)
def me(current_user: UserModel = Depends(get_current_user)):
    return current_user
