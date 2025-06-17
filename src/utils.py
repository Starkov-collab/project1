import json
import os
from typing import Dict, List


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
                return []
            """возвращаем пустой список если данных нет или вызывает ошибку"""
    except FileNotFoundError :
        return []


transactions = load_transactions('../data/operations.json')
print(transactions)
