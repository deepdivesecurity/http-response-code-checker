# http-response-code-checker
This repo contains the script which take an Excel file of URLs and obtains the HTTP response code from each
# URL Response Code Checker

This Python script checks the HTTP status codes of URLs listed in an Excel file and outputs the results to a new Excel file. It helps automate the process of verifying the health of links.

---

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

---

## Project Description

This Python script reads URLs from an Excel file, checks each URL's HTTP response code, and writes the results to another Excel file. It leverages the `requests` library to check the status codes and uses `pandas` for reading and writing Excel files.

---

## Installation

### Requirements

- Python 3.7 or higher
- pandas
- requests
- openpyxl
- click

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/url-response-checker.git
   cd url-response-checker
   ```

2. Create the virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Usage
    ```bash
    python url_response_checker.py
    ```
The script will prompt you to select an input Excel file containing the URLs and specify an output file where the results will be saved.

## Features
- Reads URLs from Excel files
- Checks the HTTP status code for each URL
- Saves the results in a new Excel file with response codes
- Supports .xlsx file formats

