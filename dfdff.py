# Password Manager Project
# Made by a 12th-grade student
# This program can save, view, search, and edit passwords
# All passwords are stored in a CSV file

import csv
import os

file_name = "passwords.csv"


# Add a new password
def add_password():
    print("\nAdd a new password")
    website = input("Website/App: ")
    password = input("Password: ")

    file_exists = os.path.isfile(file_name)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Website", "Password"])
        writer.writerow([website, password])

    print("Password saved!\n")


# View all passwords
def view_passwords():
    print("\nAll saved passwords:\n")
    try:
        with open(file_name, "r") as file:
            reader = list(csv.reader(file))
            if len(reader) <= 1:
                print("No passwords saved yet.\n")
                return

            for row in reader:
                print(f"{row[0]} : {row[1]}")

    except FileNotFoundError:
        print("No passwords found. Please add some first.\n")


# Search for a password
def search_password():
    print("\nSearch for a password")
    name = input("Website/App to search: ").lower()
    found = False

    try:
        with open(file_name, "r") as file:
            reader = list(csv.reader(file))
            for row in reader[1:]:  # skip header
                if row[0].lower() == name:
                    print(f"Password for {row[0]}: {row[1]}\n")
                    found = True
                    break

        if not found:
            print("No password found for that website/app.\n")

    except FileNotFoundError:
        print("No passwords saved yet.\n")


# Edit a password
def edit_password():
    print("\nEdit a password")
    name = input("Website/App to edit: ").lower()
    updated = False

    try:
        with open(file_name, "r") as file:
            reader = list(csv.reader(file))

        for i, row in enumerate(reader[1:], start=1):  # skip header
            if row[0].lower() == name:
                print(f"Current password: {row[1]}")
                new_pass = input("New password: ")
                reader[i][1] = new_pass
                updated = True
                break

        if updated:
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)
            print("Password updated!\n")
        else:
            print("No password found for that website/app.\n")

    except FileNotFoundError:
        print("No passwords saved yet.\n")


# Main program
while True:
    print("\nPassword Manager Menu")
    print("1. Add password")
    print("2. View passwords")
    print("3. Search password")
    print("4. Edit password")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        search_password()
    elif choice == "4":
        edit_password()
    elif choice == "5":
        print("\nThanks for using the Password Manager. Bye!\n")
        break
    else:
        print("Invalid choice, try again.\n")
