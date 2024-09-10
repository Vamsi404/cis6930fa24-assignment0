import pytest
import main
import json
from unittest import mock

MOCK_API_DATA = {
    "items": [
        {
            "title": "Most Wanted 1",
            "subjects": ["Terrorism", "Murder"],
            "field_offices": ["New York", "Los Angeles"]
        },
        {
            "title": "Most Wanted 2",
            "subjects": ["Fraud"],
            "field_offices": ["Chicago"]
        }
    ]
}

MOCK_FILE_DATA = {
    "items": [
        {
            "title": "File Wanted 1",
            "subjects": ["Robbery"],
            "field_offices": ["Houston"]
        }
    ]
}


def test_fetch_data_from_file():
    with mock.patch("builtins.open", mock.mock_open(read_data=json.dumps(MOCK_FILE_DATA))):
        with mock.patch("main.json.load") as mocked_json_load:
            mocked_json_load.return_value = MOCK_FILE_DATA
            
            result = main.fetch_data_from_file("dummy_file.json")
            
            assert result == MOCK_FILE_DATA
