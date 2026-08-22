# 🔐 Terminal Password Manager

A terminal-based password manager built with Python as a CS50 final project.
Store, retrieve, edit and delete your service credentials securely using Fernet encryption and SHA256 hashing.

---

## 🛠️ Technologies Used

- **Python** — core language
- **SQLite3** — local database for storing credentials
- **Fernet (cryptography library)** — encryption/decryption of stored passwords
- **SHA256 + Base64 (hashlib)** — one-way hashing for the master password

---

## 📁 Project Structure

```
project/
│
├── Main.py          # Entry point — handles master password login
├── queries.py       # All database operations (add, edit, delete, select)
├── user_choice.py   # User menu and input handling
└── Manager.db       # SQLite database (created automatically on first run)
```

---

## ⚙️ How to Run

### Requirements
Install the required library:
```bash
pip install cryptography
```

### Important — Database Path
Make sure all files are in the **same folder** before running.
The program looks for `Manager.db` in the current directory.

### Run the program
```bash
python Main.py
```

---

## 🔑 Master Password

The default master password is:
```
Password
```

> **To change the master password:**
> 1. From the main menu choose `Edit`
> 2. Enter `Main` as the service you want to change
> 3. For Email/Username enter anything (e.g. `admin`)
> 4. Enter your new password
> 5. Done! Your new password is now active

---

## 📋 Features

- **Login system** with master password protection
- **5 attempt limit** — locked out for 30 seconds after 5 wrong attempts
- **Add** new service credentials (service name, email/username, password)
- **Check** saved credentials for any service
- **Edit** existing credentials or change master password
- **Delete** any saved service
- **Fernet encryption** for all stored passwords
- **SHA256 hashing** for master password — never stored in plain text

---

## 🔒 Security Notes

- All stored passwords are **Fernet encrypted** (AES-128-CBC under the hood)
- The master password is **hashed with SHA256** — cannot be recovered if forgotten
- The Fernet encryption key is hardcoded in `queries.py` — for a production app this should be stored securely or derived from the master password
- Base64 encoding is used as a pre-processing step before hashing the master password

---

## 🚀 Usage Example

```
Add
Edit
Check
Delete
Exit
Choose a service: add
Please insert (Service, Email/Username, Password):
Google
user@gmail.com
mypassword123

Choose a service: check
Enter the service you want: Google
Email/Username: user@gmail.com
Password: mypassword123
```

---

## 👨‍💻 Author

Eslam — ITI - CS50 Final Project

---

## 📜 License

Copyright © 2026 Eslam

This project is submitted as a final project for the CS50 Introduction to Computer Science course offered by ITI (Information Technology Institute), Egypt.

All rights reserved. This code may not be copied, modified, or distributed without permission from the author.
