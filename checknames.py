# Поиск имени в списках самых популярных имён
# девочек и мальчиков в США

def main():
    # Получить список самых популярных имён девочек
    # и вывести его в распакованном виде
    girl_names = get_names('GirlNames.txt')
    print('Список самых популярных имён девочек в США:', *girl_names)
    
    # Получить список самых популярных имён мальчиков
    # и вывести его в распакованном виде
    boy_names = get_names('BoyNames.txt')
    print('\nСписок самых популярных имён мальчиков в США:', *boy_names)
    
    # Получить поисковый запрос от пользователя
    search_girl_names, search_boy_names = get_search_query()
    
    # Инициализировать флаги для поиска
    # и определить, в каких списках надо искать имена
    girl_names_query = False
    boy_names_query = False
    
    if search_girl_names != 'n':
        girl_names_query = True
    else:
        print('Самые популярные имена девочек не ищем!')
        
    if search_boy_names != 'n':
        boy_names_query = True
    else:
        print('Самые популярные имена мальчиков не ищем!')
    
    # Произвести поиск в определённых пользователем списках имён
    # и показать результат
    print('\nРезультат поиска в списке самых популярных имён:')
    if girl_names_query:     
        if boy_names_query:
            search_result_girls = search_names(search_girl_names,
                                                    girl_names)
            print(f'\t- имя девочки {search_result_girls}!') 
            search_result_boys = search_names(search_boy_names,
                                                   boy_names)
            print(f'\t- имя мальчика {search_result_boys}!') 
        else:
            search_result_girls = search_names(search_girl_names,
                                                    girl_names)
            print(f'\t- имя девочки {search_result_girls}!')
    elif boy_names_query:
        search_result_boys = search_names(search_boy_names,
                                               boy_names)
        print(f'\tимя мальчика {search_result_boys}!')
    else:
        print(f'\tничего не найденo, так как запроса искать не было!')


# Функция получает популярные имёна из файла и возвращает список имён
def get_names(filename):
    # Создать пустой список для записи имён
    names = []
    
    # Открыть файл с именами для чтения
    outfile = open(filename, 'r')
    
    # Записать имена в список
    for name in outfile:
        names.append(name.rstrip('\n'))
    
    # Закрыть файл
    outfile.close()
    
    # Вернуть список имён
    return names


# Функция получает и возвращает запросы от пользователя на поиск имён
def get_search_query():
    # Получить поисковые запросы
    print('\nДля поиска в списках самых популярных имён введите имя')
    print('(или "n", если имя девочки/мальчика искать не надо):')
    first_query = input('\t- для девочки >>> ')
    second_query = input('\t- для мальчика >>> ')
    
    # Вернуть поисковые запросы
    return first_query, second_query


# Функция ищет имя по запросу в списке популярных имён
def search_names(query, list_name):
    # Инициализировать переменную для результатов поиска
    result = 'не найдено'
    
    # Произвести поиск
    if query in list_name:
        result = 'найдено'
        
    # Вернуть результат поиска
    return result


# Вызвать главную функцию
if __name__ == '__main__':
    main()    
