import json
from typing import Any, Dict, List

from config import PATH_DIR


def get_data_transactions(path: str) -> List[Dict[str, Any]]:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(PATH_DIR / f"data/{path}", "r", encoding="utf-8") as transaction_file:
            try:
                transactions = list(json.load(transaction_file))
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []

    return transactions


print(get_data_transactions("operations.json"))
# print(get_data_transactions("empty2.json"))
