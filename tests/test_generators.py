import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list, usd_transactions: list):
    assert list(filter_by_currency(transactions, "USD")) == usd_transactions
    assert list(filter_by_currency(transactions, "BYN")) == [transactions[-1]]

def test_filter_by_currency_incorrect_curn(transactions: list, usd_transactions: list):
    assert list(filter_by_currency(transactions, "PLN")) == []

def test_filter_by_currency_empty_list(transactions: list, usd_transactions: list):
    assert list(filter_by_currency([], "AED")) == []

def test_transaction_descriptions(transactions: list) -> None:
    assert list(transaction_descriptions(transactions)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert transaction_descriptions(transactions[1]) == "Перевод организации"
    assert transaction_descriptions([]) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            8,
            12,
            [
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
            ],
        ),
        (1, 1, ["0000 0000 0000 0001"]),
        (9999999999999998, 9999999999999999, [["9999 9999 9999 9998", "9999 9999 9999 9999"]]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str):
    assert list(card_number_generator(8, 12)) == expected
