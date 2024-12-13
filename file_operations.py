
from tkinter import filedialog, simpledialog
import subprocess
from encryptor import encrypt_file, decrypt_file
from face_capture import capture_user_face
from face_auth import authenticate_user

FILES_DIR = "Secured_Files"

def create_secure_file():
    username = simpledialog.askstring("Username", "Enter your username:")
    if not username or not capture_user_face(username):
        print("[ERROR] File creation cancelled.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "w") as f:
        f.write("")
    subprocess.run(["notepad", file_path])
    encrypt_file(file_path)

def open_secure_file():
    file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
    if not file_path or not authenticate_user():
        print("[ERROR] Authentication failed.")
        return

    decrypt_file(file_path)
    subprocess.run(["notepad", file_path])
    encrypt_file(file_path)
