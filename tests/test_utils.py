import json

from unittest.mock import Mock, patch

import pytest

from src.utils import get_data_transactions

path = "operations.json"
def test_get_data_transactions():
    mock_transactions = Mock(return_value=[{'1': 1, "2": 2}])
    json.load = mock_transactions
    assert get_data_transactions(path) == [{'1': 1, "2": 2}]
    mock_transactions.assert_called_once()


@patch('json.load')
def test_get_data_transactions_patch(mock_transactions):
    mock_transactions.return_value = [{'1': 1, "2": 2}]
    assert get_data_transactions(path) == [{'1': 1, "2": 2}]
    mock_transactions.assert_called_once()

@patch("builtins.open")
@patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load, mock_open):
    from src.utils import get_data_transactions
    result = get_data_transactions("fake_path.json")
    assert result == []

# #
# @patch("builtins.open", side_effect=FileNotFoundError)
# def test_file_not_found_error(mock_open):
#     from src.utils import get_data_transactions
#     result = get_data_transactions("fake_path.json")
#     assert result == []