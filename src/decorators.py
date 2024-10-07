from time import time


def log(filename: str = ""):
    def decorator(funk):
        def wrapper(*args, **kwargs):
            start_of_the_function = time()
            try:
                result = funk(*args, **kwargs)
            except Exception as result:
                pass
                # input_parameters = (*args, **kwargs)
            finally:
                stop_of_the_function = time()
                if filename:
                    with open(filename, "a") as file_log:
                        file_log.write(
                            f"""{filename}\n
                            resut = {result}\n
                            start_of_the_function = {start_of_the_function}\n
                            stop_of_the_function = {stop_of_the_function}\n\n"""
                        )
                else:
                    print(
                        f"""{filename}\n
                            resut = {result}\n
                            start_of_the_function = {start_of_the_function}\n
                            stop_of_the_function = {stop_of_the_function}\n\n"""
                    )
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
