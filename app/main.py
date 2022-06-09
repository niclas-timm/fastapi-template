from fastapi import FastAPI
from app.core.db.db import engine
from app import models
from app.routers import router
from app.core.security import cors
from app.core.cache import setup
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

# logging.config.fileConfig('logger.conf', disable_existing_loggers=False)
# logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

cors.add_cors(app)
app.include_router(router)


@app.get('/')
@cache(expire=1000)
async def front():
    # logger.info("logging from the root logger")
    return {"Hello": "World"}


@app.on_event('startup')
async def startup():
    """Enable response caching upon startup."""
    r = setup.get_redis_instance()
    FastAPICache.init(RedisBackend(r), prefix="response-cache")
