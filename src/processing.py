def filter_by_state(my_list: list, state="EXECUTED") -> list:
    """Функция фильтрует список словарей  по значению ключа state"""
    filter_list = [d for d in my_list if d["state"] == state]

    return filter_list
