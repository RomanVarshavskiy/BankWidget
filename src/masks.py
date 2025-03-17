import logging

logging.basicConfig(
    filename="../logs/mask.log",
    filemode="w",
    format="%(asctime)s %(name)s:%(levelname)s: %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)

logger = logging.getLogger()


def get_mask_card_number(num: int | str) -> str:
    """Маскирует номер банковской карты"""
    logger.info('Starting function "get_mask_card_number"')
    if len(str(num)) == 16 and str(num).isdigit():
        mask_number = str(num)[:4] + " " + str(num)[4:6] + "**" + " " + "*" * 4 + " " + str(num)[-4:]
        logging.info("Masking card number - Success")
        return mask_number
    logging.info("Cancel - Incorrect account number entered")
    logger.info('Finished function "get_mask_card_number"')
    return "Некорректный ввод номера карты"


def get_mask_account(num_account: int | str) -> str:
    """Маскирует номер банковского счета"""
    logger.info('Starting function "get_mask_account"')
    if len(str(num_account)) == 20 and str(num_account).isdigit():
        logging.info("Masking account number - Success")
        return "**" + str(num_account)[-4:]
    logging.info("Cancel - Incorrect account number entered")
    logger.info('Finished function "get_mask_account"')
    return "Некорректный ввод номера счета"


#
# if __name__ == '__main__':
#     print(get_mask_card_number(7000792289606361))
#     print(get_mask_account(77777777777777777777))
