def get_mask_card_number(num: int | str) -> str:
    """Маскирует номер банковской карты"""
    mask_number = str(num)[:4] + " " + str(num)[4:6] + "**" + " " + "*" * 4 + " " + str(num)[-4:]
    return mask_number


def get_mask_account(num_account: int | str) -> str:
    """Маскирует номер банковского счета"""
    return "**" + str(num_account)[-4:]