"""
Write a program that asks the user for a password and validates it based on the following criteria:
The password must be at least seven characters long.
It must contain at least one uppercase letter.
It must contain at least one lowercase letter.
It must contain at least one numeric digit.
"""


def main():
    password = input('Enter your password: ')
    if len(password) < 7:
        print("That is not a valid password.")
    elif not any(char.isupper() for char in password):
        print("That is not a valid password.")
    elif not any(char.islower() for char in password):
        print("That is not a valid password.")
    elif not any(char.isdigit() for char in password):
        print("That is not a valid password.")
    else:
        print("This is a Valid password.")
main()