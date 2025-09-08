import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Automated Testing Framework Demo!" in response.data

def test_get_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.data.strip() == b"[]"
