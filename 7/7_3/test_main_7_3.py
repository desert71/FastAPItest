from fastapi.testclient import TestClient
from main_7_3 import app

client = TestClient(app)

# def test_read_item():

#     response = client.get('/items/1')

#     # Assertions
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1}

#     response = client.get('/items/z')

#     # Assertions
#     assert response.status_code == 200
#     assert response.json() == {"item_id": "z"}

def test_login_and_access_data():
    login_data = {
    "username": "user123",
    "password": "secretpassword"
    }
    response = client.post('/login/', json=login_data)
    assert response.status_code == 200
    assert "set-cookie" in response.headers

    cookies = response.cookies
    cookie_value = cookies["session_cookie"]

    headers = {
        "Cookie": f"session_cookie= {cookie_value}"
    }
    response = client.get('protected_data/', headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "username" in data
    assert "email" in data