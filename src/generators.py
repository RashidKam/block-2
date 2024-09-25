from src.masks import card_number


def filter_by_currency(list_of_transactions: list[dict], currency: str = None):
    """
    функци принимает на вход список транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    :param list_of_transactions: список транзакций в виде списка словарей
    :param currency: заданная валюта транзакции
    :return: итератор транзакция заданной валюты
    """
    for transaction in list_of_transactions:
        if currency.lower() == transaction["operationAmount"]["currency"]["code"].lower():
            yield transaction


def transaction_descriptions(list_of_transactions: list[dict]):
    '''
    Функция поочередно возвращает описание каждой операции
    :param list_of_transactions: Транзакции в виде списка словарей
    :return: итератор содержащий описание всех операций
    '''
    return (x["description"] for x in list_of_transactions)


def card_number_generator():
    '''
    Генератор номеров карт начиная с '0000 0000 0000 0001' и заканчивая '9999 9999 9999 9999'
    :return: номер карты в виде 1234 1234 1324 1234
    '''
    for i in range(1, 10**16):
        result = card_number(str(i))
        yield result
