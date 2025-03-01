from typing import Generator


def filter_by_currency(list_dict: list, currency: str) -> Generator:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    return (d for d in list_dict if d["operationAmount"]["currency"]["name"] == currency.upper())


def transaction_descriptions(list_dict: list) -> Generator:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for d in list_dict:
        yield d["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор генерирует номера карт в заданном диапазоне, в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, stop + 1):
        card_number = f"{str(i):0>16}"
        card_number = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
        yield card_number
