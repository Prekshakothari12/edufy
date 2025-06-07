import os
from datetime import datetime

LOG_FILE = "login_log.txt"

def write_login(username):
    with open(LOG_FILE, "a") as f:
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{username}, {login_time}\n")
    print("Login info saved.")

def display_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            print("Log contents:")
            print(f.read())
    else:
        print("Log file does not exist.")

def clear_log():
    with open(LOG_FILE, "w") as f:
        pass  # Overwrites the file with nothing
    print("Log cleared.")

def delete_log():
    if os.path.exists(LOG_FILE):
        confirm = input("Are you sure you want to delete the log? (y/n): ")
        if confirm.lower() == 'y':
            os.remove(LOG_FILE)
            print("Log file deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Log file not found.")

# Example menu
while True:
    print("\n--- User Login Logger ---")
    print("1. Write login")
    print("2. Display log")
    print("3. Clear log")
    print("4. Delete log")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        user = input("Enter username: ")
        write_login(user)
    elif choice == '2':
        display_log()
    elif choice == '3':
        clear_log()
    elif choice == '4':
        delete_log()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
