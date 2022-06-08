import asyncio
import aioredis

from app.core import config


async def redis_connection():
    """Create connection to redis instance.

    Returns:
        Redis: The redis connection.
    """
    host = config.REDIS_HOST
    port = config.REDIS_PORT
    username = config.REDIS_USERNAME
    password = config.REDIS_PASSWORD
    redis_url = f"redis://{host}:{port}"
    try:
        redis = aioredis.from_url(
            url=redis_url,
            username=username,
            password=password
        )
        yield redis
    finally:
        await redis.close()
