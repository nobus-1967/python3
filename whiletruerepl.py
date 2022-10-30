#!/usr/bin/env python3
"""
While loop example - simple REPL:

- type something and the program will repeate it as 'You typed: ...';
- to quit just type nothing (press only ENTER);
- or type 'q' + ENTER (or press CTRL+D) and confirm exit.
"""


def main() -> None:
    while True:
        try:
            user_input = input('prompt> ')

            if user_input:
                if user_input.strip().lower() == 'q':
                    answer = quit()

                    if not answer:
                        return answer
                else:
                    print(f'You typed: "{user_input}"')
            else:
                print('You typed nothing, quitting the program...')

                return False
        except EOFError:
            answer = quit()

            if not answer:
                return answer


def quit() -> bool:
    print('Do you really want to exit?')

    answer = input('[y/n]> ').strip().lower()

    while answer not in ['y', 'yes', 'n', 'no']:
        print('Wrong answer! Type "y" or "n":')

        answer = input('[y/n]> ').strip().lower()

    if answer in ['y', 'yes']:
        return False
    elif answer in ['n', 'no']:
        return True


if __name__ == '__main__':
    main()
