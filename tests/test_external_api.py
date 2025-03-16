from unittest.mock import MagicMock, patch

import pytest

from src.external_api import transaction_amount_in_rub


def test_transaction_amount_in_rub_RUB(transactions: list) -> None:
    assert transaction_amount_in_rub(transactions[1]) == float(transactions[1]["operationAmount"]["amount"])


@patch("requests.get")
def test_transaction_amount_in_rub_from_currency_success(mock_get: MagicMock, transactions: list) -> None:
    expected = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1742114283, "rate": 85.145342},
        "date": "2025-03-16",
        "result": 836473.799982,
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = expected
    assert transaction_amount_in_rub(transactions[0]) == expected["result"]
    mock_get.assert_called_once()


@patch("requests.get")
def test_transaction_amount_in_rub_failed_request(mock_get: MagicMock, transactions: list) -> None:
    mock_get.return_value.status_code = 404

    with pytest.raises(ValueError, match="Failed to get currency rate"):
        transaction_amount_in_rub(transactions[0])
