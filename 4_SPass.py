#Strong password checker
#Must have at least 1 uppercase letter
#Must have at least 1 lowercase letter
#Must have at least 1 special character
#Must  be at least 8 characters long and at most 16 characters long
#Must have  at  least 1 number
#Must not have two consecutive characters that are same

import getpass
import string

def is_strong_password(password):
    reasons = []

    if not (8 <= len(password) <= 16):
        reasons.append("Password length should be between 8 and 16 characters.")

    if not any(char.isupper() for char in password):
        reasons.append("Password should contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        reasons.append("Password should contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        reasons.append("Password should contain at least one digit.")

    special_chars = string.punctuation  # All special characters
    if not any(char in special_chars for char in password):
        reasons.append("Password should contain at least one special character.")

    if any(password[i] == password[i + 1] for i in range(len(password) - 1)):
        reasons.append("Password should not have consecutive repeating characters.")

    return reasons

password = getpass.getpass("Enter the password: ")
weakness_reasons = is_strong_password(password)

if not weakness_reasons:
    print("Strong Password")
else:
    print("Weak Password")
    for reason in weakness_reasons:
        print(reason)
