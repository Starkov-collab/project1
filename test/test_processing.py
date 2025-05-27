from src.processing import filter_by_state, sort_by_date

#Тестовые данные
test_operat = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Тест 1: Проверка фильтрации по state="EXECUTED" (значение по умолчанию)
def test_filter_by_state_executed():
    result = filter_by_state(test_operat)
    assert len(result) == 2  # Должно быть 2 элемента
    assert all(op["state"] == "EXECUTED" for op in result)  # Все операции EXECUTED


def test_filter_by_state_canceled():
    result = filter_by_state(test_operat, state="CANCELED")  # Указываем нужный статус
    assert len(result) == 2
    assert all(op["state"] == "CANCELED" for op in result)

def test_filter_by_state_list():
    result = filter_by_state([])
    assert result == []



#Тестовые данные
test_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def test_sort_descending(operations):
    """Сортировка от новых к старым (reverse=True)."""
    result = sort_by_date(operations, reverse=True)
    # Ожидаемый порядок id: 2019 → 2018-10 → 2018-09 → 2018-06
    assert [op["id"] for op in result] == [41428829, 615064591, 594226727, 939719570]

def test_sort_ascending(operations):
    """Сортировка от старых к новым (reverse=False)."""
    result = sort_by_date(operations, reverse=False)
    # Ожидаемый порядок id: 2018-06 → 2018-09 → 2018-10 → 2019
    assert [op["id"] for op in result] == [939719570, 594226727, 615064591, 41428829]