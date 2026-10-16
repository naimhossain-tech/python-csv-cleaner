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
## Demo: Before and After

This example demonstrates how the CSV Cleaner removes extra whitespace, blank rows, and duplicate records.

### Sample Command

```bash
python clean_csv.py portfolio_demo.csv -o portfolio_demo_cleaned.csv
```

### Cleaning Results

- Rows read: 5
- Blank rows removed: 1
- Duplicate rows removed: 1
- Rows kept: 3

### Cleaned Output

```csv
name,email,city
Rahim,rahim@example.com,Dhaka
Karim,karim@example.com,Chattogram
Nusrat,nusrat@example.com,Sylhet
```

### Features Demonstrated

- Trims whitespace from values
- Removes completely blank rows
- Removes duplicate records
- Saves cleaned data to a separate CSV file
