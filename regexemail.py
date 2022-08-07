"""Search email using RegEx."""
import re


def main():
    """Run main program."""
    email_regex = re.compile(
        r'''
        (^(?:[A-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Z0-9!#$%&'*+/=^_`{|}~-]+)*))
        @
        ((?:[A-Z0-9]+(?:-[A-Z0-9]+)*)(?:\.[A-Z]{2,})$)
        ''',
        re.IGNORECASE | re.VERBOSE
    )

    user_email = input('Enter email to check: ')

    result = email_regex.search(user_email)

    if result:
        email = result.group()
        local_part, domain = result.groups()

        print('This email is valid!')
        print('--------------------')
        print('Email info')
        print('--------------------')
        print(f'full address: {email}')
        print(f'local-part: {local_part}')
        print(f'domain: {domain}')
    else:
        print('This email is not valid!')


if __name__ == '__main__':
    main()
