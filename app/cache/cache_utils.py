""" Utility methods to interact with the redis cache.

Methods like getting and settings values in the redis cache.

"""

from redis import Redis

# Default expiration 4 hours.
DEFAULT_EXPIRATION_IN_HOURS: int = 60 * 60 * 4


async def get_cache_key(r: Redis, key: str):
    """Get value for a given cache key

    Args:
        r (Redis): The redis client.
        key (str): The key for which the value will be retrieved from redis.

    Returns:
        (Any | None): The value for the cache key.
    """
    value = await r.get(key)
    if value is None:
        return None
    return value.decode("utf-8")


async def set_cache_key(r: Redis, key: str, value: str, timeout: int = DEFAULT_EXPIRATION_IN_HOURS) -> None:
    """Set new cache key in Redis.

    Add new cache key to redis.
    By default, the key will be stored for 4 hours.

    Args:
        r (Redis): The redis instance.
        key (str): The key that will be created.
        value (str): The value for the key that will be stored.
        timeout (int, optional): Time in seconds for how long the cache key will be valid
        . Defaults to 4 hours.
    """
    await r.set(key, value)
    await r.expire(key, timeout)
