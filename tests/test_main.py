import pytest
import main
import json
from unittest import mock

# Mock data for testing
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
    # Mock requests.get to return a mock response
    with mock.patch("main.requests.get") as mocked_get:
        mocked_response = mock.Mock()
        mocked_response.json.return_value = MOCK_API_DATA
        mocked_response.raise_for_status = mock.Mock()  # No action needed
        mocked_get.return_value = mocked_response
        
        # Call the function
        result = main.fetch_data_from_api(1)
        
        # Assert that the result matches the mock data
        assert result == MOCK_API_DATA

def test_fetch_data_from_file():
    # Mock open and json.load to return mock file data
    with mock.patch("builtins.open", mock.mock_open(read_data=json.dumps(MOCK_FILE_DATA))):
        with mock.patch("main.json.load") as mocked_json_load:
            mocked_json_load.return_value = MOCK_FILE_DATA
            
            # Call the function
            result = main.fetch_data_from_file("dummy_file.json")
            
            # Assert that the result matches the mock file data
            assert result == MOCK_FILE_DATA

def test_extract_and_format_data():
    # Call the extract_and_format_data function with mock data
    formatted_data = main.extract_and_format_data(MOCK_API_DATA)
    
    # Expected formatted data
    expected_data = [
        f"Most Wanted 1þTerrorism,MurderþNew York,Los Angeles",
        f"Most Wanted 2þFraudþChicago"
    ]
    
    # Assert the formatted data matches the expected output
    assert formatted_data == expected_data
