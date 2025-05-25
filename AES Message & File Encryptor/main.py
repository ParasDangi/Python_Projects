from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import hashlib
import os

# Generate a consistent key from a password
def get_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Encrypt message with Fernet
def encrypt():
    password = code.get()
    if not password:
        messagebox.showerror("Encryption", "Password is required for encryption")
        return
    try:
        key = get_key(password)
        fernet = Fernet(key)

        message = text1.get(1.0, END).strip()
        if not message:
            messagebox.showerror("Encryption", "Enter a message to encrypt")
            return

        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        encrypted_message = fernet.encrypt(message.encode()).decode()

        Label(screen1, text="ENCRYPTED MESSAGE", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypted_message)
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {str(e)}")

# Decrypt message with Fernet
def decrypt():
    password = code.get()
    if not password:
        messagebox.showerror("Decryption", "Password is required for decryption")
        return
    try:
        key = get_key(password)
        fernet = Fernet(key)

        message = text1.get(1.0, END).strip()
        if not message:
            messagebox.showerror("Decryption", "Enter a message to decrypt")
            return

        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        decrypted_message = fernet.decrypt(message.encode()).decode()

        Label(screen2, text="DECRYPTED MESSAGE", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

# Encrypt a selected file
def encrypt_file():
    password = code.get()
    if not password:
        messagebox.showerror("File Encryption", "Password is required for file encryption")
        return
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        key = get_key(password)
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_path + ".enc", 'wb') as enc_file:
            enc_file.write(encrypted)
        messagebox.showinfo("Success", "File encrypted successfully")
    except Exception as e:
        messagebox.showerror("Error", f"File encryption failed: {str(e)}")

# Decrypt a selected file
def decrypt_file():
    password = code.get()
    if not password:
        messagebox.showerror("File Decryption", "Password is required for file decryption")
        return
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        key = get_key(password)
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)

        # Recover original extension
        if file_path.endswith(".enc"):
            original_ext = os.path.splitext(file_path[:-4])[1]  # get ext before .enc
            base_name = os.path.splitext(file_path)[0]
            save_path = base_name + "_decrypted" + original_ext
        else:
            save_path = file_path + "_decrypted"

        with open(save_path, 'wb') as dec_file:
            dec_file.write(decrypted)
        messagebox.showinfo("Success", f"File decrypted successfully: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"File decryption failed: {str(e)}")

# Reset inputs
def reset():
    code.set("")
    text1.delete(1.0, END)

# UI Setup
screen = Tk()
screen.geometry("600x500")
screen.title("AES Message & File Encryptor")
code = StringVar()
text1 = Text(font=("Robote", 15), bg="white", relief=GROOVE, wrap=WORD, bd=0)

Label(text="Enter text for encryption and decryption", fg="black", font=("Arial", 16)).place(x=10, y=10)
text1.place(x=10, y=50, width=570, height=100)
Label(text="Enter secret Key", fg="black", font=("Arial", 16)).place(x=10, y=170)
Entry(textvariable=code, width=30, bd=0, font=("Arial", 16), show="*").place(x=10, y=210)

Button(text="ENCRYPT MESSAGE", command=encrypt, height="2", width="25", bg="#ed3833", fg="white", bd=0).place(x=10, y=260)
Button(text="DECRYPT MESSAGE", command=decrypt, height="2", width="25", bg="#00bd56", fg="white", bd=0).place(x=300, y=260)
Button(text="ENCRYPT FILE", command=encrypt_file, height="2", width="25", bg="#8a2be2", fg="white", bd=0).place(x=10, y=320)
Button(text="DECRYPT FILE", command=decrypt_file, height="2", width="25", bg="#ff8c00", fg="white", bd=0).place(x=300, y=320)
Button(text="RESET", command=reset, height="2", width="60", bg='#1089ff', fg="white", bd=0).place(x=10, y=380)

screen.mainloop()