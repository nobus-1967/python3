import random

def guess_number(maximum: int, number: int) -> str:
    try:
        your_number = input('Введите ваше число от 1 до {}: '.format(maximum))
        your_number = int(your_number)
    except ValueError:
        print('\tНеобходимо было ввести целое положительное число!')
        print('\n!!! Программа завершена !!!')
    else:
        if your_number == number:
            print('\tПоздравляю, вы отгадали число и выиграли!')
            print('\n\tПрограмма завершена')
        elif your_number > number:
            print('\tНет, не угадали! Ваше число больше!')
            guess_number(maximum, number)
        else:
            print('\tНет, не угадали! Ваше число меньше')
            guess_number(maximum, number)


def max_number() -> int:
    try:
        maximum = input('Введите максимальное число от 1 до 100 включительно: ')
        maximum = int(maximum)
    except ValueError:
        print('\tНеобходимо было ввести целое положительное число!\n \
              Я делаю это за вас: 100')
        return 100
    else:
        return maximum
    


def random_number(maximum: int) -> int:
    number = random.randint(1, maximum)

    return number


maximum = max_number()
number = random_number(maximum)

if __name__ == '__main__':
    guess_number(maximum, number)
