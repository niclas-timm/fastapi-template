from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.core.db import db

client = TestClient(app)


class TestDB:
    """Database test class."""

    def test_db_connection(self):
        """Test database connection."""
        session = db.SessionLocal()
        assert isinstance(session, Session)
        session.close()
