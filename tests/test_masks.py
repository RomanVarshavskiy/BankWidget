import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_start(num_card: int | str) -> None:
    assert get_mask_card_number(7000792289606361) == num_card
    assert get_mask_card_number("7000792289606361") == num_card


@pytest.mark.parametrize(
    "value, expected",
    [
        (2222333355556666, "2222 33** **** 6666"),
        ("7777777777777777", "7777 77** **** 7777"),
        (700000007922896063611, "Некорректный ввод номера карты"),
        ("7000079228960", "Некорректный ввод номера карты"),
        ("70007%%!!&&06361", "Некорректный ввод номера карты"),
        ("", "Некорректный ввод номера карты"),
    ],
)
def test_get_mask_card_number(value: int | str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


def test_get_mask_account_start(num_account: int | str) -> None:
    assert get_mask_account(73654108430135874305) == num_account
    assert get_mask_account("73654108430135874305") == num_account


@pytest.mark.parametrize(
    "value, expected",
    [
        (77777777777777777777, "**7777"),
        ("00000000000000001234", "**1234"),
        (73654108430135874305000000, "Некорректный ввод номера счета"),
        ("73654108430135", "Некорректный ввод номера счета"),
        ("736541084301%%%&&&9", "Некорректный ввод номера счета"),
        ("", "Некорректный ввод номера счета"),
    ],
)
def test_get_mask_account(value: int | str, expected: str) -> None:
    assert get_mask_account(value) == expected
