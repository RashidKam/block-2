from datetime import date


def filter_by_state(list_of_data: list[dict], state:str="EXECUTED") -> list[dict]:
    '''Функция принимает список словарей и возвращает новый список со словарями
    у которых значение по ключу "state" равно "EXECUTED"'''

    result = []
    for i in list_of_data:
        if i["state"] == state:
            result.append(i)
    return result


def sort_by_date(list_of_data: list[dict], sort_order: bool = False) -> list[dict]:
    """
    Возвращает список словарей, отсортированный по ключу "date"
    :param list_of_data: исходный список словарей
    :param sort_order: порядок сортировки (опционально)
    :return: отсортированный список словарей
    """

    return sorted(
        list_of_data,
        key=lambda list_of_data: date(
            int(list_of_data["date"][0:4]), int(list_of_data["date"][5:7]), int(list_of_data["date"][8:10])
        ),
        reverse=sort_order,
    )
