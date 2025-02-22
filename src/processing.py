def filter_by_state(my_list: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует список словарей по значению ключа state"""
    filter_list = [d for d in my_list if d["state"] == state]

    return filter_list


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Функция сортирует список словарей по значению ключа date"""
    if reverse:
        sorted_list = sorted(list_dict, key=lambda d: d["date"], reverse=True)
    else:
        sorted_list = sorted(list_dict, key=lambda d: d["date"])

    return sorted_list
