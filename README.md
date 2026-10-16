# Python CSV Cleaner

A lightweight Python tool to clean CSV files by trimming whitespace,
removing blank rows, and removing duplicate records.

## Features

- Trims whitespace from column names and cell values
- Removes completely blank rows
- Removes duplicate records
- Reports rows processed, removed, and kept
- Supports custom output paths
- Handles common file and CSV errors
- Uses Python's built-in libraries

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Usage

Clean a CSV file:

```bash
python clean_csv.py input.csv
python clean_csv.py input.csv -o output/cleaned.csv
python clean_csv.py --help
CSV Cleaning Report
-------------------
Rows read:             4
Blank rows removed:    1
Duplicate rows removed:    1
Rows kept:             2
Output saved to:       demo_cleaned.csv

## ধাপ ২: ব্যক্তিগত ও অপ্রয়োজনীয় ফাইল সুরক্ষিত রাখুন

একটি `.gitignore` তৈরি করুন:

```bash
cat > .gitignore <<'EOF'
.venv/
__pycache__/
*.pyc
*.backup
input.csv
cleaned_output.csv
demo.csv
demo_cleaned.csv
