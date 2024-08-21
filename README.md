# Password Manager

A simple yet secure password manager built with Python. This tool allows you to store, retrieve, and generate strong passwords, all while ensuring that your data is encrypted for maximum security.

## Features

- **Store Passwords**: Save your passwords securely with associated usernames and website names.
- **Retrieve Passwords**: Easily search for and retrieve stored passwords by the website name.
- **Generate Strong Passwords**: Automatically generate strong, random passwords with a mix of letters, numbers, and special characters.
- **Encryption**: All passwords are encrypted using the `cryptography` library before being stored.

## Prerequisites

- Python 3.x
- `cryptography` library

You can install the required library using pip:

```bash
pip install cryptography
```

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```

2. **Run the Program**:

   Execute the following command in your terminal:

   ```bash
   python password_manager.py
   ```

3. **Options**:
   - **Add a New Password**: Enter the website name, username, and password. If you leave the password blank, a strong random password will be generated for you.
   - **Retrieve a Password**: Enter the website name to retrieve the stored username and password.
   - **Generate a Strong Password**: Generate a random password of your desired length.
   - **Exit**: Close the program.

## Security

This password manager uses the `Fernet` symmetric encryption from the `cryptography` library to ensure that all stored passwords are encrypted. The encryption key is generated once and stored in the `key.key` file. Ensure this key file is stored securely, as it is required to decrypt your passwords.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software as you see fit.
```
