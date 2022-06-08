from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import db
from app.core.user import schema as user_schema
from app.core.user.services import crud, auth, verification
from app.core.user.model import UserModel
from app.core.security.deps import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security.models import TokenModel
from .services import password as password_service
from .services import mail as mail_service

router = APIRouter(
    tags=['users']
)


@router.post('/register', response_model=user_schema.UserResponse)
def register_user(*, database: Session = Depends(db.get_db), new_user: user_schema.UserCreate):
    """ Register new user

    Register new user by email and password.
    """
    existing_user = crud.get_by_email(db=database, email=new_user.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail='A user with the same email already exists.'
        )
    user = crud.create_user(db=database, new_user=new_user)
    return user


@router.post('/token', response_model=TokenModel)
async def login(*, database: Session = Depends(db.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    token = auth.user_login(db=database, email=form_data.username,
                            password=form_data.password)
    return {"access_token": token, "token_type": "bearer"}


@router.get('/me', response_model=user_schema.UserResponse)
def me(current_user: UserModel = Depends(get_current_user)):
    return current_user


@router.get('/email/verify/')
def verify_user_email(token: str, db: Session = Depends(db.get_db)):
    email = verification.verify_email_token(token)
    if not email:
        raise HTTPException(
            status_code=400,
            detail='Invalid token provided'
        )
    return verification.verify_email(email=email, db=db)


@router.get('/request-password-reset')
def request_password_reset(email: str, db: Session = Depends(db.get_db)):
    user = crud.get_by_email(db=db, email=email)
    # For security reasons we don't send error msg if the user does not exist.
    if not user:
        return True
    token = password_service.generate_password_reset_token(email)
    mail_service.send_reset_password_email(
        email_to=email, token=token)
    return True


@router.post('/reset-password')
def reset_password(data: user_schema.ResetPassword, db: Session = Depends(db.get_db)):
    email_from_token = password_service.verify_password_reset_token(data.token)
    if not email_from_token:
        raise HTTPException(
            status_code=400,
            detail='Invalid token'
        )
    if not email_from_token == data.email:
        raise HTTPException(
            status_code=400,
            detail='Invalid data'
        )
    return password_service.change_password(db=db, email=data.email, new_pass=data.new_password)
