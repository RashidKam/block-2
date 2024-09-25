from src.masks import card_number

def filter_by_currency(list_of_transactions: list[dict], currency: str = None):
    for transaction in list_of_transactions:
        if currency.lower() == transaction["operationAmount"]["currency"]["name"].lower():
            yield transaction


def transaction_descriptions(list_of_transactions: list[dict]):
    return (x["description"] for x in list_of_transactions)


def card_number_generator():
    for i in range(1, 10 ** 16):
        if len(str(i)) < 16:
            i = '0' * (16 - len(str(i))) + str(i)
            yield card_number(str(i))
        yield card_number(str(i))

print(next(card_number_generator()))
print(next(card_number_generator()))
print(next(card_number_generator()))
print(next(card_number_generator()))
print(next(card_number_generator()))
print(next(card_number_generator()))
print(next(card_number_generator()))
