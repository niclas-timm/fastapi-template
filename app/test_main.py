from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


class TestMain:
    def test_front(self):
        response = client.get("/")
        assert response.status_code == 200
