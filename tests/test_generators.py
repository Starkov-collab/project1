import pytest
from typing import Dict, List
from generators import filter_by_currency,card_number_generator,transaction_descriptions

@pytest.fixture
def sample_transactions() -> List[Dict]:
    return [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1"
        },
        {
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "Transaction 2"
        },
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 3"
        },
    ]

def test_filter_by_currency_usd(sample_transactions):
    """Проверяем фильтрацию USD транзакций"""
    filtered = list(filter_by_currency(sample_transactions, "USD"))
    assert len(filtered) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in filtered)

def test_filter_by_currency_eur(sample_transactions):
    """Проверяем фильтрацию EUR транзакций"""
    filtered = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(filtered) == 1
    assert filtered[0]["description"] == "Transaction 2"

def test_filter_empty_list():
    """Проверяем работу с пустым списком"""
    assert list(filter_by_currency([], "USD")) == []

def test_filter_no_matching_currency(sample_transactions):
    """Проверяем случай, когда нет подходящих валют"""
    assert list(filter_by_currency(sample_transactions, "GBP")) == []

def test_transaction_descriptions(sample_transactions):
    """Проверяем извлечение описаний"""
    gen = transaction_descriptions(sample_transactions)
    assert next(gen) == "Transaction 1"
    assert next(gen) == "Transaction 2"
    assert next(gen) == "Transaction 3"

def test_transaction_descriptions_empty():
    """Проверяем пустой список транзакций"""
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999, 10001, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001"
    ]),
])
def test_card_number_generator(start, end, expected):
    """Проверяем генерацию номеров карт"""
    result = list(card_number_generator(start, end))
    assert result == expected

def test_card_number_formatting():
    """Проверяем форматирование номера"""
    number = next(card_number_generator(42, 42))
    assert number == "0000 0000 0000 0042"
    assert len(number) == 19  # 16 цифр + 3 пробела

def test_card_number_boundaries():
    """Проверяем граничные значения"""
    first = next(card_number_generator(1, 1))
    last = next(card_number_generator(9999999999999999, 9999999999999999))
    assert first == "0000 0000 0000 0001"
    assert last == "9999 9999 9999 9999"