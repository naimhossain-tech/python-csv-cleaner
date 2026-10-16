import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("clean_csv.py")
SUPPORTED = {".csv", ".xlsx"}


def main():
    parser = argparse.ArgumentParser(
        description="Clean all CSV and Excel files in a folder."
    )
    parser.add_argument("folder", help="Folder containing input files")
    parser.add_argument(
        "-o", "--output-dir",
        default="batch_cleaned_output",
        help="Folder for cleaned files (default: batch_cleaned_output)"
    )
    args = parser.parse_args()

    source_dir = Path(args.folder)
    output_dir = Path(args.output_dir)

    if not source_dir.is_dir():
        print(f"Error: Input folder not found: {source_dir}")
        return 1

    try:
        source_dir = source_dir.resolve()
        output_dir = output_dir.resolve()

        if output_dir == source_dir:
            print("Error: Output folder must differ from input folder.")
            return 1

        # Collect files before processing to avoid picking up new outputs.
        files = sorted(
            p for p in source_dir.iterdir()
            if p.is_file() and p.suffix.lower() in SUPPORTED
        )

        if not files:
            print("No CSV or XLSX files found.")
            return 1

        output_dir.mkdir(parents=True, exist_ok=True)

        succeeded = 0
        failed = 0

        print(f"Files found: {len(files)}")

        for source in files:
            output = output_dir / f"cleaned_{source.name}"

            print(f"\nProcessing: {source.name}")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(source),
                    "-o",
                    str(output),
                ],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                succeeded += 1
                print("Result: SUCCESS")
                print(f"Output: {output}")
            else:
                failed += 1
                print("Result: FAILED")
                message = (result.stdout + result.stderr).strip()
                print(message or "Unknown error")

        print("\n" + "=" * 36)
        print("         BATCH SUMMARY")
        print("=" * 36)
        print(f"Files found:    {len(files)}")
        print(f"Successful:     {succeeded}")
        print(f"Failed:         {failed}")
        print(f"Output folder:  {output_dir}")
        print("=" * 36)

        return 1 if failed else 0

    except OSError as error:
        print(f"Error: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
