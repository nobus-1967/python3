#!/usr/bin/env python3
"""Create cleared word list from string."""
import re

punctuation: str = r'[!"#$&\'()*+,./:;<=>?\[\\\]^`{|}~]'
string: str = (
    ' #\t**My   `super-string`**  (100%?), email:  john_doe@mail.com. \n'
)

# 1. Remove punctuation marks  and special characters from string.
cleared_string: str = re.sub(punctuation, '', string)
print(cleared_string)

# 2. Strip string (remove whitespace characters).
stripped_string: str = cleared_string.strip()
print(stripped_string)

# 3. Split string into words in lowercase.
splitted_string: list[str] = [
    word.lower() for word in stripped_string.split(' ') if word
]
print(splitted_string)
