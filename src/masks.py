def get_mask_card_number(number_card: str) -> str:
    """принимает номер карты и возвращает ее маску, вне зависимости от длины номера карты"""

    if not number_card.isdigit():
        return 'некорректные данные'

    number_card_list = list(number_card)  # перевод номера карты из типа строка в тип список

    for i in range(6, len(number_card_list) - 4):  # замена части цифр на *
        number_card_list[i] = "*"

    for i in range(4, int(len(number_card_list) * 1.2), 5):  # разделение номера карты на блоки по 4 цифры
        number_card_list[i:i] = " "

    return "".join(number_card_list)


def get_mask_account(account_number: str) -> str:
    """принимает номер счета и возвращает его маску"""

    mask_account = f"**{account_number[-4:]}"
    return mask_account
