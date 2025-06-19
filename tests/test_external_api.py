import os
import pytest
from unittest.mock import patch, Mock
from src.external_api import get_currency_usd_or_euro


class TestCurrencyConversion:
    """Тесты для функции get_currency_usd_or_euro()"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Подготовка тестовых данных"""
        self.usd_transaction = {
            "operationAmount": {
                "amount": "100.0",
                "currency": {"code": "USD"}
            }
        }
        self.eur_transaction = {
            "operationAmount": {
                "amount": "50.0",
                "currency": {"code": "EUR"}
            }
        }
        self.rub_transaction = {
            "operationAmount": {
                "amount": "5000.0",
                "currency": {"code": "RUB"}
            }
        }

    @patch('requests.get')
    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_eur_transaction_success(self, mock_get):
        """Тест успешной конвертации EUR в RUB"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 5000.0}
        mock_get.return_value = mock_response

        result = get_currency_usd_or_euro(self.eur_transaction)
        assert result == 5000.0
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=50.0",
            headers={"apikey": "test_key"}
        )

    @patch('requests.get')
    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_usd_conversion_success(self, mock_get):
        """Тест успешной конвертации USD в RUB"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 7500.0}
        mock_get.return_value = mock_response

        result = get_currency_usd_or_euro(self.usd_transaction)
        assert result == 7500.0
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0",
            headers={"apikey": "test_key"}
        )

    @patch('requests.get')
    def test_non_usd_eur_transaction(self, mock_get):
        """Тест пропуска конвертации для RUB"""
        result = get_currency_usd_or_euro(self.rub_transaction)
        assert result == '5000.0'
        mock_get.assert_not_called()

    @patch('requests.get')
    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_api_error_response(self, mock_get):
        """Тест обработки ошибки API"""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Server Error"
        mock_get.return_value = mock_response

        result = get_currency_usd_or_euro(self.usd_transaction)
        assert result == 0.0
        mock_get.assert_called_once()

    @patch('requests.get')
    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_api_invalid_json_response(self, mock_get):
        """Тест обработки невалидного JSON ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")

        result = get_currency_usd_or_euro(self.usd_transaction)
        assert result == 0.0