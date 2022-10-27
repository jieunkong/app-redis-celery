from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_get_user_info():
    resp = client.get('/api/v1/users/1')
    print(resp.text)
    assert resp.status_code == 200
