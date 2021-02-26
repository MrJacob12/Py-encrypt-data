from cryptography.fernet import Fernet
import glob, os

def generate_key():
    key = Fernet.generate_key()
    print(key)

def encrypt_data(filename,keyname):
    key = keyname
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
            print("Successful encrypt data")

def decrypt_data(filename,keyname):
    key = keyname
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
        print("Successful decrypt data")


