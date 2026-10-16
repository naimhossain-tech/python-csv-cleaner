# Python CSV Cleaner

A lightweight command-line tool for cleaning CSV files using Python built-in libraries.

## Features

- Trims leading and trailing whitespace from headers and values
- Removes completely blank rows
- Removes duplicate records
- Displays a cleaning summary
- Supports custom output file paths
- Requires no third-party Python packages

## Requirements

- Python 3.8 or newer
- A terminal or command prompt

## Getting Started

Clone the repository and enter the project directory:

    git clone https://github.com/naimhossain-tech/python-csv-cleaner.git
    cd python-csv-cleaner

## Usage

Clean a CSV file using the default output filename:

    python clean_csv.py input.csv

Specify an output filename:

    python clean_csv.py input.csv -o output.csv

Display command-line help:

    python clean_csv.py --help

## Example

Suppose the input CSV contains blank rows and duplicate records. Run:

    python clean_csv.py input.csv -o cleaned.csv

Example cleaning report:

    CSV Cleaning Report
    Rows read: 5
    Blank rows removed: 1
    Duplicate rows removed: 1
    Rows kept: 3
    Output saved to: cleaned.csv

The report above is an example. Actual counts depend on the input file.

## How It Works

1. Reads the input CSV file.
2. Cleans whitespace from headers and values.
3. Removes completely blank rows.
4. Removes duplicate records.
5. Writes the cleaned data to the output file.
6. Reports the cleaning results.

## Safety Notes

- Keep a backup of important source files.
- Review cleaned data before using it in production.
- Do not assume that duplicate rows always represent invalid data.

## License

No formal open-source license has been added yet. Contact the repository owner for licensing and reuse permission.
