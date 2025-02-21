import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(num_card):
    assert get_mask_card_number(7000792289606361) == num_card
    assert get_mask_card_number("7000792289606361") == num_card


@pytest.mark.parametrize("value, expected", [(7000792289606361, "7000 79** **** 6361"),
                                             ("7000792289606361", "7000 79** **** 6361"),
                                             (700000007922896063611, "Некорректный ввод номера карты"),
                                             ("7000079228960", "Некорректный ввод номера карты"),
                                             ("70007%%!!&&06361", "Некорректный ввод номера карты"),
                                             ('', "Некорректный ввод номера карты")])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


# def test_get_mask_card_number_size():
#     with pytest.raises(ValueError):
#         get_mask_card_number("700000007922896063611")



def test_get_mask_account(num_account):
    assert get_mask_account(73654108430135874305) == num_account
    assert get_mask_account("73654108430135874305") == num_account


@pytest.mark.parametrize("value, expected", [(73654108430135874305, "**4305"),
                                             ("73654108430135874305", "**4305"),
                                             (73654108430135874305000000, "Некорректный ввод номера счета"),
                                             ("73654108430135", "Некорректный ввод номера счета"),
                                             ("736541084301%%%&&&9", "Некорректный ввод номера счета"),
                                             ("", "Некорректный ввод номера счета")])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
