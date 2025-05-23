# File Transfer Application
## Overview
This is a simple **file-sharing application** built using Python and Tkinter. It enables users to **send and receive files** over a network using **sockets**. The application provides a user-friendly graphical interface for easy file selection and transfer.

## Features
- **Send Files:** Share files from your local system with another device.
- **Receive Files:** Accept files from a sender over the network.
- **Network-Based Communication:** Uses socket programming for seamless data transmission.
- **Graphical User Interface:** Built with Tkinter for an intuitive experience.
- **File Selection Dialog:** Choose files effortlessly for sending.
- **User Authentication:** Uses system hostname as a unique identifier for connections.

## Requirements
- **Python 3.x**
- Required Libraries:
  - `tkinter` (built-in with Python)
  - `socket` (built-in with Python)
  - `os` (built-in with Python)
  - `subprocess` (built-in with Python)

## Installation
No special installation is required. Just run the Python script.

## Usage
1. **Launch the application.**
2. **Send Files:**
   - Click the **"Send"** button.
   - Select a file using the file dialog.
   - Click **"SEND"** to transmit the file.
3. **Receive Files:**
   - Click the **"Receive"** button.
   - Enter the **Sender ID** (hostname).
   - Specify the filename for the incoming file.
   - Click **"Receive"** to retrieve the file.

## Code Structure
- `Send()`: Opens a new window to handle file transmission.
  - `select_file()`: Allows users to pick a file.
  - `Sender()`: Sends the selected file to the recipient.
- `Receive()`: Opens a new window for receiving files.
  - `receiver()`: Connects to the sender and downloads the file.
- Tkinter GUI components enhance usability.

## Notes
- Ensure **both sender and receiver are running the application** for successful file sharing.
- File transfer relies on **local network connectivity**.
- Currently supports **text files (`.txt`)** but can be modified for other formats.

## Future Improvements
- Expand file format support beyond `.txt`.
- Add **progress indicators** for file transfers.
- Improve security with **encryption** for transmitted data.

Enjoy fast and simple file sharing with this application! 🚀
