import unittest
from pathlib import Path
from unittest.mock import patch
import tempfile
import app as web_app

class TestDownloadSecurity(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp.name)
        self.patch = patch.object(web_app, "OUTPUT_DIR", Path(self.temp.name))
        self.patch.start()
        web_app.app.config["TESTING"] = True
        self.client = web_app.app.test_client()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def test_valid_cleaned_csv_download(self):
        path = self.output_dir / "cleaned_test.csv"
        path.write_text("Name,City\nNaim,Dhaka\n", encoding="utf-8")
        response = self.client.get("/download/cleaned_test.csv")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Name,City", response.data)
        self.assertIn("attachment", response.headers.get("Content-Disposition", ""))
        response.close()

    def test_missing_file(self):
        response = self.client.get("/download/cleaned_missing.csv")
        self.assertEqual(response.status_code, 404)

    def test_wrong_extension(self):
        response = self.client.get("/download/cleaned_test.txt")
        self.assertEqual(response.status_code, 404)

    def test_unapproved_filename(self):
        response = self.client.get("/download/report.csv")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
