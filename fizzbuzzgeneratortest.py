#!/usr/bin/env python3
"""Test FizzBuzz using generator (with time)."""

fizzbuzz = (('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
            for i in range(1, 10001))


def main():
    number = next(fizzbuzz)
    i = 1
    ok = 0
    errors = 0

    print('Starting test:')
    print('--------------')

    while number:
        try:
            if isinstance(number, int):
                print(f'{number}: OK')
                ok += 1
            elif isinstance(number, str):
                if i % 15 == 0:
                    assert number == 'FizzBuzz', f'{number} (for {i}): Error'
                    print(f'{number} (for {i}): OK')
                    ok += 1
                elif i % 3 == 0:
                    assert number == 'Fizz', f'{number} (for {i}): Error'
                    print(f'{number} (for {i}): OK')
                    ok += 1
                elif i % 5 == 0:
                    assert number == 'Buzz', f'{number} (for {i}): Error'
                    print(f'{number} (for {i}): OK')
                    ok += 1
                else:
                    assert number == 'FizzBuzz', f'{number} (for {i}): Error'
                    print(f'{number} (for {i}): Error')
                    errors += 1
        except AssertionError as e:
            print(e)
            errors += 1
        finally:
            try:
                number = next(fizzbuzz)
                i += 1
            except StopIteration:
                print('--------------')
                print('Test finished.')
                print(f'Total:\t{i}')
                break

    print(f'Passed:\t{ok}')
    print(f'Errors:\t{errors}')


if __name__ == '__main__':
    main()
