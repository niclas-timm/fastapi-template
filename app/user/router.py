from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import db
from app.user import schema as user_schema
from app.user.model import UserModel
from app.user.services import get_by_email, create_user

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/register', response_model=user_schema.UserResponse)
def register_user(*, db: Session = Depends(db.get_db), new_user: user_schema.UserCreate):
    existing_user = get_by_email(db=db, email=new_user.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail='A user with the same email already exists.'
        )
    user = create_user(db=db, new_user=new_user)
    return user


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
