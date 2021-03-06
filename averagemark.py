#!/usr/bin/env python3
# Средний балл документа об образовании и его уровень

# Главная функция
def main():
    # Получить экзаменационные оценки для расчёта среднего балла
    # и вернуть полученную сумму всех балов и количество оценок,
    # а также наличие оценок "удовлетворительно"
    total, quantity, satisfactory = get_marks()
    if satisfactory > 0:
        print(f'У вас были оценки "удовлетворительно"')
        
    # Рассчитать средний балл документа об образовании
    average = calc_average(total, quantity)
    print(f'Ваш средний балл: {average:.2f}')
    
    # Определить уровень документа об образовании
    grade = determine_grade(average, satisfactory)
    
    # Показать пользователю уровень документа об образовании
    show_grade(grade)
    
    
# Функция для получения от пользователя экзаменационных оценок,
# расчёта суммы всех баллов, подсчёта количества всех оценок
# и определения наличия оценок "удовлетворительно"
# Сигнальной меткой для окончания ввода оценок является ввод числа 0
def get_marks():
    total = 0
    quantity = 0
    satisfactory = 0
    flag=True
    while flag:
        print('Необходимо ввести балл оценки (3, 4, 5) или 0 для окончания')
        try:
            mark = int(input('>>> Введите экзаменационную оценку: '))
            if mark not in [0, 3, 4, 5]:
                print('Ошибка! Ввод числа вне допустимого диапазона!')
            elif mark == 0:
                flag = False
                print('-------------------------------------')
            else:
                total += mark
                quantity += 1
                if mark == 3:
                    satisfactory += 1
        
        except ValueError:
            print('Ошибка! Нужно было ввести целое число!')
                
    return total, quantity, satisfactory


# Функция получает сумму всех баллов и количество экзаменационных оценок
# для расчёта среднего балла документа об образовании
def calc_average(total, quantity):
    average = 0
    try:
        average = total / quantity
    except ZeroDivisionError:
        print('Данных недостаточно для расчёта')        
    
    return average


# Функция определяет уровень документа об образовании на основании
# среднего балла и наличия оценок "удовлетворительно"
# Уровни соответствуют:
# АA - диплом с отличием и среднему баллу 5.0
# AB - диплом с отличием (средний балл от 4.75, нет удовлетворительных оценок)
# BB - диплом без отличия
# CC - уровень не может быть определён
def determine_grade(average, satisfactory):
    grade = 'LEVEL'
    if average == 0:
        grade = 'CC'
    elif average == 5.0:
        grade = 'AA'
    elif (average >= 4.75 and average < 5.0) and (satisfactory == 0):
        grade = 'AB'
    else:
        grade = 'BB'
    
    return grade


# Функция показывает пользователю уровень документа об образовании
def show_grade(grade):
    if grade == 'AA':
        print('Вы получаете диплом с отличием и значок "Отличник учёбы"')
    elif grade == 'AB':
        print('Вы получаете диплом с отличием')
    elif grade == 'BB':
        print('Вы получаете диплом без отличия')
    else:
        print('Уровень документа об образовании не может быть определён...')
        print('Попробуйте ввести данные ещё раз')

# Вызвать главную функцию
if __name__ == '__main__':
    main()
