''' Work with text files using context manager (with).'''

def main():
    '''Run the main function of the program.'''
    print('Starting the program...')
    answer = 'y'

    while answer == 'y':
        select_menu()

        print('\nDo you want to continue?')
        answer = input('Type y for "yes", others for "no" >>> ').lower()

    print('\nThe program is over.')


def select_menu():
    '''Show the menu and return user\'s choice.'''
    print('\n------------------------------')
    print('Menu: ')
    print('1. Create a new file')
    print('2. Display the file')
    print('3. Add a new item to the file')
    print('------------------------------\n')

    choice = user_input()

    while choice == 0:
        choice = user_input()

    if choice == 1:
        create_file()
    elif choice == 2:
        display_file()
    elif choice == 3:
        add_to_file()


def user_input():
    '''Input user\'s choice.'''
    try:
        choice = input('Make a selection 1, 2 or 3 >>> ')

        int_choice = int(choice)
        assert 1 <= int_choice <= 3

        return int_choice
    except (ValueError, AssertionError):
        print('Wrong selection.')
        return 0


def create_file():
    '''Create a new text file and write user\'s text.'''
    with open('file.txt', 'wt') as file:
        print('Type anything to write into the file:')
        text = input('>>> ')

        file.write(f'{text}\n')


def display_file():
    '''Display the text file with user\'s text.'''
    try:
        with open('file.txt', 'rt') as file:
            print('File\'s content:')
            print('------------------------------')

            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print('File doesn\'t exist.')
        print('Select item 1 from the menu to create a new file.')


def add_to_file():
    '''Add user\'s text to the file.'''
    with open('file.txt', 'at') as file:
        print('Type anything to add to the file')
        print('(create a file if it doesn\'t exist):')
        text = input('>>> ')

        file.write(f'{text}\n')


if __name__ == '__main__':
    main()
