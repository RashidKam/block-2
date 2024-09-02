import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('number_card, mask_card',
                         [('7000792289606361', '7000 79** **** 6361'),
                          ('7000792289606361883402', '7000 79** **** **** **34 02'),
                          ('number_card', 'некорректные данные'),
                          ('0000', '0000'),
                          ('', 'некорректные данные')])
def test_get_mask_card_number(number_card, mask_card):
    assert get_mask_card_number(number_card) == mask_card
