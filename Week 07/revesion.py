"""
Login [l]
Register [r]
    Custom password [c]
    Generated password [g]
        Digits? [y/n]
        Symbols? [y/n]
        Length of password (default = 10) [50]
View Accounts [v]
Exit [e]
"""
import string
import random

phonebook_dictionary = {}


def read_into_dictionary():
    file_in = open("phonebook.txt", "r")
    for line in file_in:
        name, phone = line.split(" ")
        phonebook_dictionary[name] = phone.rstrip()


def validate():
    read_into_dictionary()  # Reading into a dictionary
    entered_name = input("Enter a name: ")
    entered_phone = input("Enter the phone number: ")
    # Check if a name exists in the dictionary
    if entered_name in phonebook_dictionary:
        print("name found")
    else:
        print("name not found")
    # Check if the entered phone no. belongs to the entered name
    if entered_phone == phonebook_dictionary[entered_name]:
        print("phone valid")
    else:
        print("phone not valid")


def generate_secret_word():
    # Generate password
    letters = string.ascii_letters  # Alphabet letters (upper & lower case)
    digits = string.digits  # All numbers 0-9
    symbols = string.punctuation  # All special characters/symbols
    secret_word = ""
    character_combo = letters  # include letters
    include_digits = input("Would you like to include digits? [y/n]: ").lower()
    if include_digits == "y":
        character_combo += digits
    combo_length = input("Enter the length of secret word (press enter for 10): ")
    if combo_length == "":
        combo_length = 10
    else:
        combo_length = int(combo_length)
    for character in range(combo_length):
        secret_word += random.choice(character_combo)
    print(secret_word)


def get_and_save_record():
    new_name = input("Enter a name: ")
    new_phone = input("Enter the phone number: ")
    file_out = open("phonebook.txt", "a")
    file_out.write(new_name + " " + new_phone + "\n")
    file_out.close()


def view_records():
    read_into_dictionary()
    print(f"{'Name':10s} Phone\n{'':-<21s}")
    for name, phone in phonebook_dictionary.items():
        print(f"{name:10s} {phone}")

# Login
# validate()

# generate_secret_word()

# Save a new record
# get_and_save_record()

# View records
# view_records()
