def get_mask_card_number(num: int | str) -> str:
    """Маскирует номер банковской карты"""
    if len(str(num)) == 16 and str(num).isdigit():
        mask_number = str(num)[:4] + " " + str(num)[4:6] + "**" + " " + "*" * 4 + " " + str(num)[-4:]
        return mask_number
    return "Некорректный ввод номера карты"

def get_mask_account(num_account: int | str) -> str:
    """Маскирует номер банковского счета"""
    if len(str(num_account)) == 20 and str(num_account).isdigit():
        return "**" + str(num_account)[-4:]
    return "Некорректный ввод номера счета"
