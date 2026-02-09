"""Batch convert files in a folder to PDFs."""
import argparse
import sys
from pathlib import Path

from docx2pdf import convert


def convert_docx_to_pdf(file_path: Path) -> None:
    """Convert a DOCX file to PDF."""
    print(f"Converting DOCX to PDF: {file_path}")
    output_path = file_path.with_suffix(".pdf")
    convert(str(file_path), output_path)


def process_folder(folder_path: Path) -> None:
    """Process all files in a folder."""
    print(f"Processing folder: {folder_path}")
    docx_files = [path for path in folder_path.glob("*.docx")]  # noqa: C416
    print(f"Found {len(docx_files)} DOCX files to convert.")
    for docx_file in docx_files:
        convert_docx_to_pdf(docx_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Batch convert files into PDFs",
    )
    parser.add_argument(
        "folder",
        help="Path for files to be converted",
    )

    args = parser.parse_args()
    if not args.folder:
        print("Error: Folder path is required.")
        parser.print_help()
        sys.exit(1)

    folder_path = Path(args.folder)

    # Process the folder
    process_folder(folder_path)
