#!/usr/bin/env python3
# Convert CamelCase into snake_case or kebab-case.


def main():
    """Convert CamelCase into snake_case or kebab-case."""
    print('Starting the program...')
    
    menu()
    
    print('Finishing the program...')
   

def menu():
    """Show the menu of this program."""
    
    choice = 'y'
    
    while choice == 'y':
        print('\nThis program convert names from CamelCase into:')
        print('\t1. lowerCamelCase')
        print('\t2. snake_case')
        print('\t3. kebab-case')
        
        try:
            name = input('\nEnter a name to convert in CamelCase:\n\t<-- ')
            
            item = int(input('Choose 1 or 2 or 3 menu item: '))
        
            if item == 1:
                lower_camel_case(name)
            elif item == 2:
                snake_case(name)
            elif item == 3:
                kebab_case(name)
            else:
                print('\t--> Wrong value of item...')                
            
            choice = input('\nConvert a new name? (y/n): ')

        except ValueError:
            print('\t--> Not a value of item...')
        
        
def lower_camel_case(name):
    """Convert a name into lowerCamelCase"""
    if name.isalpha():
        if len(name) == 1:
            converted_name = name[0].lower()
        else:
            converted_name = name[0].lower() + name[1:]
    else:
        converted_name = 'Hmm... seems there\'s nothing to convert...'
    
    print(f'\t--> {converted_name}')
            


def snake_case(name):
    """Convert a name into snake_ase"""
    if name.isalpha():
        if len(name) == 1:
            converted_name = name[0].lower()
        else:
            converted_name = name[0].lower()
            
            for ch in name[1:]:
                if ch.islower() or ch.isdigit():
                    converted_name += ch
                elif ch.isupper():
                    converted_name += '_' + ch.lower()
                
    else:
        converted_name = 'Hmm... seems there\'s nothing to convert...'
        
    print(f'\t--> {converted_name}')


def kebab_case(name):
    """Convert a name into kebab_case"""
    if name.isalpha():
        if len(name) == 1:
            converted_name = name[0].lower()
        else:
            converted_name = name[0].lower()
            
            for ch in name[1:]:
                if ch.islower() or ch.isdigit():
                    converted_name += ch
                elif ch.isupper():
                    converted_name += '-' + ch.lower()
                
    else:
        converted_name = 'Hmm... seems there\'s nothing to convert...'
        
    print(f'\t--> {converted_name}')
                

if __name__ == '__main__':
    main()
