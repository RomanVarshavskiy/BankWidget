import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_number_card(name_card_number: str) -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == name_card_number


def test_mask_account_card_number_account(account: str) -> None:
    assert mask_account_card("Счет 73654108430135874305") == account


@pytest.mark.parametrize(
    "value, expected",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет ***///%%%$$$@@@@9589", "Некорректный ввод"),
        ("Visa Classic XXXXXXXXXXXXXXXX", "Некорректный ввод"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_mask_account_card_empty() -> None:
    with pytest.raises(IndexError):
        mask_account_card("")


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-03-11") == "11.03.2024"
    assert get_date("2024-03-TTT02:26:18.671407") == "Некорректный ввод"
    assert get_date("") == "Некорректный ввод"
