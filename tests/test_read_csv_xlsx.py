from unittest.mock import patch, MagicMock

from config import PATH_DIR
from src.read_csv_xlsx import read_csv, read_excel


@patch("csv.DictReader")
@patch("builtins.open")
def test_read_csv(mock_open: MagicMock, mock_reader: MagicMock) -> None:
    mock_reader.return_value = [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
    assert read_csv("test_path") == [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
    mock_open.assert_called_once_with(PATH_DIR / "data/test_path", encoding="utf-8")
    mock_open = mock_open.return_value.__enter__.return_value
    mock_reader.assert_called_once_with(mock_open, delimiter=";")


@patch("pandas.read_excel")
def test_read_excel(mock_reader: MagicMock) -> None:
    mock_reader.return_value.to_dict.return_value = [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
    assert read_excel("test_path") == [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
    mock_reader.assert_called_once_with(PATH_DIR / "data/test_path")
