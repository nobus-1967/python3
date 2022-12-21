#!/usr/bin/env python3
"""Flatten list of lists."""
import numpy as np

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'Source: {list_of_lists}')

# Method 1: Brute Force
flatten_list_1 = []

for sublist in list_of_lists:
    for number in sublist:
        flatten_list_1.append(number)

print(f'Method 1: {flatten_list_1}')

# Method 2: List Comprehension
flatten_list_2 = [number for sublist in list_of_lists for number in sublist]

print(f'Method 2: {flatten_list_2}')

# Method 3: NumPy Flatten
np_array = np.array(list_of_lists)

flatten_list_3 = list(np_array.flatten())

print(f'Method 3: {flatten_list_3}')
