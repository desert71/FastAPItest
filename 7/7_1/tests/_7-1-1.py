from fastapi.testclient import TestClient
import sys
from main.m_7_1_1 import app


client = TestClient(app)

def test_calculate_sum():
    response = client.get('/sum/?a=5&b=10')
    assert response.status_code == 200
    assert response.json() == {"result": 15}