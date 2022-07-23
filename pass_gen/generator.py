from random import choice

digits = "0123456789"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!#$%&*+-=?@^_"
ally = digits + uppercase + lowercase + punctuation

chars = ""

pwd_length = int(input("Enter pass lenght: "))
pwd_auto = input("Gen auto? (y, n): ")

if pwd_auto == "y":
    chars += ally
else:
    pwd_digits = input("include digits? (y, n): ")
    pwd_uppercase = input("include uppercase (y, n): ")
    pwd_lowercase = input("include lowercase (y, n): ")
    pwd_punctuation = input("include symbols? (y, n): ")
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
