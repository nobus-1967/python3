#!/usr/bin/env python3
"""Convert int to list of digits (the same order)."""

from typing import Union, Tuple, List, Any


def main():
    """Run the main function."""
    
    # Get a number (int).
    number = get_int()
    
    while number is None:
        number = get_int()
    
    # Convert int to list of it's digits.
    minus, digits_list = int_2_digit_lists(number)
    
    # Print a result.
    print_result(number, minus, digits_list)
        

def get_int() -> Union[int, Any]:
    """Get a number to convert from user."""
    
    try:
        user_input = input('Please input an integer number >>> ')
        
        number = int(user_input)
    except (TypeError, ValueError):
        print(f'({user_input}) is not an integer number.',
                            'Please try again!' )
        print('----------------------------------')
        
        return None
    else:
        return number    

    
def int_2_digit_lists(number: int) -> Tuple[bool, List[int]]:
    """Get int and return list of it's digits."""
    digits_list = []
    minus = False
    
    if number <0:
        number = abs(number)
        minus = True
    
    if number < 10:
        digits_list.append(number)
    else:
        digits_list.append(number % 10)
        number //= 10
         
        while number > 0:
            digits_list.insert(0, number % 10)
            number //= 10
            
    return minus, digits_list


def print_result(number: int, minus: bool, digits_list: List[int]) -> None:
    """Print a result of convertion."""
    print('----------------------------------')
    print(f'({number}) consists of the following digits:', end=' ')
    
    if minus:
        print('<minus>', end=' ')
    
    for digit in digits_list:
        print(digit, end=' ')    
    
    print(end='\n')


if __name__ == '__main__':
    main()
