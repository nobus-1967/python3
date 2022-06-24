#!/usr/bin/env python3
"""Hash (using bcrypt), store (using pickle) and validate a password."""
import getpass
import bcrypt
import pickle


def main():
    """Run main program."""
    # 1. Secure input and encrypt user's password:
    hashed_password = hash_password()

    # 2. Save encrypted password to file 'password.dat':
    store_hash(hashed_password)

    # 3. Load and read encrypted password from file 'password.dat':
    restored_hashed_password = load_hash()

    # 4. Validate encrypted password (user's secure input again):
    result = validate_hash(restored_hashed_password)
    if result:
        print('Validation was successful!')
    else:
        print('Validation failed!')


def hash_password():
    """Secure input and encode a password."""
    password = getpass.getpass(prompt='Enter your password to encrypt: ')
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def store_hash(hashed_password):
    """Save encrypted password to file."""
    with open('password.dat', 'wb') as file:
        pickle.dump(hashed_password, file)


def load_hash():
    """Load and read encrypted password from file."""
    with open('password.dat', 'rb') as file:
        return pickle.load(file)


def validate_hash(restored_hashed_password):
    """Validate encrypted password."""
    password = getpass.getpass(prompt='Enter your password to validate: ')
    return bcrypt.checkpw(password.encode(), restored_hashed_password)


if __name__ == '__main__':
    main()
