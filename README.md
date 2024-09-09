
# CIS6930FA24 -- Assignment 0 -- Template

**Name**: Vamsi Manda
UFID: 43226231

## Assignment Description

The goal of this assignment is to develop a Python command-line tool that interacts with the FBI’s Most Wanted API and processes data either from the API or a local JSON file. The task involves fetching data on wanted individuals, reformatting it, and outputting the result with thorn (`þ`) as the delimiter between fields.

The assignment requires implementing functionality to:

1. **Fetch Data from the FBI API**: Retrieve data using pagination to handle multiple pages of results.
2. **Read from a Local JSON File**: Provide an option to load data from a local JSON file instead of the API.
3. **Extract Specific Fields**: Parse the data to extract fields such as `title`, `subjects`, and `field_offices`.
4. **Format Data**: Reformat the extracted data into thorn-separated values for consistent output.
5. **Command-line Interface**: Use command-line arguments to allow users to specify whether to fetch data from the API or a file.

This project combines API interaction, file handling, JSON parsing, string manipulation, and command-line interface design to automate the extraction and formatting of relevant data in a structured manner.

## How to Install

To install the required dependencies, run the following command:

```bash
pipenv install -e .
```

## How to Run

To execute the program, use one of the following commands:

- **Fetch data from the FBI API (specify page number):**

  ```bash
  pipenv run python main.py --page <page_number>
  ```

- **Read data from a local JSON file:**

  ```bash
  pipenv run python main.py --file <path_to_json_file>
  ```

## Example(Video)

https://github.com/user-attachments/assets/212f3b61-2d20-48de-b0c9-80e28dc0df3e



## Functions

#### `main.py`

- **`fetch_data_from_api(page)`**: Fetches data from the FBI API for the specified page number.
  
  ```python
  def fetch_data_from_api(page):
      # Code to send a GET request to the FBI API and return the JSON data
  ```

- **`fetch_data_from_file(file_location)`**: Loads data from a local JSON file.

  ```python
  def fetch_data_from_file(file_location):
      # Code to open the file and load JSON data
  ```

- **`extract_and_format_data(data)`**: Extracts relevant fields (`title`, `subjects`, `field_offices`) and formats them into thorn-separated rows.

  ```python
  def extract_and_format_data(data):
      # Code to parse the data and format each entry
  ```

- **`print_to_stdout(formatted_data)`**: Outputs the formatted data to the console.

  ```python
  def print_to_stdout(formatted_data):
      # Code to print the data to standard output
  ```

- **`main(page=None, file_location=None)`**: Orchestrates data fetching and formatting based on input parameters.

  ```python
  def main(page=None, file_location=None):
      # Code to determine data source and process data
  ```


## Bugs and Assumptions

- **Assumptions**:
  - The FBI API endpoint and the structure of the returned JSON data remain consistent.
  - The local JSON file (if used) follows the same structure as the data returned by the FBI API.

- **Known Bugs**:
 -Some comma-separated names were initially missed, so I had to join them again using a comma to ensure all values were included.
