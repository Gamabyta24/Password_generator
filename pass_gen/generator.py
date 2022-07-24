from random import choice
import prompt

def main():
    digits = "0123456789"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!#$%&*+-=?@^_"
    ally = digits + uppercase + lowercase + punctuation

    chars = ""

    pwd_length = prompt.integer("Enter pass lenght: ")
    pwd_auto = prompt.string("Gen auto? (y, n): ")

    if pwd_auto == "y":
        chars += ally
    else:
        pwd_digits = prompt.string("include digits? (y, n): ")
        pwd_uppercase = prompt.string("include uppercase (y, n): ")
        pwd_lowercase = prompt.string("include lowercase (y, n): ")
        pwd_punctuation = prompt.string("include symbols? (y, n): ")
        if pwd_digits == "y":
            chars += digits
        if pwd_uppercase == "y":
            chars += uppercase
        if pwd_lowercase == "y":
            chars += lowercase
        if pwd_punctuation == "y":
            chars += punctuation


    password = ""
    for i in range(pwd_length):
        password += choice(chars)
    print(f'Your password: {password}')

if __name__ == '__main__':
    main()