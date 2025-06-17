import unittest
from unittest.mock import patch, mock_open
from your_module import load_transactions  # замените your_module на имя вашего модуля


class TestLoadTransactions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    @patch('json.load')
    def test_load_transactions_success(self, mock_json_load, mock_file):
        """Тест успешной загрузки транзакций из файла"""
        # Настраиваем mock для json.load
        mock_json_load.return_value = [{"id": 1, "amount": 100}]

        # Вызываем тестируемую функцию
        result = load_transactions('test_path.json')

        # Проверяем результаты
        self.assertEqual(result, [{"id": 1, "amount": 100}])
        mock_file.assert_called_once_with('test_path.json', 'r')
        mock_json_load.assert_called_once()

    @patch('builtins.open', new_callable=mock_open, read_data='{"id": 1, "amount": 100}')
    @patch('json.load')
    def test_load_transactions_not_list(self, mock_json_load, mock_file):
        """Тест случая, когда JSON не является списком"""
        # Настраиваем mock для json.load (возвращаем dict вместо list)
        mock_json_load.return_value = {"id": 1, "amount": 100}

        # Вызываем тестируемую функцию
        result = load_transactions('test_path.json')

        # Проверяем что вернулся пустой список
        self.assertEqual(result, [])

    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_load_transactions_file_not_found(self, mock_file):
        """Тест случая, когда файл не найден"""
        # Вызываем тестируемую функцию
        result = load_transactions('nonexistent_path.json')

        # Проверяем что вернулся пустой список
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    @patch('json.load', side_effect=json.JSONDecodeError('msg', 'doc', 0))
    def test_load_transactions_invalid_json(self, mock_json_load, mock_file):
        """Тест случая с невалидным JSON"""
        # Вызываем тестируемую функцию
        result = load_transactions('invalid.json')

        # Проверяем что вернулся пустой список
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()