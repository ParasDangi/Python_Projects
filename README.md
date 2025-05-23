# Python Utility Projects

## Overview
This repository contains multiple Python-based utility projects designed to enhance automation and efficiency in various domains, including **encryption**, **report generation**, and **file transfer**. Each project features a simple yet effective graphical user interface built with Tkinter.

## Included Projects
1. **Message Encryption & Decryption**
   - A basic encryption tool using base64 encoding.
   - Allows users to encode and decode messages with a secret key.
   
2. **Candidate Report Generator**
   - Generates candidate reports using SQLite database data.
   - Fills a Word template and converts to PDF format.
   - Supports multi-threaded report generation.

3. **File Transfer Application**
   - Enables sending and receiving files over a local network.
   - Uses socket programming for direct communication.
   - Provides an easy-to-use interface for quick sharing.

## Common Features
- **User-Friendly GUI:** Built with Tkinter for ease of use.
- **Automation & Efficiency:** Streamlines common tasks such as encryption, reporting, and file transfer.
- **Python-Based Solutions:** Portable and lightweight applications.
- **Networking & Database Integration:** Uses sockets and SQLite for data handling.

## Setup & Requirements
- Python 3.x
- Required dependencies (install via `pip`):
  - `python-docx`, `pywin32` (for report generation)
  - `socket`, `sqlite3`, `base64`, `os`, `tkinter` (built-in modules)
- Ensure necessary files (`template.docx`, `database.db`) exist for respective projects.

## Future Enhancements
- Improve encryption security with stronger algorithms.
- Enhance report formatting and customization options.
- Add progress tracking and encryption for file transfers.

This repository provides simple yet effective Python utilities for various tasks, making automation accessible and efficient. 🚀
