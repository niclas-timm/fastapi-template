# -------------------------------------------------------------------------------
# Register all partial routers from your modules here.
# To do so, import the router object from your router file and add it to the
# partial_routers list. It will then be automatically registered as a router
# for your application.
# -------------------------------------------------------------------------------
from fastapi import APIRouter
from typing import List

from app.core.user.router import router as user_router

partial_routers: List[APIRouter] = [
    user_router
]

router = APIRouter()
for partial_router in partial_routers:
    router.include_router(partial_router)
