from typing import Any
from functools import wraps
from config import PATH_DIR

def log(filename: Any=None):
    """Декоратор логирует начало и конец выполнения функции, а также ее
    результаты или возникшие ошибки и записывает логи в файл или в консоль"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                result = None
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
            if filename:
                with open(PATH_DIR/"data/filename", "w", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result
        return wrapper
    return decorator


@log()#filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(1, 0)
# print(my_function(1, 0))