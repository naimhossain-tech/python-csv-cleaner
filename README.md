Python CSV Cleaner

A lightweight Python command-line tool to clean CSV files by trimming whitespace, removing blank rows, and removing duplicate records.

Features

- Trims whitespace from column names and cell values
- Removes completely blank rows
- Removes duplicate records
- Reports rows read, removed, and kept
- Supports custom output file paths
- Handles common CSV and file errors
- Uses Python's built-in libraries only

Requirements

- Python 3.8 or newer
- No third-party packages required

Usage

Clean a CSV file

python clean_csv.py input.csv

Save the cleaned file to a specific location

python clean_csv.py input.csv -o output.csv

View available options

python clean_csv.py --help

Demo: Before and After

Run the example:

python clean_csv.py portfolio_demo.csv -o portfolio_demo_cleaned.csv

Cleaning Report

CSV Cleaning Report
-------------------
Rows read:              5
Blank rows removed:     1
Duplicate rows removed: 1
Rows kept:              3
Output saved to:        portfolio_demo_cleaned.csv

Cleaned Output

name,email,city
Rahim,rahim@example.com,Dhaka
Karim,karim@example.com,Chattogram
Nusrat,nusrat@example.com,Sylhet

How It Works

1. Reads the input CSV file.
2. Trims unnecessary whitespace.
3. Removes completely blank rows.
4. Removes duplicate records.
5. Saves the cleaned data to an output file.

Safety

Always review the cleaned output before using it for important work. Keep a backup of your original data.

License

This project is available for learning and practical CSV-cleaning tasks.
