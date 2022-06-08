from fastapi import APIRouter

from app.core.user.router import router as user_router

router = APIRouter()
router.include_router(user_router)
