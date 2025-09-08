import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_add_and_get_items(client):
    # Start with empty list
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json == []

    # Add an item
    response = client.post("/items", json={"name": "Apple"})
    assert response.status_code == 201
    assert response.json["message"] == "Item added"

    # Get items again
    response = client.get("/items")
    assert response.status_code == 200
    assert "Apple" in response.json

    # Add another item
    response = client.post("/items", json={"name": "Banana"})
    assert response.status_code == 201

    # Get items again
    response = client.get("/items")
    assert response.status_code == 200
    assert "Apple" in response.json
    assert "Banana" in response.json
