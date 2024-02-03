from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_user():
    response = client.post("/users", json={"username": "testuser", "email": "testuser@example.com", "number_of_tasks": 5})
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "testuser@example.com", "number_of_tasks": 5}

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "testuser@example.com", "number_of_tasks": 5}

def test_update_user():
    response = client.put("/users/1", json={"username": "updateduser", "email": "updateduser@example.com", "number_of_tasks": 10})
    assert response.status_code == 200
    assert response.json() == {"username": "updateduser", "email": "updateduser@example.com", "number_of_tasks": 10}

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}
