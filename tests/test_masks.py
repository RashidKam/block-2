import pytest

from src.masks import card_number, get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, mask_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000792289606361883402", "7000 79** **** **** **34 02"),
        ("number_card", "некорректные данные"),
        ("0000", "0000"),
        ("", ""),
    ],
)
def test_get_mask_card_number(number_card, mask_card):
    assert get_mask_card_number(number_card) == mask_card


@pytest.mark.parametrize(
    "account_number, mask_account_number",
    [
        ("", ""),
        ("73654108430135874305", "**4305"),
        ("7365410000008430135874305", "**4305"),
        ("0135874305", "**4305"),
        ("account_number", "некорректные данные"),
    ],
)
def test_get_mask_account(account_number, mask_account_number):
    assert get_mask_account(account_number) == mask_account_number


@pytest.mark.parametrize(
    "number_card, corrected_number_card",
    [
        ("01", "0000 0000 0000 0001"),
        ("1", "0000 0000 0000 0001"),
        ("44444444564897651321312", "4444 4444 5648 9765 1321 312"),
        ("", "0000 0000 0000 0000"),
    ],
)
def test_card_number(number_card, corrected_number_card):
    assert card_number(number_card) == corrected_number_card
