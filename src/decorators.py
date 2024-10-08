from time import time


def log(filename: str = ""):
    '''
    Данный декоратор записывает в файл/выводит в консоль логи работы функции
    :param filename: наименование файла, в который будут записываться логи работы функции
    :return:
    '''
    def decorator(funk):
        def wrapper(*args, **kwargs):
            start_of_the_function = time()
            input_parameters = (*args, *kwargs)

            try:
                result = funk(*args, **kwargs)
                message = f"{funk.__name__}\nresut = {result}"

            except Exception as e:
                stop_of_the_function = time()
                message = f"""{funk.__name__}\nerorr: {e}\ninput parameters: {input_parameters}
start of the function = {start_of_the_function}\nstop of the function = {stop_of_the_function}\n\n"""

            finally:
                if filename:
                    with open(filename, "a") as file_log:
                        file_log.write(message)
                else:
                    print(message)

        return wrapper

    return decorator


# @log()
# def my_function():
#     raise Exception("СООБЩЕНИЕ !!! !!!")
#
#
# my_function()


@log("her.txt")
def my_function(x, y):
    aaaa = x + y
    raise Exception("СООБЩЕНИЕ !!! !!!")


my_function(1, 2)
