from src import masks


def mask_account_card(type_number: str) -> str:
    """Функция маскирует номер карты или счета"""
    type_number_list = type_number.strip().split()
    if len(type_number_list) == 0:
        raise IndexError("Некорректный ввод")
    else:
        if len(type_number_list[-1]) == 16 and type_number_list[-1].isdigit():
            type_number_list[-1] = masks.get_mask_card_number(str(type_number_list[-1]))
            return " ".join(type_number_list)
        elif len(type_number_list[-1]) == 20 and type_number_list[-1].isdigit():
            type_number_list[-1] = masks.get_mask_account(str(type_number_list[-1]))
            return " ".join(type_number_list)
        return "Некорректный ввод"


def get_date(date: str) -> str:
    """Функция обрезает дату и возвращает в формате 'ДД.ММ.ГГГГ'"""
    if len(date) < 10 or not "".join(date[:10].split("-")).isdigit():
        return "Некорректный ввод"
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
