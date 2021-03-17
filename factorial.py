# Вычисление факториала числа 100 различными методами

# Метод 1: рекурсия
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(f'Метод 1 (рекурсия) для числа 100: {recursive_factorial(100)}')


# Метод 2: итерация + рекурсия
def iterative_and_recursive_factorial(n):
    def calculate_factorial(counter, factorial):
        if counter == 1:
            return factorial
        else:
            return calculate_factorial(counter - 1, counter * factorial)
    
    return calculate_factorial(n, 1)
    

print(f'Метод 2 (интерация + рекурсия) для числа 100: {iterative_and_recursive_factorial(100)}')


# Метод 3: итерация (цикл while)
def iterative_factorial_while(n):
    factorial = 1
    counter = 1
    while counter <= n:
        factorial *= counter
        counter += 1
    
    return factorial


print(f'Метод 3 (итерация-while) для числа 100: {iterative_factorial_while(100)}')


# Метод 4: итерация (цикл for)
def iterative_factorial_for(n):
    factorial = 1
    for value in range(1, n + 1):
        factorial *= value
    
    return factorial


print(f'Метод 4 (итерация-for) для числа 100: {iterative_factorial_for(100)}')
