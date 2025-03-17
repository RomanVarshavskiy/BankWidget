import json
import logging
from typing import Any, Dict, List

from config import PATH_DIR

logging.basicConfig(
    filename="../logs/utils.log",
    filemode="w",
    format="%(asctime)s %(name)s:%(levelname)s: %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)

logger = logging.getLogger()


def get_data_transactions(path: str) -> List[Dict[str, Any]]:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    logger.info('Starting function "get_data_transactions"')
    try:
        with open(PATH_DIR / f"data/{path}", "r", encoding="utf-8") as transaction_file:
            try:
                logging.info("Transactions received successfully")
                transactions = list(json.load(transaction_file))
            except json.JSONDecodeError:
                logging.info("Error decoding file. JSONDecodeError")
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logging.info(f"File {path} not found. FileNotFoundError")
        print(f"Файл {path} не найден")
        return []

    logger.info("Finished function")
    return transactions


# print(get_data_transactions("operations.json"))
# print(get_data_transactions("empty2.json"))
