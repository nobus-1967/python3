# Циклы, итераторы и рекурсия
# Выводим на экран последовательность цифр от 1 до 5 включительно

# Цикл с предусловием
def print_while():
    n = 1
    while n <= 5:
        print(n, end=' ')
        n += 1


# Простой итератор
def print_iter():
    list = [1, 2, 3, 4, 5]
    list = iter(list)
    print(next(list), end=' ')
    print(next(list), end=' ')
    print(next(list), end=' ')
    print(next(list), end=' ')
    print(next(list), end=' ')
    
# Цикл for
def print_for():
    for num in range(1, 6):
        print(num, end=' ')
        
# Рекурсия
def print_recursively(n=5):
    if n == 1:
        print(n, end=' ')
    else:
        print_recursively(n - 1)
        print(n, end=' ')
        

if __name__ == '__main__':
    print('1) Цикл с предусловием:')
    print_while()
    print('\n\n2) Простой итератор:')
    print_iter()
    print('\n\n3) Цикл for:')
    print_for()
    print('\n\n4) Рекурсия:')
    print_recursively()
