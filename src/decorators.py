# from time import time


def log(filename: str = ""):
    """
    Данный декоратор записывает в файл/выводит в консоль логи работы функции
    :param filename: наименование файла, в который будут записываться логи работы функции
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # start_of_the_function = time()
            input_parameters = (*args, *kwargs)

            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__}; result: {result}\n"

            except Exception as e:
                # stop_of_the_function = time()
                message = f"""{func.__name__}; erorr: {e}; input parameters: {input_parameters}\n"""
            # start of the function = {start_of_the_function}\nstop of the function = {stop_of_the_function}\n\n"""

            finally:
                if filename:
                    with open(filename, "a") as file_log:
                        file_log.write(message)
                else:
                    print(message)

        return wrapper

    return decorator
