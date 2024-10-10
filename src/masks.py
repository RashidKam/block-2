def get_mask_card_number(number_card: str) -> str:
    """принимает номер карты и возвращает ее маску, вне зависимости от длины номера карты"""

    if number_card == "":
        return ""

    if not number_card.isdigit():
        return "некорректные данные"

    number_card_list = list(number_card)  # перевод номера карты из типа строка в тип список

    for i in range(6, len(number_card_list) - 4):  # замена части цифр на *
        number_card_list[i] = "*"

    for i in range(4, int(len(number_card_list) * 1.2), 5):  # разделение номера карты на блоки по 4 цифры
        number_card_list[i:i] = " "

    return "".join(number_card_list)


def get_mask_account(account_number: str) -> str:
    """принимает номер счета и возвращает его маску"""

    if account_number == "":
        return ""

    if not account_number.isdigit():
        return "некорректные данные"

    mask_account = f"**{account_number[-4:]}"
    return mask_account


def card_number(card_number: str) -> str:
    """
    Функция принимает порядковый номер каты и переводит его в соответствуючий вид
    :param card_number: номер карты длинной от 1 до 16 цифр
    :return: 16-значный номер карты разделённый блоками по 4 цифры (пример: '1234 1324 1234 1234')
    """
    if len(card_number) < 16:
        card_number = "0" * (16 - len(card_number)) + card_number
    number_card_list = list(card_number)
    for i in range(4, int(len(number_card_list) * 1.2), 5):  # разделение номера карты на блоки по 4 цифры
        number_card_list[i:i] = " "
    return "".join(number_card_list)
