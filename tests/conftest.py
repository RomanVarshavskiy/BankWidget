import pytest


@pytest.fixture
def num_card() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def num_account() -> str:
    return "**4305"


@pytest.fixture
def name_card_number() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def account() -> str:
    return "Счет **4305"


@pytest.fixture
def my_list_dict() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
