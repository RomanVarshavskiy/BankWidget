import csv

import pandas as pd

from config import PATH_DIR


def read_csv(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    with open(PATH_DIR / f"data/{path}", encoding="utf-8") as f:
        csv_reader = csv.DictReader(f, delimiter=";")
        return [row for row in csv_reader]


# print(read_csv('transactions.csv'))


def read_excel(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из EXCEL"""
    excel_df = pd.read_excel(PATH_DIR / f"data/{path}").to_dict(orient="records")
    return excel_df


print(read_excel("transactions_excel.xlsx"))
