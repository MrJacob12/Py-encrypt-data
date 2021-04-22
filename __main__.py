from cryptography.fernet import Fernet
import glob, os

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_data_file(filepath,keyname):
    key = keyname
    f = Fernet(key)
    with open(filepath, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filepath, "wb") as file:
            file.write(encrypted_data)
            print("Successful encrypt data")

def decrypt_data_file(filepath,keyname):
    key = keyname
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)
        print("Successful decrypt data")

def encrypt_data(text,keyname):
    encoded_message = text.encode()
    f = Fernet(keyname)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_data(text,keyname):
    f = Fernet(keyname)
    decrypted_message = f.decrypt(text)
    return decrypted_message.decode()

