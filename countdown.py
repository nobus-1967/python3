# Recursive function as a countdown

def main():
    """Run main function."""
    number = get_number()
    
    while number == 0:
        number = get_number()
    
    print('\nStart:')
    countdown(number)


def get_number() -> int:
    """Input and check a number from 1 to 100."""
    try:
        num = int(input('Enter a positive integer from 1 to 100: '))
        
        # if num is not in range 1-100, it will be reassignment = 0
        if num <= 0:
            print('Wrong value (your number <= 0), try again.')
            num = 0
        elif num > 100:
            print('Wrong value (your number > 100), try again.')
            num = 0   
    except ValueError:
        # if exeption, num will be assignment = 0
        print('Wrong value (not a number), try again.')
        num = 0
    finally:
        # return num (num = 0 if not in range or exception)
        return num
        

def countdown(n: int) -> None:
    """Run recursive function."""
    if n == 1:
        print('1\nDone!')
    else:
        print(n)
        countdown(n - 1)
        
        
if __name__ == '__main__':
    main()
