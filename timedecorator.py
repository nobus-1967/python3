#!/usr/bin/env python3
"""Simple time decorator."""
from time import time


def time_decorator(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f'Elapsed time: {(end - start):.6} seconds')

    return wrapper


if __name__ == '__main__':

    @time_decorator
    def print_nums():
        num = int(input('Enter an integer greater than 0: '))
        print(*[num for num in range(1, num + 1)], sep=', ')

    print_nums()
