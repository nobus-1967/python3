#!/usr/bin/env python3
# A binary search function returns the index of the item if found.

import math


def main():
    """
    Looks for an item (a number) in a sorted sequence using
    a binary search function.
    Return the index of the item if found (or -1 if not found).
    """
    
    sequence = get_sequence()    
      
    number = int(input('Enter a natural number to look for in your sequence: '))
    result = binary_search(number, sequence)
    
    if result > 0:
        print(f'Number {number} is found, it has index {result}')
    elif result == -1:
        print(f'Number {number} is not found')


def get_sequence():
    """Get a sequence of items from user and sorted it (stop with 0)."""
    numbers = []
    
    number = int(input('Enter first natural number (an integer number > 0): '))
    
    while (number != 0):
        numbers.append(number)
        
        number = int(input('Next natural number (or 0 to finish input): '))
        
    print('You\'ve entered the numbers:')
    for number in numbers:
        print(number, end=' ')
        
    print('\n')
        
    unique_numbers = list(set(sorted(numbers)))
    
    print('The sorted list of unique numbers:')
    for number in unique_numbers:
        print(number, end=' ')
        
    print('\n')        

     
    return unique_numbers


def binary_search(number, sequence):
    """Run a binary search"""
    left = 0
    right = len(sequence) - 1

    while True:
        if left > right:
            return -1
        
        middle = math.floor((left + right) / 2)
        
        if sequence[middle] < number:
            left = middle + 1
        elif sequence[middle] > number:
            right = middle - 1
        elif sequence[middle] == number:
            return middle    


if __name__ == '__main__':
    main()
