#!/usr/bin/env python3
"""Convert miles to kilometers and kilometers to miles."""

MILE_IN_KM = 1.60934
KM_IN_MILE = 0.62137


def main():
    """Run main program."""
    print('CONVERTER MILES <-> KILOMETERS')
    print('------------------------------')
    display_menu()
       
    choice = check_choice()
    
    while choice in [1, 2]:
        run_converter(choice)
        
        print('\n>>> Do you want to convert another value?')
        
        choice = check_choice()
        
    print('\n------------------------')
    print('FINISHING THE PROGRAM...')
    
                
def display_menu():
    """Print the menu of the program."""
    print('\n1. Convert miles to kms.')
    print('2. Convert kms to miles.')
    print('3. Quit the program.\n')
    

def get_user_choice():
    """Input user's choice."""
    try:
        user_choice = int(input('>>> Enter your choice (1, 2 or 3): '))
        assert 1 <= user_choice <= 3
    
    except (AssertionError, ValueError):
        print('You should type 1, 2 or 3 and then ENTER')
        
        user_choice = None
    
    finally:
        return user_choice
    

def check_choice():
    """Get and check user's choice."""
    checked_choice = get_user_choice()
    
    while checked_choice is None:
        checked_choice = get_user_choice()
        
    return checked_choice


def get_user_value():
    """Input user's value to convert."""
    try:
        user_value = float(input('\n>>> Enter your value to convert: '))
        assert user_value >= 0.0
    
    except (AssertionError, ValueError):
        print('You should input a positive number (i.e 0, 7, 13.64 etc).')
        
        user_value = None
    
    finally:
        return user_value
    

def check_value():
    """Get and check user's value."""
    checked_value = get_user_value()
    
    while checked_value is None:
        checked_value = get_user_value()
    
    return checked_value
    
    
def run_converter(user_choice):
    """Run the converter and convert user's value."""
    value = check_value()
        
    match user_choice:
        case 1:
            print(f'\n{value} mile(s) = {convert_2_kms(value):.2f} km(s)')
        case 2:
            print(f'\n{value} km(s) = {convert_2_miles(value):.2f} mile(s)')
            

def convert_2_kms(user_value):
    """Convert miles to kilometers."""
    return user_value * MILE_IN_KM


def convert_2_miles(user_value):
    """Convert kilometers to miles."""
    return user_value * KM_IN_MILE

    
if __name__ == '__main__':
    main()
