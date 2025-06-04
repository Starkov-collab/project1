import datetime

import pytest


@pytest.fixture
def not_16_digets_card():
    return "Номер карты должен содержать 16 цифр"


@pytest.fixture()
def not_isdigit_card():
    return "Номер карты должен содержать только цифры"


@pytest.fixture
def not_20_digets_account():
    return "Номер счета должен содержать 20 цифр"


@pytest.fixture()
def not_isdigit_account():
    return "Номер счет должен содержать только цифры"


@pytest.fixture(
    params=[
        ("2023-05-15", "15.05.2023"),  # Обычная дата
        ("2000-12-31", "31.12.2000"),  # Граничные значения года
        ("1999-01-01", "01.01.1999"),  # Начало года
        ("2020-02-29", "29.02.2020"),  # Високосный год])
    ]
)
def valid_date_pair(request):
    """Фикстура возвращает пары (входная дата, ожидаемый результат)"""
    return request.param


@pytest.fixture(
    params=[
        "2023-13-01",
        "2023-02-30",
        "not-a-date",
        "2023/05/15",
        "",
    ]
)
def invalid_date(request):
    """Фикстура возвращает некорректные даты"""
    return request.param


@pytest.fixture
def operations():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
