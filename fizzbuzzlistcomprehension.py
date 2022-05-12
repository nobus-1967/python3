#!/usr/bin/env python3
"""One-liner FizzBuzz test using List comprehension."""

fizz_buzz_list = ['Fizzbuzz' if number % 15 == 0 else
             ('Fizz' if number % 3 == 0 else
              ('Buzz' if number % 5 == 0 else number))
             for number in range(1, 101)]

print('FizBuzz Test')
print('------------')
for index, item in enumerate(fizz_buzz_list):
    print(f'{index + 1:3d} - {item}')

