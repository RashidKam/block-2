import pytest
from unittest.mock import Mock, patch

from src.utils import download_transaction_data, external_api, request_sum_transaction
from tests.conftest import transaction_of_operations


@patch('json.load')
def test_download_transaction_data(mock_file, transaction_of_operations):
    mock_file.value_return = transaction_of_operations()

    assert download_transaction_data("/home/rashid/PycharmProjects/homework_9.1/data/operations.json") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@patch('requests.request')
def test_external_api(mock_requests):
    mock_requests.return_value.json.return_value = "{'result': 250.250}"
    assert external_api("USD", 100.00) == 250.25


def test_request_sum_transaction():
    test_data = {"operationAmount": {"amount": 31957.58, "currency": {"name": "руб.", "code": "RUB"}}}
    assert request_sum_transaction(test_data) == 31957.58
