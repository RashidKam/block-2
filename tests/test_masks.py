import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('number_card, mask_card',
                         [('7000792289606361', '7000 79** **** 6361'),
                          ('7000792289606361883402', '7000 79** **** **** **34 02'),
                          ('number_card', 'некорректные данные'),
                          ('0000', '0000'),
                          ('', '')])
def test_get_mask_card_number(number_card, mask_card):
    assert get_mask_card_number(number_card) == mask_card


@pytest.mark.parametrize('account_number, mask_account_number',
                         [('', ''),
                          ('73654108430135874305', '**4305'),
                          ('7365410000008430135874305', '**4305'),
                          ('0135874305', '**4305'),
                          ('account_number', 'некорректные данные')])
def test_get_mask_account(account_number, mask_account_number):
    assert get_mask_account(account_number) == mask_account_number
