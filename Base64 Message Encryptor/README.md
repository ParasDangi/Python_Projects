# Python
There are several Projects available here..............
Each one are described one by one are as follow...

# Encryption.py
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
