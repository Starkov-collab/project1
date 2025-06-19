import json
import logging
import os
from typing import Dict, List

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path : str) -> List[Dict] :
    """функция принимает на выход путь к файлу JSON"""
    try :
        with open(file_path , 'r') as file :
            """Открываем путь к файлу json в режиме чтения
             Использование with гарантирует, 
             что файл будет автоматически закрыт после завершения работы с ним, 
             что помогает избежать утечек ресурсов. """
            transaction = json.load(file)
            """Используем json.load для загрузки данных из файла"""
            if isinstance(transaction, list) :
                """Используем для проверки является ли объект экземпляром данного класса"""
                return transaction
            else :
                logging.info(f'Данные не найдены')
                return []
            """возвращаем пустой список если данных нет или вызывает ошибку"""
    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {file_path}, ошибка: {ex}')
        return []
except json.JSONDecodeError as ex :
    logger.error(f'Ошибка декодирования JSON в файле {file_path}, ошибка: {ex}')
    return []


transactions = load_transactions('./data/operations.json')
print(transactions)
