import pytest
from config import PATH_DIR
from src.decorators import log

def test_log_to_file_sucсes(capsys):

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    assert result == 3
    with open(PATH_DIR/"data/mylog.txt") as file:
        assert file.read() == "my_function ok"

    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_to_console_error(capsys):

    @log()
    def my_function(x, y):
        return x / y

    result = my_function(1, 0)

    assert result == None

    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Explanation: division by zero. Inputs: (1, 0), {}\n"

