# 2D-dictionary with named rows.
# Example:
# {'Jane': {'Math': 4, 'English': 5, 'History': 5},
#  'John': {'Math': 2, 'English': 3, 'History': 4}}
grades = {}

for i in range (2):
    name = input('Enter name: ')
    math = int(input('Enter grade in Math: '))
    en = int(input('Enter grade in English: '))
    hist = int(input('Enter grade in History: '))
    
    grades[name] = {'Math': math, 'English': en, 'History': hist}
    print()

print(grades)

print()

for name in grades:
    print(f'{name}:', end=' ')
    for subject in grades[name]:
        print(f'{subject} - {grades[name][subject]}.', end=' ')
    print(end='\n')
    
print()

for name in grades:
    print(name)

print()

for name in grades:
    print(grades[name]['Math'])

print()

for name in grades:
    print((name), grades[name]['English'])

print()

for name in grades:
    print((name), 'History', grades[name]['History'])

print()

for name in grades:
    print(name)
    for subject in grades[name]:
        print('->', subject, grades[name][subject])
    print()
