
def menu():
    print("Вот что я умею: ")
    print('''Меню:
    1 Вывести весь список сотрудников
    2 Поиск сотрудника по фамилии
    3 Добавить запись в базу данных
    4 Удалить запись с базы данных
    5 Импорт из csv файла
    6 Экспорт в csv файл
    7 Выход из базы данных
      ''')


def control_menu():
    while True:
        number = input('Выберите нужное действие (номер цифры): ')
        if number.isdigit():
            number = int(number)
            if 0 < number < 8:
                return number
            else:
                print('Введите правильный выбор в меню')
                continue
        print('Вы ввели не цифру! Начните сначала!')
        continue


# validation of input
