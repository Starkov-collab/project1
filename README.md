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

# Декоратор log для логирования выполнения функций
Этот модуль предоставляет декоратор log для логирования выполнения функций, который может записывать результаты как в консоль, так и в файл.

## Функциональность
### Декоратор log предоставляет следующие возможности:

Логирование успешного выполнения функции:

Записывает имя функции и возвращаемое значение

Поддерживает как вывод в консоль, так и запись в файл

Логирование ошибок:

Перехватывает все исключения

Записывает тип ошибки, аргументы функции и ключевые аргументы

Поддерживает оба режима вывода (консоль/файл)

Гибкость вывода:

При указании filename логи пишутся в файл

Без filename - вывод в консоль

## Использование
Базовый пример (вывод в консоль)
python
@log()
def add(a, b):
    return a + b

add(2, 3)  # Вывод: "Функция add успешно завершена. Результат: 5"
Логирование в файл
python
@log(filename="operations.log")
def multiply(a, b):
    return a * b

multiply(4, 5)  # Запись в файл operations.log
### Обработка ошибок
python
@log()
def divide(a, b):
    return a / b

divide(10, 0)  # Вывод: "Ошибка в divide: ZeroDivisionError, args: (10, 0), kwargs: {}"
### Тестирование
Для тестирования декоратора используется pytest. Тесты проверяют:

Успешное выполнение с выводом в консоль

Обработку ошибок с выводом в консоль

Успешное выполнение с записью в файл

Обработку ошибок с записью в файл

Режим добавления записей в файл (не перезапись)

Сохранение метаданных функции

Запуск тестов
bash
pytest tests/test_decorators.py -v

pytest (для тестирования)

# Рекомендации по использованию
Для сохранения метаданных функций рекомендуется использовать @functools.wraps

Для важных задач рассмотрите добавление временных меток в логи

При работе с файлами убедитесь в наличии прав на запись

Для больших проектов рассмотрите использование стандартного модуля logging

Пример расширенного использования
python
from datetime import datetime
from functools import wraps

def log(filename=None, with_time=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                timestamp = f"[{datetime.now()}] " if with_time else ""
                message = f"{timestamp}Функция {func.__name__} успешно завершена. Результат: {result}"
                
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                
                return result
            except Exception as e:
                timestamp = f"[{datetime.now()}] " if with_time else ""
                message = f"{timestamp}Ошибка в {func.__name__}: {type(e).__name__}, args: {args}, kwargs: {kwargs}"
                
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
        return wrapper
    return decorator

