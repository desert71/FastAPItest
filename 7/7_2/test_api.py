import unittest
from unittest.mock import patch, MagicMock
from app import get_and_process_data

class TestApp(unittest.TestCase):

    @patch('app.fetch_data_from_api')
    @patch('app.process_data')
    def test_get_and_process_data(self, mock_process_data: MagicMock,
                                  mock_fetch_data: MagicMock):
        
        # Mock функции fetch_data_from_api для возврата "sample response"
        mock_response = {"key": "value"}
        mock_fetch_data.return_value = mock_response

        # Mock функции process_data
        mock_processed_data = {"KEY": "VALUE"}
        mock_process_data.return_value = mock_processed_data

        # Вызов тестируемой функции
        result = get_and_process_data()

        # Assertions
        mock_fetch_data.assert_called_once() # Проверка, что fetch_data_from_api был вызван
        mock_process_data.assert_called_once_with(mock_response) # Проверка, что process_data была вызрана с "mocked response"
        self.assertEqual(result, mock_processed_data) # Проверка, что функция вернула ожидаемые обработанные данные
    
if __name__ == '__main__':
    unittest.main()