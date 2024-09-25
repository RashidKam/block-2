import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(data_of_transactions):
    data_list, currency, result = data_of_transactions
    assert list(filter_by_currency(data_list, currency)) == result


def test_transaction_descriptions(data_of_transactions):
    data_list, _, _ = data_of_transactions
    assert list(transaction_descriptions(data_list)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_card_number_generator():
    generator_ = card_number_generator()
    assert next(generator_) == "0000 0000 0000 0001"
    assert next(generator_) == "0000 0000 0000 0002"
    assert next(generator_) == "0000 0000 0000 0003"
    assert next(generator_) == "0000 0000 0000 0004"
