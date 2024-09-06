# -*- coding: utf-8 -*-
import argparse
import sys
import requests
import json

THORN = 'þ'  # Thorn character for separating fields


def fetch_data_from_api(page):
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


def fetch_data_from_file(file_location):
    with open(file_location, 'r') as file:
        data = json.load(file)
    return data


def extract_and_format_data(data):
    formatted_data = []

    for item in data.get('items', []):
        title = item.get('title', '')
        subjects = ','.join(item.get('subjects', []))
        field_offices = item.get('field_offices') or []
        field_offices_str = ','.join(field_offices)
        formatted_data.append(f"{title}{THORN}{subjects}{THORN}{field_offices_str}")

    return formatted_data


def print_to_stdout(formatted_data):
    for row in formatted_data:
        print(row)


def main(page=None, file_location=None):
    if page is not None:
        data = fetch_data_from_api(page)
    elif file_location is not None:
        data = fetch_data_from_file(file_location)
    else:
        raise ValueError("Either 'page' or 'file_location' must be provided.")

    formatted_data = extract_and_format_data(data)
    print_to_stdout(formatted_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch and format data from the FBI wanted API.")
    parser.add_argument("--file", type=str, required=False, help="File location of the JSON file for testing")
    parser.add_argument("--page", type=int, required=False, help="Page number to fetch data from the FBI API")

    args = parser.parse_args()
    
    if args.page:
        main(page=args.page)
    elif args.file:
        main(file_location=args.file)
    else:
        parser.print_help(sys.stderr)
