from cryptography.fernet import Fernet
import glob, os

def generate_key(file):
    key = Fernet.generate_key()
    file += ".key"
    with open(file,"wb") as key_file:
        key_file.write(key)

def encrypt_data(filename,keyname):
    wxs = "key/"
    wxs += keyname
    wxs += ".key"
    key = open(wxs,"rb").read()
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
            print("Successful encrypt data")

def decrypt_data(filename,keyname):
    wxs = "key/"
    wxs += keyname
    wxs += ".key"
    key = open(wxs,"rb").read()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
        print("Successful decrypt data")


while True:
    print("List of your keys: ")
    for file in os.listdir("key/"):
        if file.endswith(".key"):
            print(file)
    try:
        menu = input("\nEncrypt data [E] Decrypt data [D] Generate new key [K]\n")
        if menu.lower() == "e":
            print("Encrypt data \n")
            filename = input("File path: ")
            keyname = input("Key name: ")
            encrypt_data(filename,keyname)
        elif menu.lower() == "d":
            print("Decrypt data \n")
            filename = input("File path: ")
            keyname = input("Key name: ")
            decrypt_data(filename,keyname)
        elif menu.lower() == "k":
            filename = input("Filename: ")
            generate_key(filename)
    except:
        print("Something went wrong")