from fastapi.testclient import TestClient

from app.main import app
from app.core.cache import setup
from app.core.cache import cache_utils
import pytest

client = TestClient(app)

TEST_CACHE_KEY = 'test'
TEST_CACHE_VALUE = 'Some test value'


@pytest.mark.asyncio
class TestCache:
    async def test_set_cache_item(self):
        r = setup.get_redis_instance()
        await cache_utils.set_cache_key(r=r, key=TEST_CACHE_KEY, value=TEST_CACHE_VALUE)
        assert await cache_utils.get_cache_key(r, TEST_CACHE_KEY) == TEST_CACHE_VALUE

    async def test_remove_test_key(self):
        r = setup.get_redis_instance()
        await cache_utils.remove_cache_key(r, TEST_CACHE_KEY)
        await r.close()
