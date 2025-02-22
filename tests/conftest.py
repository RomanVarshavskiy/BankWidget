import pytest


@pytest.fixture
def num_card():
    return "7000 79** **** 6361"


@pytest.fixture
def num_account():
    return "**4305"


@pytest.fixture
def name_card_number():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def account():
    return "Счет **4305"
