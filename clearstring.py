#!/usr/bin/env python3
"""Create cleared word list from string."""
import re

# Punctuation and special symbols
PUNCTUATION_1 = r'[!"#&\'()*+,;<=>?\[\\\]^`{|}~]'
PUNCTUATION_2 = '.-_:/'


def clear_string(string):
    # 1. Remove punctuation marks  and special characters from string
    cleared_string = re.sub(PUNCTUATION_1, '', string)

    # 2. Strip string (remove whitespace characters).
    stripped_string = cleared_string.strip()

    # 3. Convert letters to lowercase.
    lower_string = stripped_string.lower()

    # 4. Split string into words (removing spaces).
    splitted_string = [word.strip() for word in lower_string.split(' ')]

    # 5. Clear words from period and some other marks.
    cleared_list = [word.strip(PUNCTUATION_2) for word in splitted_string]

    # 6. Finally remove empty strings from word list.
    word_list = [word for word in cleared_list if word]

    return word_list


if __name__ == '__main__':
    string = """
 #\t**My  `super-string`** (50%?), ~$25.00, e-mail: john_doe@mail.com. \n
>>> {Details -- http://www.dohndoe.net}
"""
    print(clear_string(string))
