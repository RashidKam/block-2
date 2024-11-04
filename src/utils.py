import json
import os

import requests
from dotenv import load_dotenv


def download_transaction_data(path_to_file: str) -> list:
    """
    Функция принимает путь до файла с танзакциями и возвращает их в виде списка словарей.
    В случае если файл не найден или файл пустой, вернёт пустой список
    :param path_to_file: путь до файла
    """
    try:
        with open(path_to_file) as file_data_of_transaction:
            transaction_data = json.load(file_data_of_transaction)
    except FileNotFoundError:
        return []
    else:
        if type(transaction_data) == list:
            return transaction_data
        else:
            return []


# Путь до файла с транзакциями
# '/home/rashid/PycharmProjects/homework_9.1/data/operations.json'


def external_api(currency: str, amount: float) -> float:
    """
    Конвертирует сумму заданной валюты в рубли по средствам обращения к внешнему API
    :param currency: вид заданной валюты формат  'USD', 'EUR' или др.
    :param amount: сумма заданной валюты
    :return: значение, переведенное в рубли
    """
    load_dotenv()
    my_api_key = os.getenv("API_KEY_APILAYER")
    payload = {}
    headers = {"apikey": my_api_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        result = round(response.json()["result"], 2)
        return result
    else:
        raise Exception("Неполадки")  # Позднее необходимо прописать варианты исключений


def request_sum_transaction(transaction: dict) -> float:
    """
    Принимает информацию о транзакции и возвращает сумму транзакции в рублях
    :param transaction: информация о транзакции в формате словаря
    :return:
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency == "RUB":
        return amount
    else:
        return external_api(currency, amount)
