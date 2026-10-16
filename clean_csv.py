import argparse
import csv
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Clean CSV files and remove blank or duplicate rows."
    )
    parser.add_argument("input", help="Path to the input CSV file")
    parser.add_argument(
        "-o", "--output",
        default="cleaned_output.csv",
        help="Output CSV path (default: cleaned_output.csv)"
    )
    args = parser.parse_args()

    source = Path(args.input)
    output = Path(args.output)

    if not source.is_file():
        print(f"Error: Input file not found: {source}")
        return 1

    try:
        if source.resolve() == output.resolve():
            print("Error: Input and output files must be different.")
            return 1

        with source.open(
            "r", newline="", encoding="utf-8-sig"
        ) as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: CSV header is missing.")
                return 1

            headers = [h.strip() for h in reader.fieldnames]

            if any(not h for h in headers):
                print("Error: Empty column names are not allowed.")
                return 1

            if len(set(headers)) != len(headers):
                print("Error: Duplicate column names after trimming.")
                return 1

            rows = []
            seen = set()
            total = 0
            blank_removed = 0
            duplicate_removed = 0

            for row in reader:
                total += 1

                if None in row:
                    print(
                        f"Error: Too many values on CSV line "
                        f"{reader.line_num}."
                    )
                    return 1

                cleaned = {
                    header: (
                        (row.get(original) or "").strip()
                    )
                    for original, header in zip(
                        reader.fieldnames, headers
                    )
                }

                if all(value == "" for value in cleaned.values()):
                    blank_removed += 1
                    continue

                key = tuple(cleaned[h] for h in headers)

                if key in seen:
                    duplicate_removed += 1
                    continue

                seen.add(key)
                rows.append(cleaned)

        output.parent.mkdir(parents=True, exist_ok=True)

        with output.open(
            "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file, fieldnames=headers
            )
            writer.writeheader()
            writer.writerows(rows)

        removed = blank_removed + duplicate_removed
        kept = len(rows)
        removal_rate = (removed / total * 100) if total else 0.0

        print("\n" + "=" * 36)
        print("         CSV CLEANING REPORT")
        print("=" * 36)
        print("Status:                SUCCESS")
        print(f"Input file:            {source}")
        print(f"Output file:           {output}")
        print("-" * 36)
        print(f"Total rows checked:    {total}")
        print(f"Blank rows removed:    {blank_removed}")
        print(f"Duplicate rows removed:{duplicate_removed:>5}")
        print(f"Total rows removed:    {removed}")
        print(f"Rows kept:             {kept}")
        print(f"Removal rate:          {removal_rate:.2f}%")
        print("=" * 36)
        return 0

    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Error: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
