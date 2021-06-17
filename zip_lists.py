# Use zip() and type annotation (from typing)
from typing import List

numbers = [1, 2, 3]
names = ['Ann', 'Bob', 'Emma']


def main() -> None:
    '''Run main function.'''
    numbered_names = zip_lists(numbers, names)
    
    for number, name in numbered_names:
        print(number, name)


def zip_lists(nums: List[int], strings: List[str]) -> List[tuple]:
    ''' Zip two lists into one list of tuples.'''
    return list(zip(nums, strings))


if __name__ == '__main__':
    main()
