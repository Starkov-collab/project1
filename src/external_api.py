import json
import requests
import os
from dotenv import load_dotenv
from typing import Dict,List


load_dotenv()

def get_currency_usd_or_euro(transaction : Dict) -> float :
        currency_code = transaction["operationAmount"]["currency"]["code"]
        currency_amount = transaction["operationAmount"]["amount"]
        if currency_code in ("USD","EUR") :
            url = (f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
                   f"{currency_code}&amount="
                   f"{currency_amount}")
            headers = {
                    "apikey": os.getenv("API_KEY") #подтягиваю  API
                }
            response = requests.get(url, headers=headers)
            if response.status_code == 200 : # Рабочий запрос
                #print((response.json()))# возращает массив данных
                return round(float(response.json()["result"]),3)

            else:
                print(f"Ошибка запроса: {response.status_code} - {response.text}")
                return 0.0
        else :
            return currency_amount


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



