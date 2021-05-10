#!/usr/bin/env python3
# Check if the number is a prime number.

def main():
    """Check the number if that's a prime number.""" 
    try:
        number = int(input('Enter a natural number greater than 1: '))
        
        if number < 2:
            result = 'Incorrect value'
        elif number == 2:
            result = True
        else:
            result = is_prime(number)
        
        print(result)
    except ValueError:
        print('Not a number')


def is_prime(number):
    """Check the number greater than 2.""" 
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False

    return True        


if __name__ == '__main__':
    main()
