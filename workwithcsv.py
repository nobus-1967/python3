'''Work with CSV-files using csv module and context manager (with).'''
import csv


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
    print('1. Create a new CSV-file')
    print('2. Display records')
    print('3. Add a new item to the CSV-file')
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
    '''Create a new CSV-file and add a record.'''
    with open('file.csv', 'w', newline='') as file:
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        print('Input some data to write into the CSV-file:')
        record = make_record()

        while record == 0:
            record = make_record()

        writer.writerow(record)


def display_file():
    '''Display all records in the CSV-file.'''
    try:
        with open('file.csv', newline='') as file:
            reader = csv.DictReader(file)

            print('Records (title is not included):')
            print('------------------------------')
            print('Name\t| Age\t| City')
            print('------------------------------')

            for row in reader:
                print(f"{row['name']}\t| {row['age']}\t| {row['city']}")
    except FileNotFoundError:
        print('File doesn\'t exist.')
        print('Select item 1 from the menu to create a new CSV-file.')


def add_to_file():
    '''Add new record to the CSV-file.'''
    with open('file.csv', 'a') as file:
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        print('Input some data to write into the CSV-file')
        print('(create a file if it doesn\'t exist):')
        record = make_record()

        while record == 0:
            record = make_record()

        writer.writerow(record)


def make_record():
    '''Make a new record for CSV-file.'''
    try:
        name = input('Enter name >>> ')
        assert len(name) > 0

        age = input('Enter age  >>> ')
        assert len(age) > 0

        city = input('Enter city >>> ')
        assert len(city) > 0

        return {'name': name, 'age': age, 'city': city}
    except AssertionError:
        print('Wrong data. Repeat your input:')
        return 0


if __name__ == '__main__':
    main()
