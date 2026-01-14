import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Helper for creating an item
def create_item(name="Stapler", quantity=10, price=5.0):
    return client.post("/api/items/", json={"name": name, "quantity": quantity, "price": price})

def test_create_item():
    response = create_item()
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Stapler"
    assert data["quantity"] == 10
    assert data["price"] == 5.0

def test_get_item():
    create_resp = create_item(name="Notebook", quantity=2, price=1.5)
    item_id = create_resp.json()["id"]
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Notebook"

def test_update_item():
    create_resp = create_item(name="Marker", quantity=3, price=2.5)
    item_id = create_resp.json()["id"]
    response = client.put(f"/api/items/{item_id}", json={"name": "Highlighter", "quantity": 5, "price": 3.0})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Highlighter"
    assert data["quantity"] == 5
    assert data["price"] == 3.0

def test_delete_item():
    create_resp = create_item(name="Tape", quantity=1, price=0.5)
    item_id = create_resp.json()["id"]
    response = client.delete(f"/api/items/{item_id}")
    assert response.status_code == 204
    # Confirm deletion
    get_resp = client.get(f"/api/items/{item_id}")
    assert get_resp.status_code == 404

def test_list_items():
    create_item(name="Paper", quantity=1, price=1.0)
    create_item(name="Envelope", quantity=2, price=2.0)
    response = client.get("/api/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(item["name"] == "Paper" for item in data)
    assert any(item["name"] == "Envelope" for item in data)

def test_invalid_create():
    response = client.post("/api/items/", json={"name": "", "quantity": -1, "price": -5.0})
    assert response.status_code == 422

def test_not_found():
    response = client.get("/api/items/99999")
    assert response.status_code == 404
    response = client.put("/api/items/99999", json={"name": "X"})
    assert response.status_code == 404
    response = client.delete("/api/items/99999")
    assert response.status_code == 404
