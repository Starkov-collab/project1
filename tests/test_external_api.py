import os
import unittest
from unittest.mock import patch, Mock
import json

from requests.cookies import MockRequest
from urllib3 import request

from src.external_api import get_currency_usd_or_euro

def setUp(self) :
    """
    Настройка тестовых данных
    setUp - создает тестовые данные для разных транзакций
    self - это ссылка на экземпляр
    """
    self.usd_transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "USD"
            }
        }
    }

    self.eur_transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {
                "code": "EUR"
            }
        }
    }
    self.rub_transaction = {
        "operationAmount": {
            "amount": "5000.0",
            "currency": {
                "code": "RUB"
            }
        }
    }

@patch('requests.get')
@patch.dict('os.environ', {'API_KEY': 'mock_key'})
def test_eur_transaction_success(self, mock_get) :
    """корректно формирует запрос к API для конвертации EUR → RUB."""
    mock_response = Mock()
    """Создание mock-объекта для имитации HTTP-ответа от API"""
    mock_response.status_code = 200
    """Установка статус-кода ответа (200 = успешный запрос)"""
    mock_response.json.return_value = {"result" : 5000.0} # Предположим курс 1 EUR = 100 RU

    mock_get.return_value = mock_response
    result = get_currency_usd_or_euro(self.eur_transaction)

    self.assertEqual(result, 5000.0)
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=50.0",
        headers={"apikey": "test_key"}
    )

@patch('request.get')
@patch.dict('os.environ', {'API_KEY': 'mock_key'})  # Мокируем переменные окружения
def test_usd_conversion_success(self, mock_get):
    """Тест успешного конвертирования USD в RUB."""
    # Настраиваем мок-ответ API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}  # Предположим курс 1 USD = 75 RUB
    mock_get.return_value = mock_response
    """Эта строка настраивает поведение мок-объекта mock_get 
    (который заменяет реальный HTTP-клиент, например requests.get),
     чтобы при его вызове он возвращал заранее подготовленный мок-ответ (mock_response)"""

    # Вызываем тестируемую функцию
    result = get_currency_usd_or_euro(self.usd_transaction)

    # Проверяем результаты
    self.assertEqual(result, 7500.0)
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0",
        headers={"apikey": "test_key"}
    )

@patch('request.get')
@patch.dict('os.environ', {'API_KEY': 'mock_key'})
def test_non_usd_eur_transaction(self, mock_get) :
    """Тест что для не-USD/EUR валют возвращается исходная сумма."""
    result = get_currency_usd_or_euro(self.rub_transaction)

    self.assertEqual(result, "5000.0")
    mock_get.assert_not_called()  # Убеждаемся, что запрос не делался

@patch('request.get')
@patch.dict('os.environ', {'API_KEY': 'mock_key'})
def test_api_error_responce(self, mock_get) :
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "Server Error"
    mock_get.return_value = mock_response

    result = get_currency_usd_or_euro(self.ust_transaction)

    self.assertEqual(result, 0.0)
    mock_get.assert_called_once()

@patch('request.get')
@patch.dict('os.environ', {'API_KEY': 'mock_key'})
def test_api_invalid_json_response(self, mock_get):
    """Тест обработки невалидного JSON ответа."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")

    result = get_currency_usd_or_euro(self.ust_transaction)

    self.assertEqual(result, 0.0)



