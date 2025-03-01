import random

from tests.conftest import transactions

def filter_by_currency(list_dict: list, currency: str) -> dict:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    return (d for d in list_dict if d["operationAmount"]["currency"]["name"] == currency)


transactions = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
"description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
           {"id": 111111111, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUS", "code": "RUS"}},
            "description": "Перевод со счета на счет", "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"},
           {"id": 142264268, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет", "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"},
           {"id": 222222222, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту", "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"},
           {"id": 333333333, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "BLR", "code": "BLR"}},
            "description": "Перевод организации", "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"}]

print(*list(filter_by_currency(transactions, "USD")))


def transaction_descriptions(list_dict: list) -> str:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for d in list_dict:
        yield d["description"]

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: int, stop: int):
    """ Генератор генерирует номера карт в заданном диапазоне, в формате XXXX XXXX XXXX XXXX"""
    card_number = [random.randint(start, stop) for _ in range(16)]
    card_number = ''.join(str(n) for n in card_number)
    card_number = ' '.join(card_number[i:i+4] for i in range(0, 16, 4))

    return card_number

print((card_number_generator(1, 9)))