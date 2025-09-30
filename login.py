import time

def create_account():
    print("Create Account ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    print("Account created!")
    return username, password

def login(valid_username, valid_password):
    attempts = 0
    lockout_time = 60 #seconds

    while True:
        if attempts >= 5:
            print("Too many failed attempts. Locked out for 1 minute...")
            time.sleep(lockout_time)
            attempts = 0


        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == valid_username and password == valid_password:
            print("Login successful!")
            return True
        else:
            attempts += 1
            print(f"Wrong credentials. {5 - attempts} guesses left.")

def main():
    user, pw = create_account()
    login(user, pw)

if __name__ == "__main__":
    main()
