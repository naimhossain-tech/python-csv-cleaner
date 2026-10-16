import csv
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python clean_csv.py input.csv")
    sys.exit(1)

source = Path(sys.argv[1])
output = Path("cleaned_output.csv")

if not source.is_file():
    print(f"Error: File not found: {source}")
    sys.exit(1)

try:
    with source.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("Error: CSV header is missing.")
            sys.exit(1)

        headers = [h.strip() for h in reader.fieldnames]

        if len(set(headers)) != len(headers):
            print("Error: Duplicate column names after trimming.")
            sys.exit(1)

        rows = []
        for row in reader:
            cleaned = {}
            for key, value in row.items():
                cleaned[key.strip()] = (
                    value.strip() if value is not None else ""
                )
            rows.append(cleaned)

    with output.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Success: {len(rows)} rows processed.")
    print(f"Output saved to: {output}")

except (OSError, UnicodeError, csv.Error) as error:
    print(f"Error: {error}")
    sys.exit(1)
