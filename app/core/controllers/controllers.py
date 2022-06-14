# -------------------------------------------------------------------------------
# Creating a FastAPI APIRouter with all controllers registered in config.yml
# as sub routers.
# -------------------------------------------------------------------------------
from app.core.controllers.controller_discoverer import get_partial_routers

router = get_partial_routers()
