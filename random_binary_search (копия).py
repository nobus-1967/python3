import random


def main():
    """Программа осуществляет бинарный поиск числа в массиве."""
    array = get_array()
    if array is None:
        print('Работа программы прекращена')
        return
    else:
        print(f'\nИсходный массив для поиска: {array}')
        array_to_clear = set(array)
        array_to_search = list(array_to_clear)
        array_to_search.sort()
        print(f'Без учёта повторяющихся элементов: {array_to_search}')
        
        num = get_number()
        if num is None:
            print('Работа программы прекращена.')
            return
        else:
            result = binary_search(array_to_search, num)
            if result:
                print(f'\nЧисло {num} найдено.')
            else:
                print(f'\nЧисло {num} не найдено.')   
   
    
def get_array():
    """Функция возвращает упорядоченный массив из n=items элементов."""
    try:
        low = int(input('Введите нижний диапазон числового массива: '))
        high = int(input('Введите верхний диапазон числового массива: '))
        if high < low:
            print('Неправильно задан диапазон (верхний меньше нижнего)!')
            raise ValueError
        
        items = int(input('Введите количество генерируемых элементов: '))      
    except ValueError:
        print('Неверный ввод данных!')
    else:
        new_array = [random.randint(low, high) for item in range(items)]
        new_array.sort()
        
        return new_array


def get_number():
    """Функция возвращает введённое пользователем число для поиска."""
    try:
        number = int(input('\nВведите число для поиска в массиве: '))
    except ValueError:
        print('Неверный ввод!')
    else:
        return number    


def binary_search(array, number):
    """Функция возвращает результаты бинарного поиска числа."""
    result = False
    if number < array[0] or number > array[-1]:
        return result
    else:
        if len(array) == 1:
            if array[0] == number:
                result = True

            return result
        else:
            middle = len(array) // 2
            left = array[:middle]
            right = array[middle:]
            
            if array[middle] == number:
                return True
            elif array[middle] < number:
                return binary_search(right, number)
            else:
                return binary_search(left, number)
       

if __name__ == '__main__':
    main()    
