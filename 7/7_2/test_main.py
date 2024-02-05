import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app, fetch_data_from_api, process_data

client = TestClient(app)

class TestApp(unittest.TestCase):

    @patch('main.fetch_data_from_api')
    @patch('main.process_data')
    def test_get_and_process_data(self, mock_process_data,
                                  mock_fetch_data):
        
        # Mock функции fetch_data_from_api для возврата "sample response"
        mock_response = {"key": "value"}
        mock_fetch_data.return_value = mock_response

        # # Mock функции process_data
        mock_processed_data = {"KEYss": "VALUE"}
        mock_process_data.return_value = mock_processed_data

        # Вызов тестируемой функции
        response = client.get('/data/')

        # Assertions
        mock_fetch_data.assert_called_once() # Проверка, что fetch_data_from_api был вызван
        mock_process_data.assert_called_once_with(mock_response) # Проверка, что process_data была вызрана с "mocked response"
        self.assertEqual(response.status_code, 200) # Проверка, что status_code равен 200
        print(response.json())
        self.assertEqual(response.json(), mock_processed_data) # Проверка, что функция вернула ожидаемые обработанные данные
    
if __name__ == '__main__':
    unittest.main()