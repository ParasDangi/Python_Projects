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
        screen1.resizable(False,False)

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
        screen2.resizable(False,False)

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
screen.geometry("590x680")
screen.title("AES Message & File Encryptor")
screen.resizable(False,False)
image_icon=PhotoImage(file="Image/icon.png")
screen.iconphoto(False,image_icon)
code = StringVar()

text1 = Text(font=("Robote", 15), bg="white", relief=GROOVE, wrap=WORD, bd=0)
text1.place(x=10, y=48, width=560, height=130)

Label(text="Enter text for encryption and decryption", fg="black", font=("Arial", 16)).place(x=10, y=10)

Label(text="Enter secret Key", fg="black", font=("Arial", 16)).place(x=10, y=180)
Entry(textvariable=code, width=30, bd=0, font=("Arial", 16), show="*").place(x=10, y=208)

encrypt_image=PhotoImage(file="Image/encrypt.png")
encrypt=Button(text="ENCRYPT MESSAGE", image=encrypt_image,command=encrypt,bd=0).place(x=10, y=260)

decrypt_image=PhotoImage(file="Image/decrypt.png")
decrypt=Button(image=decrypt_image,command=decrypt,bd=0).place(x=310, y=250)

encrypt_file_image=PhotoImage(file="Image/encrypt_file.png")
encrypt_file=Button( image=encrypt_file_image,command=encrypt_file,bd=0).place(x=10, y=400)

decrypt_file_image=PhotoImage(file="Image/decrypt_file.png")
decrypt_file=Button(image=decrypt_file_image, command=decrypt_file,bd=0).place(x=310, y=400)

Button(text="RESET", command=reset, height="2", width="60", bg='#1089ff', fg="white", bd=0).place(x=10, y=550)
screen.mainloop()