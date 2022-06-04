from fastapi import APIRouter

from app.user.router import router as user_router

router = APIRouter()
router.include_router(user_router)
