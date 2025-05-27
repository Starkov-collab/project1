import pytest
from datetime import datetime
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("number, result",[
    ("Maestro 1596837868705199","Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589","Счет **9589"),
    ("MasterCard 7158300734726758","MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560","Счет **5560"),
    ("Visa Classic 6831982476737658","Visa 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229","Visa 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353","Visa 5999 41** **** 6353"),
    ("Счет 73654108430135874305","Счет **4305"),
    ])
def test_mask_account_card(number,result):
    assert mask_account_card(number) == result


@pytest.mark.parametrize("date,expected_output", [
    ("2023-05-15", "15.05.2023"),  # Обычная дата
    ("2000-12-31", "31.12.2000"),  # Граничные значения года
    ("1999-01-01", "01.01.1999"),  # Начало года
    ("2020-02-29", "29.02.2020"),  # Високосный год])
])
def test_get_date_valid(date,expected_output) :
    """Проверяем коректное преобразование даты"""
    assert get_date(date) == expected_output

#Негативные тесты
@pytest.mark.parametrize("date", [
    "2023-13-20" # Некоректный месяц
    "2000-12-32"# Несуществующий день
    "" # Пустая строка
])
def test_get_date_invalid(date):
    with pytest.raises(ValueError):
        get_date(date)


