#!/usr/bin/env python
# The same -  examples of using built-in all() and any()

# Collection (tuple of tuples) for analysis
PERSONS = (('Jane', 20, 'female'), ('Jack', 21, 'male'), ('John', 22, 'male'))


# Show person's data
print('Persons\' data for analysis:')
for name, age, gender in PERSONS:
    print(f'name: {name}, age: {age}, gender: {gender}')

print()

# Check if all names start with the letter 'J'
is_all_names_start_with_j = all(name.startswith('J') for name, age, gender in PERSONS)
print(f'Do all the names start with "J"? - {is_all_names_start_with_j}')

# Check if any name starts with the letter 'J'
is_any_name_starts_with_j = any(name.startswith('J') for name, age, gender in PERSONS)
print(f'Does any name start with "J"? - {is_any_name_starts_with_j}')

print()

# Check if all are of the full legal age (i.e. above 21 years old)
is_all_adult = all(age >= 21 for name, age, gender in PERSONS)
print(f'Are all of them of the full legal age? - {is_all_adult}')

# Check if any of them is legally an adult
is_any_adult = any(age >= 21 for name, age, gender in PERSONS)
print(f'Is any of them legally an adult? - {is_any_adult}')

print()

# Are all of them male?
is_all_male = all(gender == 'male' for name, age, gender in PERSONS)
print(f'Are all of them male? - {is_all_male}')

# Is any of them female?
is_any_female = any(gender == 'female' for name, age, gender in PERSONS)
print(f'Is any of them female? - {is_any_female}')
