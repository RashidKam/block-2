import pytest


@pytest.fixture
def data_of_transactions():
    return (
        [
            {
                "id": 111111111,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 333333333,
                "state": "CANCELED",
                "date": "2018-05-17T23:20:05.206878",
                "operationAmount": {"amount": "5814.62", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 11776614605963066555",
            },
            {
                "id": 142264868,
                "state": "CANCELED",
                "date": "2019-01-23T23:20:05.206878",
                "operationAmount": {"amount": "14586.71", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод с карты на карту",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284444",
            },
        ],
        "EUR",
        [
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 142264868,
                "state": "CANCELED",
                "date": "2019-01-23T23:20:05.206878",
                "operationAmount": {"amount": "14586.71", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод с карты на карту",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284444",
            },
        ],
    )
