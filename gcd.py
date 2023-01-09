#!/usr/bin/env python3
"""
Find the Greatest Common Divisor (the Euclidean Algorithm), CLI version.
Python: 3.10 (implement Switch Statements).
"""


def main() -> None:
    """Run main program."""
    print('FINDING THE GREATEST COMMON DIVISOR (GCD):')
    print('------------------------------------------')

    result = find_gcd(m, n)

    print('Numbers:', f'{m} and {n}')
    print('GCD:'.rjust(8), result)


def find_gcd(x: int, y: int) -> int:
    """Return recursively the GCD."""
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y
    else:
        return find_gcd(x, x % y)


if __name__ == '__main__':
    import sys

    HELP: list = ['h', '-h', '--h', 'help', '-help', '--help']

    try:
        match len(sys.argv):
            case 2:
                if sys.argv[1].strip().lower() in HELP:
                    print('HELP:')
                    print('-----')
                    print('This program finds the Greatest Common Divisor')
                    print('(using the Euclidean Algorithm).')
                    print('You should enter two arguments - integers 0, e.g.:')
                    print('>>> gcd.py 2 1')
                    print('Make sure you are using Python 3.10 or newer!')
                else:
                    raise ValueError
            case 3:
                if (
                    sys.argv[1].strip().isnumeric()
                    and sys.argv[2].strip().isnumeric()
                ) and (int(sys.argv[1]) > 0 and int(sys.argv[2]) > 0):
                    m, n = [int(arg.strip()) for arg in sys.argv[1:]]
                    main()
                else:
                    raise ValueError
            case _:
                raise IndexError
    except (IndexError, ValueError):
        print('WRONG NUMBER/VALUE/TYPE OF ARGUMENTS!')
        print('-------------------------------------')
        print('You should enter two integers greater than 0, e.g.:')
        print('>>> gcd.py 2 1')
    except SyntaxError:
        print('OLD VERSION OF PYTHON!')
        print('----------------------')
        print('This program requires Python 3.10 or newer.')
