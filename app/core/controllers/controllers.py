"""
Creating a FastAPI APIRouter with all controllers registered in config.yml
as sub routers.
"""
from app.core.controllers.controller_discoverer import register_all_controllers

router = register_all_controllers()
