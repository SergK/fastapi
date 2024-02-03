import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

@pytest.mark.parametrize("user_id, expected_status", [("alice", 200), ("unknown", 404)])
def test_get_user(user_id, expected_status):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == expected_status


def test_create_user():
    user_data = {"username": "alice", "email": "alice@example.com", "tasks": 5}
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data


def test_update_user():
    user_data = {"username": "alice", "email": "alice@example.com", "tasks": 10}
    response = client.put("/users/alice", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data


def test_delete_user():
    response = client.delete("/users/alice")
    assert response.status_code == 200
    assert response.json() == {"detail": "User deleted"}