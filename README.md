# Convert-to-PDF

Automate the conversion of a group of files into PDF files.

## Features

Currently supports DOCX files via the [docx2pdf](https://github.com/AlJohri/docx2pdf) library, which requires Microsoft Word to be locally installed.

## Requirements

- Python (managed via [uv](https://github.com/astral-sh/uv))
- Microsoft Word (for DOCX conversion)

## Installation

1. Clone this repository
2. Install dependencies using uv:
   ```sh
   uv sync
   ```

## Usage

### Command Line

Convert all DOCX files in a folder:

```sh
uv run python main.py /path/to/folder
```

### Batch File

For Windows users, you can use the provided batch file for convenient conversion:

1. Copy [`convert_to_pdf_runner.bat`](convert_to_pdf_runner.bat) to the folder containing files you want to convert
2. Update the `PROJECT_PATH` variable in the batch file to point to your Convert-to-PDF installation
3. Run it

