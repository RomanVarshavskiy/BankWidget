import os

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_amount_in_rub(data: dict) -> float:
    """Функция возвращает сумму транзакции (amount) в рублях"""
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&"
        f"from={data["operationAmount"]["currency"]["code"]}&amount={data["operationAmount"]["amount"]}"
    )
    headers = {"apikey": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers)
    if data["operationAmount"]["currency"]["code"] == "RUB":
        return float(data["operationAmount"]["amount"])
    else:
        if response.status_code != 200:
            raise ValueError("Failed to get currency rate")
        result = response.json()
        currency_result = result["result"]
        return float(currency_result)


# transaction = {"id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"}
# print(transaction_amount_in_rub(transaction))
