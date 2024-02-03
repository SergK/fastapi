import pytest
from fastapi.testclient import TestClient
from app.main import app

class TestCRUDEndpoints:
    client = TestClient(app)

    def test_create_user(self):
        response = self.client.post("/users", json={"username": "testuser", "email": "test@example.com", "number_of_tasks": 5})
        assert response.status_code == 200
        assert response.json() == {"username": "testuser", "email": "test@example.com", "number_of_tasks": 5}

    def test_read_user(self):
        # Assuming a user with ID 'testuser' exists
        response = self.client.get("/users/testuser")
        assert response.status_code == 200
        assert response.json()["username"] == "testuser"

    def test_update_user(self):
        # Assuming a user with ID 'testuser' exists
        response = self.client.put("/users/testuser", json={"username": "testuser", "email": "newtest@example.com", "number_of_tasks": 10})
        assert response.status_code == 200
        assert response.json()["email"] == "newtest@example.com"

    def test_delete_user(self):
        # Assuming a user with ID 'testuser' exists
        response = self.client.delete("/users/testuser")
        assert response.status_code == 200
        assert response.json() == {"detail": "User deleted"}
