import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import openpyxl

SCRIPT = Path(__file__).with_name("batch_clean.py")


class TestBatchCleaner(unittest.TestCase):
    def run_batch(self, folder, output):
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(folder),
                "-o",
                str(output),
            ],
            capture_output=True,
            text=True,
        )

    def test_batch_csv_and_excel(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "input"
            output = root / "output"
            source.mkdir()

            # Create a CSV containing a duplicate row.
            csv_file = source / "people.csv"
            csv_file.write_text(
                "name,email\n"
                " Rahim ,rahim@example.com\n"
                "Rahim,rahim@example.com\n"
                "Karim,karim@example.com\n",
                encoding="utf-8",
            )

            # Create an Excel file.
            xlsx_file = source / "people.xlsx"
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Name", "Email"])
            sheet.append([" Karim ", "karim@example.com"])
            sheet.append(["Naim", "naim@example.com"])
            workbook.save(xlsx_file)
            workbook.close()

            result = self.run_batch(source, output)

            self.assertEqual(
                result.returncode, 0,
                result.stdout + result.stderr,
            )
            self.assertIn("Successful:     2", result.stdout)
            self.assertIn("Failed:         0", result.stdout)

            # Verify cleaned CSV output.
            with (output / "cleaned_people.csv").open(
                newline="", encoding="utf-8"
            ) as file:
                rows = list(csv.reader(file))

            self.assertEqual(
                rows,
                [
                    ["name", "email"],
                    ["Rahim", "rahim@example.com"],
                    ["Karim", "karim@example.com"],
                ],
            )

            # Verify cleaned Excel output.
            workbook = openpyxl.load_workbook(
                output / "cleaned_people.xlsx",
                read_only=True,
                data_only=True,
            )
            try:
                rows = list(workbook.active.values)
            finally:
                workbook.close()

            self.assertEqual(
                rows,
                [
                    ("Name", "Email"),
                    ("Karim", "karim@example.com"),
                    ("Naim", "naim@example.com"),
                ],
            )

    def test_missing_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = self.run_batch(
                root / "missing",
                root / "output",
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("Input folder not found", result.stdout)

    def test_empty_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "input"
            source.mkdir()

            result = self.run_batch(source, root / "output")

            self.assertEqual(result.returncode, 1)
            self.assertIn("No CSV or XLSX files found", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
