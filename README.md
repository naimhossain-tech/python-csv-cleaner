# Python CSV & Excel Cleaner

A lightweight Python command-line tool to clean CSV and Excel files by trimming whitespace, removing blank rows, and eliminating duplicate records. Supports single-file and batch processing.

## Features

- Supports CSV (`.csv`) and Excel (`.xlsx`) files
- Trims leading and trailing whitespace
- Removes completely blank rows
- Removes duplicate records
- Validates column headers and rejects duplicate header names
- Generates a cleaning summary for each file
- Supports custom output paths
- Processes multiple CSV and Excel files in one command
- Includes automated unit tests

## Requirements

- Python 3
- `openpyxl` for Excel file support

## Installation

Clone the repository:

```bash
git clone https://github.com/naimhossain-tech/python-csv-cleaner.git
cd python-csv-cleaner
```

Install the required dependency:

```bash
python -m pip install openpyxl
```

## Usage

### Clean a CSV file

```bash
python clean_csv.py input.csv
```

By default, the output is saved as `cleaned_output.csv`.

Specify an output file:

```bash
python clean_csv.py input.csv -o cleaned.csv
```

### Clean an Excel file

```bash
python clean_csv.py input.xlsx
```

Specify an output file:

```bash
python clean_csv.py input.xlsx -o cleaned.xlsx
```

### Batch processing

Place your CSV and XLSX files in a folder, then run:

```bash
python batch_clean.py batch_demo
```

By default, cleaned files are saved in `batch_cleaned_output/` with the prefix `cleaned_`.

Choose a custom output directory:

```bash
python batch_clean.py batch_demo -o results
```

Batch processing checks files directly inside the specified folder, not its subfolders.

### View help

```bash
python clean_csv.py --help
python batch_clean.py --help
```

## Example report

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

The example is illustrative. Actual results depend on the input data.

## Run tests

Run the automated tests with:

```bash
python -m py_compile clean_csv.py batch_clean.py
python -m unittest -v test_clean_csv
```

## Important notes

- Always keep a backup of important source data.
- Review cleaned output before using it in production.
- Duplicate records are identified by comparing their cleaned cell values.
- CSV and Excel files are processed using the first worksheet or active worksheet, respectively, for Excel input.
- The cleaner is intended for data cleanup, not for verifying the accuracy of the data.
- No formal open-source license has been added. Contact the repository owner for licensing and reuse permission.

## Repository

https://github.com/naimhossain-tech/python-csv-cleaner
