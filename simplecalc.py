#!/usr/bin/env python
# Простой калькулятоp
'''Simple calculator'''

# Основная функция программы
def main():
    '''Run the main function'''
    # Заголовок программы
    print('ПРОСТОЙ КАЛЬКУЛЯТОР')
    print('-------------------')
    
    # Получаем два операнда для вычислений
    print('ВВЕДИТЕ ПЕРВОЕ ЧИСЛО')
    print('Если число имеет дробную часть, она отделяется точкой!')  
    x = get_float()
    while x is None:
        x = get_float()
    print('ВВЕДИТЕ ВТОРОЕ ЧИСЛО')
    y = get_float()
    while y is None:
        y = get_float()

    # Получаем оператор для вычислений
    print('ВВЕДИТЕ ОПЕРАТОР ДЛЯ ВЫЧИСЛЕНИЯ')
    operator = get_operator()
    while operator is None:
        operator = get_operator()
        
    # Производим вычисления с полученными числами
    result = calculate(x, y, operator)

    # Печать результата c точностью до 5 знаков после запятой
    print('----------')
    print('РЕЗУЛЬТАТ:')
    print(f'{x} {operator} {y} = {result: .5f}')


# Функция для ввода и проверки корректности вводимого числа
def get_float() -> float | None:
    '''Input a float'''
    try:
        number = float(input('(число, не равное 0): '))  
        assert number != 0
        
        return number
    
    except (AssertionError, ValueError):
        print('Число введено неверно! Необходимо ввести его заново')
        print('(Число не должно быть равным нулю!)')
                
        return None
        

# Функция для ввода и проверки корректности вводимого оператора
def get_operator() -> str | None:
    '''Input an orerator'''
    try:
        operator = input('(+ или - или * или /): ')
        assert operator[0] in '+-*/'
        
        if len(operator) > 1:
            raise AssertionError        
        
        return operator
    
    except AssertionError:
        print('Оператор введен неверно! Необходимо ввести его заново')
        print('(один символ из числа +-*/)')
                
        return None
               
        
# Функция для математических действий с числами
def calculate(x: float, y: float, operator: str) -> float:
    '''Calculate two numbers'''
    total = 0.0
    
    if operator == '+':
        total = x + y
    elif operator == '-':
        total = x - y
    elif operator == '*':
        total = x * y
    elif operator == '/':
        total = x / y
        
    return total


if __name__ == '__main__':
    main()

