# -------------------------------------------------------------------------------
# Methods for managing the connection to the redis cache.
# -------------------------------------------------------------------------------
import aioredis

from app.core import config


def create_redis_connection():
    """Create connection to redis instance.

    Returns:
        Redis: The redis connection.
    """
    host = config.REDIS_HOST
    port = config.REDIS_PORT
    username = config.REDIS_USERNAME
    password = config.REDIS_PASSWORD
    redis_url = f"redis://{host}:{port}"
    return aioredis.from_url(
        url=redis_url,
        username=username,
        password=password
    )
