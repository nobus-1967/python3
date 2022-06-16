#!/usr/bin/env python3
"""Check if password is valid."""

SPECIAL_SYMBOLS = '~@#$&-_'


def main():
    """Run main program."""
    print('PASSWORD VALIDATOR:')
    print('-------------------')
    show_requirements()

    password = input('\n>>> Enter your password to check: ')

    while not valid_password(password):
        print('This password is not valid!')
        password = input('\n>>> Try to enter another password: ')

    print('This password is valid.')


def show_requirements():
    """Print the requirements to user's password."""
    print('User\'s password must meet the following requirements:')
    print('1. The password must be at least 8 characters long.')
    print('2. It must contain at least 1 uppercase letter.')
    print('3. It must contain at least 1 lowercase letter.')
    print('4. It must contain at least 1 symbol from the set:')
    print('   ', end='')

    for symbol in SPECIAL_SYMBOLS:
        print(symbol, end=' ')

    print()


def valid_password(password):
    """Validate user's password."""
    is_valid = {'correct_length': False,
                'has_uppercase': False,
                'has_lowercase': False,
                'has_digit': False,
                'has_symbols': False}

    if len(password) >= 8:
        is_valid['correct_length'] = True

    for ch in password:
        if ch.isupper():
            is_valid['has_uppercase'] = True
        if ch.islower():
            is_valid['has_lowercase'] = True
        if ch.isdigit():
            is_valid['has_digit'] = True
        if ch in SPECIAL_SYMBOLS:
            is_valid['has_symbols'] = True

    return all(is_valid.values())


if __name__ == '__main__':
    main()
