import pytest

from src.processing import filter_by_state, sort_by_date
# from tests.conftest import *


@pytest.mark.parametrize(
    "list_of_data, state, sorted_list",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ([], None, []),
    ],
)
def test_filter_by_state(list_of_data, state, sorted_list):
    assert filter_by_state(list_of_data, state) == sorted_list


@pytest.mark.parametrize(
    "list_of_data, sort_order, sorted_list",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ([], False, []),
    ],
)
def test_sort_by_date(list_of_data, sort_order, sorted_list):
    assert sort_by_date(list_of_data, sort_order) == sorted_list


def test_sort_by_date_value_error():
    with pytest.raises(ValueError):
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "19-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "18-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "18-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "18-10-14T08:21:33.419441"},
            ],
            True,
        )
