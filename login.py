import time

# Hardcoded credentials (you can replace this with a database or file lookup)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def login():
    attempts = 0
    lockout_time = 60  # seconds

    while True:
        if attempts >= 5:
            print("Too many failed attempts. Locked out for 1 minute...")
            time.sleep(lockout_time)
            attempts = 0  # reset after lockout

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            print("✅ Login successful!")
            return True
        else:
            attempts += 1
            print(f"❌ Wrong credentials. {5 - attempts} guesses left.")