import json
import logging
import os
from typing import Dict, List


# Настройка логгера для модуля utils
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень DEBUG

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Настраиваем формат записи
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict]:
    """Функция принимает на вход путь к файлу JSON и возвращает список транзакций"""
    try:
        logger.debug(f'Попытка открыть файл: {file_path}')
        with open(file_path, 'r', encoding='utf-8') as file:
            transaction = json.load(file)

            if isinstance(transaction, list):
                logger.info(f'Успешно загружено {len(transaction)} транзакций из файла {file_path}')
                return transaction
            else:
                logger.warning(f'Данные в файле {file_path} не являются списком')
                return []

    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {file_path}. Ошибка: {str(ex)}')
        return []
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка декодирования JSON в файле {file_path}. Ошибка: {str(ex)}')
        return []
    except Exception as ex:
        logger.error(f'Непредвиденная ошибка при обработке файла {file_path}. Ошибка: {str(ex)}')
        return []


if __name__ == '__main__':
    transactions = load_transactions('./data/operations.json')
    print(transactions)
