# Recursive function as a countdown

def main():
    """Run main function."""
    number = get_number()
    
    while number == 0:
        number = get_number()
    
    print('\nStart:')
    countdown(number)


def get_number() -> int:
    """Input and check a numver from 1 yo 100."""
    try:
        num = int(input('Enter a positive integer from 1 to 100: '))
        assert 1 <= num <= 100
        
        return num       
    except (ValueError, AssertionError):
        print('Wrong value, try again.')
        
        return 0
        

def countdown(n: int) -> None:
    """Run recursive function."""
    if n == 1:
        print('1\nDone!')
    else:
        print(n)
        countdown(n - 1)
        
        
if __name__ == '__main__':
    main()
    