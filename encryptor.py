
from cryptography.fernet import Fernet
import os

DATA_DIR = "User_Data"
KEY_FILE = os.path.join(DATA_DIR, "filekey.key")
os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as key_file:
    ENCRYPTION_KEY = key_file.read()

cipher = Fernet(ENCRYPTION_KEY)

def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
