import masks


def mask_account_card(type_number: str) -> str:
    """Функция маскирует номер карты или счета"""
    type_number_list = type_number.strip().split()
    if len(type_number_list[-1]) == 16:
        type_number_list[-1] = masks.get_mask_card_number(str(type_number_list[-1]))
    elif len(type_number_list[-1]) == 20:
        type_number_list[-1] = masks.get_mask_account(str(type_number_list[-1]))

    return " ".join(type_number_list)


def get_date(date: str) -> str:
    """Функция обрезает дату и возвращает в формате 'ДД.ММ.ГГГГ'"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
