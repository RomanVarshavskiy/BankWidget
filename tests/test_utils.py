import json
from unittest.mock import MagicMock, patch

from src.utils import get_data_transactions

path = "operations.json"


@patch("json.load")
def test_get_data_transactions_file_for_patch(mock_json_load: MagicMock) -> None:
    mock_json_load.return_value = [{"1": 1, "2": 2}]
    assert get_data_transactions(path) == [{"1": 1, "2": 2}]
    mock_json_load.assert_called_once()


@patch("builtins.open")
@patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load: MagicMock, mock_open: MagicMock) -> None:
    result = get_data_transactions("fake_path.json")
    assert result == []
    mock_json_load.assert_called_once()


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_error(mock_open: list) -> None:
    result = get_data_transactions("fake_path.json")
    assert result == []
