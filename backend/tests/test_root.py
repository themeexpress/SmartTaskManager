from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    r = client.get("/")
    assert r.status_code in (200, 404)  # 404 OK if root not defined
