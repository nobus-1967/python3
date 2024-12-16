#!/usr/bin/env python3
"""Check if password is valid."""
import string
from dataclasses import dataclass

DIGITS = string.digits
ASCII_LOWERCASE = string.ascii_lowercase
ASCII_UPPERCASE = string.ascii_uppercase
PUNCTUATION = string.punctuation


@dataclass
class Colors:
    """Class for keeping ANSI Colors."""

    normal: str = "\033[0m"
    bold: str = "\033[1m"
    italic: str = "\033[3m"
    underline: str = "\033[4m"
    header: str = "\033[1;96m"
    ok: str = "\033[92m"
    error: str = "\033[91m"
    prompt: str = "\033[1;94m"


def main():
    """Run main program."""
    print("\n" + Colors.header + "Welcome to Password Validator!" + Colors.normal)
    print(Colors.header + "==============================\n" + Colors.normal)

    show_requirements()

    print("\n----------------------------------------------------")
    print("First, you should enter your password to validate...\n")

    user_password = check_passwords()
    print(
        "Your password to validate: "
        + Colors.bold
        + f"{user_password}"
        + Colors.normal
        + "\n"
    )

    print("----------------------------------------------------")
    print("Then, the program starts to validate you password...\n")

    validate_result = validate_password(user_password)
    if validate_result:
        print(
            Colors.ok
            + "[OK]"
            + Colors.normal
            + " Congratulations! Your password meets all requirements."
        )
    else:
        print(
            "\n"
            + Colors.error
            + "[FAIL]"
            + Colors.normal
            + " Unfortunately, your password does not meet "
            + "the minimum requirements."
        )

    print(Colors.header + "\n============================" + Colors.normal)
    print(Colors.header + "(c) Anatoly Shcherbina, 2024" + Colors.normal + "\n")


def show_requirements():
    """Print the requirements to user's password."""
    print(
        Colors.italic
        + "To be valid, your password must meet the following requirements:"
        + Colors.normal
    )
    print(
        " 1. Your password must be at least "
        + Colors.italic
        + "8 characters long"
        + Colors.normal
        + "."
    )
    print(" 2. Passwords must contain four character types:")
    print(
        "    -- at least "
        + Colors.italic
        + "one number"
        + Colors.normal
        + ": "
        + Colors.bold
        + "0-9"
        + Colors.normal
        + ";"
    )
    print(
        "    -- at least "
        + Colors.italic
        + "one lowercase letter"
        + Colors.normal
        + ": "
        + Colors.bold
        + f"{ASCII_LOWERCASE}"
        + Colors.normal
        + ";"
    )
    print(
        "    -- at least "
        + Colors.italic
        + "one uppercase letter"
        + Colors.normal
        + ": "
        + Colors.bold
        + f"{ASCII_UPPERCASE}"
        + Colors.normal
        + ";"
    )
    print(
        "    -- at least "
        + Colors.italic
        + "one symbol from the set"
        + Colors.normal
        + ": "
        + Colors.bold
        + f"{PUNCTUATION}"
        + Colors.normal
        + "."
    )


def create_password(message):
    """Create a new password."""
    while True:
        try:
            password = input(message)
            if not password.strip():
                raise ValueError
        except ValueError:
            print("[ERROR] You typed nothing!\n")
        else:
            return password.strip()


def check_passwords():
    """Check user's input for mismatches."""
    password_1st = create_password(
        Colors.prompt + ">>>" + Colors.normal + " Enter your password:    "
    )
    password_2nd = create_password(
        Colors.prompt + ">>>" + Colors.normal + " Re-enter your password: "
    )

    check_result = password_1st == password_2nd

    if check_result:
        print("\n" + Colors.ok + "[OK]" + Colors.normal + " Passwords match.")
        return password_1st
    else:
        print(
            "\n"
            + Colors.error
            + "[FAIL] "
            + Colors.normal
            + "Passwords do not match! Try to enter them again.\n"
        )
        return check_passwords()


def validate_password(password):
    """Validate user's password."""
    is_valid = {
        "correct_length": False,
        "has_digit": False,
        "has_lowercase": False,
        "has_uppercase": False,
        "has_symbol": False,
    }

    if len(password) >= 8:
        is_valid["correct_length"] = True
    else:
        print(
            Colors.error
            + "[ERROR]"
            + Colors.normal
            + " Password must be at least 8 characters!"
        )

    for character in password:
        if character.isdigit():
            is_valid["has_digit"] = True
        if character.islower():
            is_valid["has_lowercase"] = True
        if character.isupper():
            is_valid["has_uppercase"] = True
        if character in PUNCTUATION:
            is_valid["has_symbol"] = True

    if not is_valid["has_digit"]:
        print(
            Colors.error
            + "[ERROR]"
            + Colors.normal
            + " Password must contain (a) number(s)!"
        )
    if not is_valid["has_lowercase"]:
        print(
            Colors.error
            + "[ERROR]"
            + Colors.normal
            + " Password must contain (a) lower-case letter(s)!"
        )
    if not is_valid["has_uppercase"]:
        print(
            Colors.error
            + "[ERROR]"
            + Colors.normal
            + " Password must contain (a) uppercase letter(s)!"
        )
    if not is_valid["has_symbol"]:
        print(
            Colors.error
            + "[ERROR]"
            + Colors.normal
            + " Password must contain (a) special symbol(s)!"
        )

    return all(is_valid.values())


if __name__ == "__main__":
    main()
