import json
import requests
import os
from dotenv import load_dotenv
from typing import Dict,List


load_dotenv()

def get_currency_usd_or_euro(transaction : Dict) -> float :
    try:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]

        if currency_code not in ("USD", "EUR"):
            return float(amount)  # Преобразуем строку в число для неконвертируемых валют

        url = (f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
               f"{currency_code}&amount="
               f"{amount}")
        headers = {
            "apikey": os.getenv("API_KEY")  # подтягиваем API ключ из переменных окружения
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:  # Успешный запрос
            return round(float(response.json()["result"]), 3)
        else:
            print(f"Ошибка запроса: {response.status_code} - {response.text}")
            return 0.0

    except (KeyError, ValueError, requests.RequestException) as e:
        print(f"Ошибка обработки транзакции: {e}")
        return 0.0


# with open("../data/operations.json", "r", encoding="utf-8") as f:
#     trans = json.load(f) #  позволяет прочитаь и загрузить целиком json file
#
# for tran in trans :
#     print(tran)
# #print(
#     get_currency_usd_or_euro(
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {
#                 "amount": "8221.37",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560"
#         }
#     )
# )



