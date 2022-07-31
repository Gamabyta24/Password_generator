from random import choice
import prompt
from global_const import *


def your_pass(password):
    print(f"Your password: {password}")


def get_user_data():
    objects_data = {
        "lenght": 0,
        "auto": 0,
        "digits": 0,
        "uppercase": 0,
        "lowercase": 0,
        "symbols": 0,
    }
    objects_data["lenght"] = prompt.integer("Enter pass lenght: ")
    if prompt.string("Gen auto? (y, n): ") == "y":
        objects_data["auto"] = 1
        objects_data["digits"] = 1
        objects_data["uppercase"] = 1
        objects_data["lowercase"] = 1
        objects_data["symbols"] = 1
    else:
        if prompt.string("include digits? (y, n): ") == "y":
            objects_data["digits"] = 1
        if prompt.string("include uppercase (y, n): ") == "y":
            objects_data["uppercase"] = 1
        if prompt.string("include lowercase (y, n): ") == "y":
            objects_data["lowercase"] = 1
        if prompt.string("include symbols? (y, n): ") == "y":
            objects_data["symbols"] = 1
    return objects_data


def main():
    user_data = get_user_data()
    chars = ""
    if user_data["auto"] == 1:
        chars += ALL_OPTION
    if user_data["digits"] == 1:
        chars += DIGITS
    if user_data["uppercase"] == 1:
        chars += UPPERCASE
    if user_data["lowercase"] == 1:
        chars += LOWERCASE
    if user_data["symbols"] == 1:
        chars += PUNCTUATION
    print(user_data)

    password = ""
    for i in range(user_data["lenght"]):
        password += choice(chars)
    your_pass(password)


if __name__ == "__main__":
    main()
