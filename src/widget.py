from datetime import date

from masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Принимает тип и номер карты или счета, а возвращает их замаскированными"""

    if account_card[-20:].isdigit():
        return f"{account_card[:-20]}**{account_card[-4:]}"  # проверка на соответствие счета

    elif account_card[-16:].isdigit():  # проверка на соответствие номера карты
        return f"{account_card[:-16]}{get_mask_card_number(account_card[-16:])}"

    else:
        return "Данные введены не корректно"


def get_date(date_: str) -> str:
    """Преоброзует информацию о дате
    принимет <2024-03-11T02:26:18.671407>
    Возвращает <ДД.ММ.ГГГГ>
    """

    corrected_date = date(int(date_[0:4]), int(date_[5:7]), int(date_[8:10]))
    return "{}.{}.{}".format(corrected_date.day, corrected_date.month, corrected_date.year)
    # return f"{date_[8:10]}.{date_[5:7]}.{date_[0:4]}"  прошлое решение
