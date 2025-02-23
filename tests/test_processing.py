import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(my_list_dict: list) -> None:
    assert filter_by_state(my_list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    assert filter_by_state(my_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(my_list_dict, "AAAAA") == []


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ("BBBBBB", []),
    ],
)
def test_filter_by_state_param(my_list_dict: list, state: str, expected: list) -> None:
    assert filter_by_state(my_list_dict, state) == expected


def test_sort_by_date_lower(my_list_dict: list) -> None:
    assert sort_by_date(my_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_upper(my_list_dict: list) -> None:
    assert sort_by_date(my_list_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same_dates() -> None:
    assert sort_by_date(
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
    ) == [
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
    ]


def test_sort_by_date_incorrect_dates() -> None:
    assert sort_by_date(
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2019.07.03T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "02-07-2018T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "01.07.2017T08:21:33.419441"},
        ]
    ) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2019.07.03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "02-07-2018T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "01.07.2017T08:21:33.419441"},
    ]
