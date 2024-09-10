import pytest

from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('input_data, mask_data',
                         [('', ''),
                          ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                          ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                          ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                          ('Счет 73654108430135874305', 'Счет **4305'),
                          ('input_data', 'Данные введены не корректно')])
def test_mask_account_card(input_data, mask_data):
    assert mask_account_card(input_data) == mask_data


@pytest.mark.parametrize('date_, corrected_date',
                         [('', ''),
                          ('2024-03-11T02:26:18.671407', '11.3.2024'),
                          ('2024-03-11', '11.3.2024'),
                          ('2024/03/11T02:26:18.671407', '11.3.2024')
                          ])
def test_get_date(date_, corrected_date):
    assert get_date(date_) == corrected_date


def test_error_get_date():
    with pytest.raises(ValueError):
        get_date('20-03-11T02:26:18.671407')
        get_date('date-20-03-11T02:26:18.671407')