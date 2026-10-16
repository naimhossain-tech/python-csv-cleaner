import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("clean_csv.py")

class TestCSVCleaner(unittest.TestCase):
    def run_cleaner(self, source, output):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(source), "-o", str(output)],
            capture_output=True, text=True
        )

    def test_clean_blank_duplicate_and_whitespace(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "input.csv"
            out = Path(tmp) / "output.csv"
            src.write_text("name,email\n Rahim , rahim@example.com \n\nRahim,rahim@example.com\nKarim,karim@example.com\n", encoding="utf-8")
            result = self.run_cleaner(src, out)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with out.open(newline="", encoding="utf-8") as f:
                rows = list(csv.reader(f))
            self.assertEqual(rows, [["name", "email"], ["Rahim", "rahim@example.com"], ["Karim", "karim@example.com"]])
            self.assertIn("Blank rows removed:", result.stdout)
            self.assertIn("Duplicate rows removed:", result.stdout)

    def test_missing_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "missing.csv"
            result = self.run_cleaner(src, Path(tmp) / "out.csv")
            self.assertEqual(result.returncode, 1)
            self.assertIn("Input file not found", result.stdout)

    def test_same_input_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "input.csv"
            original = "name\nRahim\n"
            src.write_text(original, encoding="utf-8")
            result = self.run_cleaner(src, src)
            self.assertEqual(result.returncode, 1)
            self.assertIn("must be different", result.stdout)
            self.assertEqual(src.read_text(encoding="utf-8"), original)

    def test_duplicate_headers_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "input.csv"
            src.write_text("name, name\nRahim,Karim\n", encoding="utf-8")
            result = self.run_cleaner(src, Path(tmp) / "out.csv")
            self.assertEqual(result.returncode, 1)
            self.assertIn("Duplicate column names", result.stdout)

if __name__ == "__main__":
    unittest.main(verbosity=2)
