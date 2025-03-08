from functools import wraps
from typing import Any, Callable

from config import PATH_DIR


def log(filename: Any = None) -> Callable:
    """Декоратор логирует начало и конец выполнения функции, а также ее
    результаты или возникшие ошибки и записывает логи в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict)  -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                result = None
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. Explanation: {e}." f" Inputs: {args}, {kwargs}"
                )
            if filename:
                with open(PATH_DIR / f"data/{filename}", "w", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return wrapper

    return decorator


# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x / y
# print(my_function(1, 0))
