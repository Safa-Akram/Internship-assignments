import hashlib
import re

# Function to check password strength
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        return False
    return True


# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Registration
def register():
    password = input("Create a password: ")

    if is_strong_password(password):
        hashed = hash_password(password)
        print("Registration successful!")
        return hashed
    else:
        print("Weak password!")
        print("Password must contain:")
        print("- At least 8 characters")
        print("- Uppercase letter")
        print("- Lowercase letter")
        print("- Number")
        print("- Special character")
        return None


# Login authentication
def login(stored_password_hash):
    password = input("Enter password to login: ")
    if hash_password(password) == stored_password_hash:
        print("Login successful ✅")
    else:
        print("Invalid password ❌")


# Main Program
stored_hash = register()
if stored_hash:
    login(stored_hash)
