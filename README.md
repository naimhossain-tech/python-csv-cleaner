# Python CSV Cleaner

A simple Python command-line tool for cleaning CSV files.

## Features

- Trims whitespace from headers and values
- Removes completely blank rows
- Removes duplicate records
- Reports cleaning results
- Supports custom output paths
- Uses Python built-in libraries

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Usage

```bash
python clean_csv.py input.csv
```

```bash
python clean_csv.py input.csv -o output.csv
```

```bash
python clean_csv.py --help
```

## Demo Results

```text
Rows read: 5
Blank rows removed: 1
Duplicate rows removed: 1
Rows kept: 3
```

## How It Works

1. Reads the input CSV file.
2. Trims unnecessary whitespace.
3. Removes blank rows.
4. Removes duplicate records.
5. Saves the cleaned output.

## Safety

Keep a backup of your original file and review the output before using it.

## License

Available for learning and practical CSV-cleaning tasks.
