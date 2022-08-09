from random import choice
import prompt
from global_const import (
    DIGITS,
    DIGITS_OBJ,
    UPPERCASE,
    UPPERCASE_OBJ,
    LOWERCASE,
    LOWERCASE_OBJ,
    PUNCTUATION,
    PUNCTUATION_OBJ,
    LONG_OBJ,
)


def your_pass(password):
    """Print your password.

    Returns:
        String with your password.
    """
    print(f"Your password: {password}")


def default_values(object_arg, value=False):
    """Set default values in list."""
    object_arg[DIGITS_OBJ] = value
    object_arg[UPPERCASE_OBJ] = value
    object_arg[LOWERCASE_OBJ] = value
    object_arg[PUNCTUATION_OBJ] = value


def get_user_data():
    """Get user data.

    Returns:
        Personal list with user request.
    """
    objects_data = {}
    default_values(objects_data)
    objects_data[LONG_OBJ] = prompt.integer("Enter pass lenght: ")
    if prompt.string("Gen auto? (y, n): ") == "y":
        default_values(objects_data, True)
    else:
        if prompt.string("include digits? (y, n): ") == "y":
            objects_data[DIGITS_OBJ] = True
        if prompt.string("include uppercase (y, n): ") == "y":
            objects_data[UPPERCASE_OBJ] = True
        if prompt.string("include lowercase (y, n): ") == "y":
            objects_data[LOWERCASE_OBJ] = True
        if prompt.string("include symbols? (y, n): ") == "y":
            objects_data[PUNCTUATION_OBJ] = True
    return objects_data


def main():
    """Main function."""
    user_data = get_user_data()
    chars = ""
    if user_data[DIGITS_OBJ]:
        chars += DIGITS
    if user_data[UPPERCASE_OBJ]:
        chars += UPPERCASE
    if user_data[LOWERCASE_OBJ]:
        chars += LOWERCASE
    if user_data[PUNCTUATION_OBJ]:
        chars += PUNCTUATION
    print(user_data)

    password = ""
    for i in range(user_data[LONG_OBJ]):
        password += choice(chars)
    your_pass(password)


if __name__ == "__main__":
    main()
