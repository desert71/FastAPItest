from fastapi.testclient import TestClient
from main_7_3 import app

client = TestClient(app)

def test_read_item():

    response = client.get('/items/1')

    # Assertions
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

    response = client.get('/items/z')

    # Assertions
    assert response.status_code == 200
    assert response.json() == {"item_id": "z"}