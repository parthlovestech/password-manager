import os
import getpass
from cryptography.fernet import Fernet
import random
import string

# Generate or load the encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Encrypt and decrypt password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Generate a random strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(length))
    return random_password

# Save password
def save_password(website, username, password, key):
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as f:
        f.write(f"{website} | {username} | {encrypted_password.decode()}\n")

# Retrieve password
def retrieve_password(website, key):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip().split(" | ")
            if data[0] == website:
                username = data[1]
                encrypted_password = data[2].encode()
                decrypted_password = decrypt_password(encrypted_password, key)
                return f"Username: {username}, Password: {decrypted_password}"
    return "Website not found."

# Main program
def main():
    # Generate key if it doesn't exist
    if not os.path.exists("key.key"):
        generate_key()

    key = load_key()

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Generate a strong password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website name: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password (leave blank to generate a strong one): ")
            if not password:
                password = generate_password()
                print(f"Generated password: {password}")
            save_password(website, username, password, key)
            print("Password saved!")

        elif choice == "2":
            website = input("Enter website name to retrieve: ")
            result = retrieve_password(website, key)
            print(result)

        elif choice == "3":
            length = int(input("Enter the desired password length: "))
            print(f"Generated password: {generate_password(length)}")

        elif choice == "4":
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
