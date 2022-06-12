# -------------------------------------------------------------------------------
# Configure pytest by adding fixtures. For example, the db() method will return
# a database instance that can be reused across all tests. For more information
# visit https://docs.pytest.org/en/6.2.x/fixture.html
# -------------------------------------------------------------------------------
import pytest
from fastapi.testclient import TestClient
from typing import Generator

from app.main import app
from app.core.db.db import SessionLocal
from app.core.cache.setup import get_redis_instance


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="session")
def cache() -> Generator:
    yield get_redis_instance()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
