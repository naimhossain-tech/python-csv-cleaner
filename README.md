# Python CSV & Excel Cleaner

A lightweight Python command-line tool for cleaning CSV and Excel files. It supports single-file cleaning and batch processing.

## Features

- Supports CSV (`.csv`) and Excel (`.xlsx`) files
- Trims leading and trailing whitespace
- Removes completely blank rows
- Removes duplicate records
- Validates column headers
- Rejects empty or duplicate header names
- Generates a cleaning summary for each file
- Supports custom output paths
- Processes multiple files in batch mode
- Includes automated unit tests
- Runs automated tests with GitHub Actions

## Requirements

- Python 3
- `openpyxl` for Excel support

## Installation

Clone the repository:

```bash
git clone https://github.com/naimhossain-tech/python-csv-cleaner.git
cd python-csv-cleaner
```

Install the dependency:

```bash
python -m pip install openpyxl
```

## Usage

### Clean a CSV file

```bash
python clean_csv.py input.csv
```

Specify a custom output file:

```bash
python clean_csv.py input.csv -o cleaned.csv
```

### Clean an Excel file

```bash
python clean_csv.py input.xlsx
```

Specify a custom output file:

```bash
python clean_csv.py input.xlsx -o cleaned.xlsx
```

### Batch processing

Place CSV and XLSX files directly inside a folder:

```bash
python batch_clean.py batch_demo
```

By default, cleaned files are saved in `batch_cleaned_output/`.

Choose a custom output directory:

```bash
python batch_clean.py batch_demo -o results
```

Batch processing checks files directly inside the specified folder, not its subfolders.

### View command help

```bash
python clean_csv.py --help
python batch_clean.py --help
```

## Example cleaning report

```text
FILE CLEANING REPORT
Status: SUCCESS
Total rows checked:    4
Blank rows removed:    1
Duplicate rows removed: 1
Total rows removed:    2
Rows kept:             2
Removal rate:          50.00%
```

This is an illustrative example. Actual results depend on the input data.

## Run automated tests

Compile the Python files:

```bash
python -m py_compile clean_csv.py batch_clean.py test_clean_csv.py test_batch_clean.py
```

Run all tests:

```bash
python -m unittest -v test_clean_csv test_batch_clean
```

## GitHub Actions

GitHub Actions automatically runs the configured tests when code is pushed to the `main` branch or a pull request targets `main`.

View workflow runs:

https://github.com/naimhossain-tech/python-csv-cleaner/actions

## Important notes

- Keep a backup of important source data.
- Review cleaned output before using it in production.
- Duplicate records are identified by comparing their cleaned cell values.
- Excel processing uses the applicable worksheet selected by the program.
- This tool cleans data; it does not verify the accuracy of the underlying information.
- No open-source license has been added. Contact the repository owner for licensing and reuse permission.

## Repository

https://github.com/naimhossain-tech/python-csv-cleaner
