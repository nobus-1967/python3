# Counts letters in a string.
import string


def main() -> None:
    '''Run the main function.'''
    user_string = input('Enter your string here:\n')

    while len(user_string) == 0:
        user_string = input('Please, enter your string:\n')

    pure_user_string = clear_string(user_string)
    letters = count_letters(pure_user_string)    

    print('Frequence of used letters in your string:')
    print_dict(letters)


def clear_string(a_string: str) -> str:
    '''Clear a string from punctuation and whitespace symbols.'''
    pure_string_list = a_string.lower().strip(string.punctuation + \
                                          string.whitespace).split()

    return ('').join(pure_string_list)


def count_letters(a_string: str) -> dict:
    '''Count symbols in the cleared list.'''
    a_dict = dict()
    
    for letter in a_string:
        a_dict[letter] = a_dict.get(letter, 0) + 1

    return a_dict


def print_dict(a_dict: dict) -> None:
    '''Print a dictionary of used letters alphabetically.'''
    for key in sorted(a_dict):
        print(f'{key}: {a_dict[key]: 2d} time(s)')
    
        
if __name__ == '__main__':
    main()    
