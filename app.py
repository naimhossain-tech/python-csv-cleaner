import csv
import uuid
import zipfile
from pathlib import Path

import openpyxl
from flask import Flask, render_template, request, send_from_directory, abort
from werkzeug.utils import secure_filename

from clean_csv import clean_csv, clean_excel

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "web_output"

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {".csv", ".xlsx"}


def save_cleaned_file(output_path, extension, headers, rows):
    if extension == ".csv":
        with output_path.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)
    else:
        workbook = openpyxl.Workbook()
        try:
            sheet = workbook.active
            sheet.append(headers)
            for row in rows:
                sheet.append(row)
            workbook.save(output_path)
        finally:
            workbook.close()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        uploaded = request.files.get("file")

        if not uploaded or not uploaded.filename:
            error = "Please select a CSV or Excel file."
        else:
            safe_name = secure_filename(uploaded.filename)
            extension = Path(safe_name).suffix.lower()

            if not safe_name or extension not in ALLOWED_EXTENSIONS:
                error = "Only CSV (.csv) and Excel (.xlsx) files are allowed."
            else:
                unique_id = uuid.uuid4().hex
                input_path = UPLOAD_DIR / f"{unique_id}{extension}"
                output_name = f"cleaned_{unique_id}{extension}"
                output_path = OUTPUT_DIR / output_name

                try:
                    uploaded.save(input_path)

                    if extension == ".csv":
                        headers, rows, total, blank, duplicates = clean_csv(input_path)
                    else:
                        headers, rows, total, blank, duplicates = clean_excel(input_path)

                    save_cleaned_file(output_path, extension, headers, rows)

                    removed = blank + duplicates
                    result = {
                        "original_name": safe_name,
                        "output_name": output_name,
                        "total": total,
                        "blank": blank,
                        "duplicates": duplicates,
                        "removed": removed,
                        "kept": len(rows),
                        "rate": (removed / total * 100) if total else 0,
                    }

                except (
                    OSError,
                    UnicodeError,
                    csv.Error,
                    ValueError,
                    TypeError,
                    zipfile.BadZipFile,
                    openpyxl.utils.exceptions.InvalidFileException,
                ):
                    error = "The file could not be processed. Check that it is a valid CSV or XLSX file."
                    if output_path.exists():
                        output_path.unlink()

                finally:
                    input_path.unlink(missing_ok=True)

    return render_template("index.html", result=result, error=error)


@app.route("/download/<filename>")
def download_file(filename):
    if not filename.startswith("cleaned_"):
        abort(404)

    if Path(filename).suffix.lower() not in ALLOWED_EXTENSIONS:
        abort(404)

    if not (OUTPUT_DIR / filename).is_file():
        abort(404)

    return send_from_directory(
        OUTPUT_DIR,
        filename,
        as_attachment=True,
        download_name=filename,
    )


@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        result=None,
        error="File is too large. The maximum upload size is 10 MB.",
    ), 413


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
