# Проект "BankWidget"

## Описание:

Проект "BankWidget" - приложение на Python. Это виджет банковских операций клиента, который показывает несколько последних успешных банковских операций.
Данный проект находится на стадии разработки.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/bankwidget.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

1. 
2.

## Тестирование

Для тестирования проекта используется библиотека 'pytest'. Чтобы запустить тесты, выполните команду:
'pytest'

Тесты покрывают следующие модули и функции:
- 'masks': функции 'get_mask_card_number' и 'get_mask_account'.
- 'widget': функции 'get_date' и 'mask_account_card'.
- 'processing': функции 'filter_by_state' и 'sort_by_date'.
- 'generators': функции 'filter_by_currency', 'transaction_descriptions' и 'card_number_generator'

Покрытие тестами составляет 100% кода проекта.


## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
