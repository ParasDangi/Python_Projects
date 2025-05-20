# Python
There are several Projects available here..............
Each one are described one by one are as follow...

# 1.Encryption.py
## Overview
This is a simple encryption and decryption tool built using Python and the Tkinter library. It allows users to encrypt and decrypt text messages using a base64 encoding method. The user must enter a secret key (`1234`) to perform these operations. 

## Features
- **Encrypt Text:** Convert plain text into base64-encoded format.
- **Decrypt Text:** Convert base64-encoded text back into readable plain text.
- **Password Protection:** Encryption and decryption require a secret key.
- **Reset Function:** Clears input fields for a fresh start.
- **User-Friendly Interface:** Simple GUI created with Tkinter.

## Requirements
- Python 3.x
- Tkinter (built-in with Python)
- `base64` module (standard Python library)

## Installation
No installation required. Simply run the Python script.

## Usage
1. **Enter the text** you want to encrypt or decrypt in the text input field.
2. **Enter the secret key** (`1234`) in the password field.
3. Click:
   - **Encrypt** to encode the text.
   - **Decrypt** to decode the text.
   - **Reset** to clear all input fields.

## Code Structure
- `encrypt()`: Encrypts user-entered text using base64 encoding.
- `decrypt()`: Decrypts text back into readable format.
- `reset()`: Clears the input fields.
- Tkinter GUI components handle user interaction.

## Notes
- This script uses basic base64 encoding, which is **not a secure** encryption method for sensitive data.
- The secret key is hardcoded as `"1234"`, which makes it vulnerable to unauthorized access.

## Future Improvements
- Allow users to set their own encryption key dynamically.
- Implement stronger encryption algorithms such as AES for better security.
- Improve the UI for enhanced user experience.

Enjoy encrypting and decrypting your messages with this simple tool! 🚀
**Encryption & Decryption Tool 🔒**
A Tkinter-based Python GUI for securely encrypting and decrypting messages using Base64 encoding. Users enter a secret key to encrypt or decrypt text, ensuring data security.

**Tech Used 🛠**
➡️Tkinter (GUI)
➡️Base64 Encoding (Encryption)
➡️Messagebox (Alerts & Errors)

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
