# Clear and split strings using re.
import re
from string import punctuation


def main():
    string = input('Enter a string:\n')

    word_list = [
        word.casefold()
        for word in re.split(r' \s*', re.sub(f'[{punctuation}]+', '', string))
        if word != ''
    ]
    print(f'Words: {word_list}')


if __name__ == '__main__':
    main()
