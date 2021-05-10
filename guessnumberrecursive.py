#!/usr/bin/env python3
import random

def guess_number(number):
    "Пользователь отгадывает случайное число."
    user_number = int(input('\n>>> Введите ваше число от 1 до 100: '))
    
    if user_number == number:
        print('\tВы отгадали загаданное число! Поздравляю')
    elif user_number > number:
        print('\tНе угадали! Загаданное число меньше')
        guess_number(number)
    elif user_number < number:
        print('\tНе угадали! Загаданное число больше')
        guess_number(number)
    

if __name__ == '__main__':
    guess_number(random.randint(1, 100))
