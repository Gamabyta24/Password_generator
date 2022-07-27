from random import choice
import prompt



def pwd_lenght():
    return prompt.integer("Enter pass lenght: ")
def pwd_auto():
    return prompt.string("Gen auto? (y, n): ")
def pwd_digits():
    return prompt.string("include digits? (y, n): ")
def pwd_uppercase():
    return prompt.string("include uppercase (y, n): ")
def pwd_lowercase():
    return prompt.string("include lowercase (y, n): ")
def pwd_punctuation():
    return prompt.string("include symbols? (y, n): ")
def your_pass(password):
    print(f'Your password: {password}')


def main():
    digits = "0123456789"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!#$%&*+-=?@^_"
    ally = digits + uppercase + lowercase + punctuation

    chars = ""

    x = pwd_lenght()
    answer = pwd_auto()

    if answer == "y":
        chars += ally
    else:
        pwd_digits()
        pwd_uppercase()
        pwd_lowercase()
        pwd_punctuation()
        if pwd_digits == "y":
            chars += digits
        if pwd_uppercase == "y":
            chars += uppercase
        if pwd_lowercase == "y":
            chars += lowercase
        if pwd_punctuation == "y":
            chars += punctuation


    password = ""
    for i in range(x):
        password += choice(chars)
    your_pass(password)

if __name__ == '__main__':
    main()