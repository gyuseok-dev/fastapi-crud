from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/create",
        json={"name": "Bob", "content": "new content"},
    )
    assert response.status_code == 200
    assert isinstance(response.json()["id"], int)
    assert response.json()["name"] == "Bob"
    assert response.json()["content"] == "new content"
    
def test_read_item():
    response = client.get("/read/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "John"
    assert response.json()["content"] == "This is a test code."

def test_update_item():
    response = client.put(
        "/update/1",
        json={"name": "Alice", "content": "modify"},
    )
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Alice"
    assert response.json()["content"] == "modify"

def test_delete_item():
    response = client.delete("/delete/1")
    assert response.status_code == 200
    response = client.delete("/delete/1")
    assert response.status_code == 404