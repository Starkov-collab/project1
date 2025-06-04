# Цель проекта
Этот проект предоставляет набор инструментов для работы с банковскими операциями:

Маскировка номеров карт и счетов

Фильтрация операций по статусу

Сортировка операций по дате

Форматирование дат

# Описание
Этот проект представляет собой систему для управления банковскими операциями. 
Он включает в себя функции для фильтрации и сортировки операций по статусу и дате. 
Проект написан на Python и использует список словарей для хранения данных о банковских транзакциях.

## Структура проекта
Проект состоит из следующих частей:
- Основной код, реализующий функции обработки банковских операций.
- Тесты для проверки функциональности.
- Конфигурационные файлы проекта.

### Основные файлы и папки:
- src/ — Исходный код проекта.
- tests/ — Тесты для проверки корректности работы функций.
- README.md — Документация по проекту.
- .gitignore — Файл для исключения ненужных файлов из Git.


## Установка
1.Склонируйте репозиторий:
```
git clonegit@github.com:Starkov-collab/project1.git
```
2.Перейдите в директорию проекта:
```
pythonProject6
```
3.Установите зависимости:

bash
pip install -r requirements.txt


#### Использование данных
1. Маскировка данных
Маскировка номера карты:
python
from src.masks import get_mask_card_number

masked_card = get_mask_card_number("7000792289606361")
print(masked_card)  # "7000 79** **** 6361"
Маскировка номера счета:
python
from src.masks import get_mask_account
masked_account = get_mask_account("73654108430135874305")
print(masked_account)  # "**4305"
Автоматическое определение типа данных:
python
from src.utils import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))  # "Visa Platinum 7000 79** **** 6361"
print(mask_account_card("Счет 73654108430135874305"))      # "Счет **4305"
2. Работа с датами
Форматирование даты:
python
from src.utils import get_date

formatted_date = get_date("2019-07-03T18:35:29.512364")
print(formatted_date)  # "03.07.2019"
3. Фильтрация операций
python
from src.filters import filter_by_state

operations = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'CANCELED'},
    {'id': 3, 'state': 'EXECUTED'}
]

# Фильтрация выполненных операций (по умолчанию)
executed_ops = filter_by_state(operations)
print(executed_ops)  # [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

# Фильтрация отмененных операций
canceled_ops = filter_by_state(operations, 'CANCELED')
print(canceled_ops)  # [{'id': 2, 'state': 'CANCELED'}]
4. Сортировка операций
python
from src.filters import sort_by_date

operations = [
    {'id': 1, 'date': '2021-07-12T15:30:00.000000'},
    {'id': 2, 'date': '2018-03-23T10:45:30.000000'},
    {'id': 3, 'date': '2019-08-26T10:50:58.294041'}
]

# Сортировка по убыванию (новые -> старые)
sorted_desc = sort_by_date(operations)
print(sorted_desc)  # [{'id': 1}, {'id': 3}, {'id': 2}]

# Сортировка по возрастанию (старые -> новые)
sorted_asc = sort_by_date(operations, reverse=False)
print(sorted_asc)  # [{'id': 2}, {'id': 3}, {'id': 1}]
📂 Структура проекта
bank-operations/
├── src/
│   ├── __init__.py
│   ├── masks.py          # Функции маскировки
│   ├── utils.py          # Вспомогательные функции
│   └── filters.py        # Фильтрация и сортировка
├── tests/                # Тесты
├── requirements.txt      # Зависимости
└── README.md             # Документация
🧪 Тестирование
Для запуска тестов выполните:

bash
python -m pytest tests/


# Модуль для работы с банковскими транзакциями
Этот модуль предоставляет инструменты для работы с банковскими транзакциями, включая фильтрацию по валюте, извлечение описаний операций и генерацию номеров банковских карт.

## Установка
bash
pip install -e .
### Функционал модуля
1. Фильтрация транзакций по валюте (filter_by_currency)
Функция фильтрует список транзакций, возвращая только те, которые выполнены в указанной валюте.

Пример использования:

python
from transaction_utils import filter_by_currency

# Получаем только USD-транзакции
usd_transactions = filter_by_currency(transactions, "USD")

# Преобразуем итератор в список для просмотра
print(list(usd_transactions))
Ожидаемый вывод:

python
[
    {
        "id": 939719570,
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации",
        ...
    },
    {
        "id": 142264268, 
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод со счета на счет",
        ...
    },
    {
        "id": 895315941,
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод с карты на карту",
        ...
    }
]
2. Извлечение описаний транзакций (transaction_descriptions)
Генератор, который последовательно возвращает описания транзакций.

Пример использования:

python
from transaction_utils import transaction_descriptions

# Создаем генератор описаний
descriptions = transaction_descriptions(transactions)

# Получаем первые 3 описания
for _ in range(3):
    print(next(descriptions))
Ожидаемый вывод:

Перевод организации
Перевод со счета на счет
Перевод со счета на счет
3. Генератор номеров банковских карт (card_number_generator)
Генерирует номера карт в указанном диапазоне в формате XXXX XXXX XXXX XXXX.

Пример использования:

python
from transaction_utils import card_number_generator

# Генерируем номера карт от 1 до 5
for card_number in card_number_generator(1, 5):
    print(card_number)
Ожидаемый вывод:

0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
Тестирование
Для запуска тестов выполните:

bash
pytest --cov=transaction_utils --cov-report=html tests/
Отчет о покрытии кода тестами будет доступен в директории htmlcov/.

Требования

pytest (для тестирования)

pytest-cov (для проверки покрытия)
