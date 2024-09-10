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

def test_extract_and_format_data():
    formatted_data = main.extract_and_format_data(MOCK_API_DATA)
    
    expected_data = [
        f"Most Wanted 1þTerrorism,MurderþNew York,Los Angeles",
        f"Most Wanted 2þFraudþChicago"
    ]
    
    assert formatted_data == expected_data