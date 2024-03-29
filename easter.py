#!/usr/bin/env python3
# Расчет Православной Пасхи в XXI веке.
"""Date of Orthodox Easter (XXI century)."""

# Константы для работы программы.
"""Сonstants list."""
A = 19
B = 4
C = 7
D1 = 30
D2 = 19
D3 = 15
E1 = 7
E2 = 2
E3 = 4
E4 = 6
F1 = 4
F2 = 26


# Основная функция программы.
def main():
    # Запустить основную функцию.
    """Run the main function."""
    # Инициализировать флаг, который будет повторять выполнение программы.
    another = 'д'

    # Печатать названия программы.
    print('Определение даты Православной Пасхи в XXI веке')
    print('----------------------------------------------')

    # Запустить цикла выполнения программы.
    while another == 'д':

        # Получить год для определения Пасхи.
        year = get_year()
        while year is None:
            year = get_year()

        # Сообщить пользователю о том, для какого года будет произведён расчёт.
        print(f'Дата Православной Пасхи будет определена для {year} года.')

        # Расчитать дату Пасхи по новому стилю и вывести её.
        easter_date = calculate_easter_date(int(year))
        print(f'Итак, Пасха приходится на {easter_date[0]} {easter_date[1]}.')

        # Запросить у пользователя необходимость повторного расчёта Пасхи
        # для другого года.
        print('\nПовторить расчёт Православной Пасхи для другого года?')
        another = input('д=да, всё остальное=нет: ')
        if another.lower() == 'да':
            another = another[0].lower()

    # Сообщить о завершении программы.
    print('--------------------------')
    print('Работа программы завершена')
    print('(c) Nobus, 2022')


def get_year() -> int | None:
    # Ввести год для расчета даты Православной Пасхи.
    """Input a year to calculate the date of Orthodox Easter."""
    try:
        year = int(input('Введите год для определения даты Пасхи: '))
        assert 2000 < year < 2101

    except (AssertionError, ValueError):
        # В случае ошибки вернуть None для повторного ввода года.
        print('Год введен неверно! Необходимо ввести его заново.')
        print('(Год - целое число больше 2000 и меньше 2101.)')

        return None
    else:
        # Вернуть год.
        return year


def calculate_easter_date(year: int) -> list:
    # Расчитать дату Пасхи.
    """Calculate the Easter's date."""
    a = year % A
    b = year % B
    c = year % C
    d = ((D2 * a) + D3) % D1
    e = ((E2 * b) + (E3 * c) + (E4 * d) + 6) % E1
    f = d + e

    date = [(F1 + f), 'апреля'] if f <= 26 else [(f - 26), 'мая']

    # Вернуть полученную дату (список из числа и месяца).
    return date


if __name__ == '__main__':
    main()
