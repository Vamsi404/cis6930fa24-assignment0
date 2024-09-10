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

def test_fetch_data_from_api():
    with mock.patch("main.requests.get") as mocked_get:
        mocked_response = mock.Mock()
        mocked_response.json.return_value = MOCK_API_DATA
        mocked_response.raise_for_status = mock.Mock()
        mocked_get.return_value = mocked_response
        
        result = main.fetch_data_from_api(1)
        
        assert result == MOCK_API_DATA
