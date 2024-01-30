from fastapi.testclient import TestClient
import sys
from main.m_7_1_2 import app, Users


client = TestClient(app)

def test_create_user():
    response = client.post(
        '/create_user',
        json={
                "username": "ya",
                "age": "5",
                "email": "ya@aemail.com",
                "password": "32158746",
                "phone": "phone_number4"
            }
        )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Пользователь создан",
        **Users
    }
