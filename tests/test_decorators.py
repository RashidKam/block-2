from src.decorators import log

# Функция проверки записи логов в файл
# @log('test_log.txt')
# def test_log(x, y):
#     return x * y
#
#
# def test_log_file():
#     test_log(4, 5)
#     with open(filename, "r") as file_log:


def test_log_print(capsys):
    @log()
    def test_func(x, y):
        return x * y

    test_func(4, 5)
    assert capsys.readouterr().out == ("test_func; result: 20\n\n")


def test_log_erorr_print(capsys):
    @log()
    def test_func_erorr(x, y):
        raise Exception("Текст исключения")

    test_func_erorr(4, 5)
    assert capsys.readouterr().out == ("test_func_erorr; erorr: Текст исключения; input parameters: (4, 5)\n\n")
