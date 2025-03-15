import os
import requests
from dotenv import load_dotenv

def transaction_amount_in_rub(data: dict):# -> float:
    """Функция возвращает сумму транзакции (amount) в рублях"""
    if data["operationAmount"]["currency"]["code"] == "RUB":
        return (data["operationAmount"]["amount"])
    else:
        load_dotenv()
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction["operationAmount"]["currency"]["code"]}&amount={transaction["operationAmount"]["amount"]}'
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Failed to get currency rate")

        return response.json()["result"]


transaction = {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
     'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
     'to': 'Счет 35383033474447895560'}
print(transaction_amount_in_rub(transaction))
