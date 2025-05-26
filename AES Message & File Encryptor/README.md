# AES Message & File Encryptor

## Overview
This application provides **secure encryption and decryption** of messages and files using **AES encryption (via Fernet)**. It allows users to **encrypt text or files with a password**, ensuring confidentiality.

## Features
- **Encrypt & Decrypt Messages:** Uses AES-based encryption to protect text data.
- **Encrypt & Decrypt Files:** Supports file encryption with `.enc` extension for security.
- **Password-Based Security:** Converts user-entered passwords into encryption keys.
- **User-Friendly GUI:** Built with Tkinter for easy access and usability.
- **File Selection Support:** Uses a file dialog to select files for encryption.

## Requirements
- Python 3.x
- Required libraries:
  - `cryptography` (install via `pip install cryptography`)
  - `tkinter`, `base64`, `hashlib`, `os` (standard Python modules)

## Installation
1. Install the required dependencies using:
   ```sh
   pip install cryptography
   ```
2. Run the Python script to start the encryption tool.

## Usage
1. **Enter text** in the message field for encryption/decryption.
2. **Enter a secret key** (password) for secure encryption.
3. Choose an option:
   - **Encrypt Message**: Converts text into an encrypted format.
   - **Decrypt Message**: Restores encrypted text.
   - **Encrypt File**: Select a file to secure with encryption.
   - **Decrypt File**: Restore an encrypted file using the same password.
   - **Reset**: Clears all inputs for fresh entry.

## Code Structure
- `get_key()`: Converts passwords into a secure key using SHA-256 hashing.
- `encrypt()`: Encrypts user input messages.
- `decrypt()`: Decrypts encrypted messages.
- `encrypt_file()`: Encrypts selected files using AES encryption.
- `decrypt_file()`: Decrypts files using the corresponding password.
- Tkinter GUI enables simple user interaction.

## Notes
- Files encrypted will have a `.enc` extension.
- Ensure **correct password** is used for decryption.
- AES encryption provides **strong security**, but keep your password safe.

## Future Improvements
- Add **progress indicators** for file encryption.
- Enhance file support for multiple formats.
- Implement cloud integration for secure storage.

This application provides a **simple yet powerful** encryption solution for text and files, making data security more accessible. 🚀
