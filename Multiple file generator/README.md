# 2.generate_report_gui.py

## Overview
This Python-based application generates candidate reports by extracting information from an SQLite database, filling a Word document template, and converting it into a PDF. It provides a user-friendly GUI using Tkinter.

## Features
- **Automated Report Generation:** Extracts candidate details from a database and generates personalized reports.
- **Flexible Output Formats:** Supports both DOCX (Word document) and PDF formats.
- **Batch Processing:** Allows multiple reports to be generated at once.
- **Automatic File Opening:** Optionally opens the first generated report after completion.
- **Multi-threading Support:** Runs report generation in the background for better responsiveness.
- **Simple and Intuitive UI:** Easy-to-use interface with input fields and selection options.

## Requirements
- Python 3.x
- Required libraries:
  - `sqlite3` (standard Python library)
  - `docx` (install using `pip install python-docx`)
  - `tkinter` (built-in with Python)
  - `pywin32` (install using `pip install pywin32` for PDF conversion)

## Installation
1. Install the required dependencies using:
   ```sh
   pip install python-docx pywin32
   ```
2. Ensure an SQLite database (`database.db`) exists with a `candidates` table containing `id`, `name`, `email`, `score`, and `DOB`.
3. Place a Word template (`template.docx`) with placeholders `{name}`, `{email}`, `{score}`, `{DOB}`.

## Usage
1. **Enter candidate ID(s)** (comma-separated) in the input field.
2. **Select the output format**:
   - **PDF** (default) or **DOCX**.
3. **Enable "Open first file" option** if needed.
4. **Click "Generate Report(s)"** to start the process.

## Code Structure
- `fill_word_template()`: Fills the Word template with database data.
- `convert_multiple_docx_to_pdf()`: Converts generated DOCX files to PDF using Microsoft Word automation.
- `generate_reports_worker()`: Fetches candidate data and handles report generation.
- `post_generation_feedback()`: Displays success/failure messages and opens the first file if requested.
- `start_report_generation()`: Parses user input and triggers background processing.
- Tkinter GUI elements provide interactive input and controls.

## Notes
- The script **requires Microsoft Word** for DOCX-to-PDF conversion on Windows.
- Database **must exist** with candidate details before running.
- Ensure **template.docx** is correctly formatted with placeholder fields.
- Multi-threading improves responsiveness but requires handling exceptions properly.

## Future Improvements
- Add dynamic template selection for custom reports.
- Implement advanced formatting for the generated documents.
- Enhance security with encrypted database access.

Enjoy generating reports effortlessly with this automated tool! 🚀

**Tech Used 🛠**
➡️Python-docx (Word processing)
➡️win32com (PDF conversion)
➡️Tkinter (GUI framework)