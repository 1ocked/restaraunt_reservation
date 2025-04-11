from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tables():
    response = client.get("/tables/")
    assert response.status_code == 200
