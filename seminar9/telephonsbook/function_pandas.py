import pandas


def print_list():  # вывести весь список в консоль
    with open('data_base.csv', 'r', encoding='UTF-8') as base:
        return base.read()


def search_surname(surname):  # поиск по фамилии (encoding="utf-8")
    csv = pandas.read_csv('data_base.csv', delimiter=',')
    csv_tall = csv[csv['Фамилия'] == surname]
    # if csv_tall == surname:
    return csv_tall
    # else:
    #     print('Такого сотрудника нет!')


# def search_surname(surname, name, lastname):  # поиск по фамилии (encoding="utf-8")
#     csv = pandas.read_csv('data_base.csv', delimiter=',')
#     csv_tall = csv[(csv['Фамилия'] == surname) & (csv['Имя'] == name) & (csv['Отчество' == lastname])]
#     print(csv_tall)
#     csv_tall = csv_tall.drop()


def add_a_note(surname, name, lastname, tel, text):  # добавить запись в базу данных
    # csv = pandas.read_csv('data_base.csv', delimiter=',') - а если у одного сотр несколко номеров тел, или наоборот у нес сотр один номер тел
    # if csv[csv['Фамилия'] != surname]:
    # data of Player and their performance
    datas = {
        'Фамилия': [surname],
        'Имя': [name],
        'Отчество': [lastname],
        'Телефон': [tel],
        'Описание': [text]
    }
# Make data frame of above data
    add = pandas.DataFrame(datas)
# append data frame to CSV file
    add.to_csv('data_base.csv', mode='a', index=False, header=False)
# print message
    print("Data appended successfully.")
    # else:
    #     print('Такой сотрудник уже есть в базе данных!')


def delete_entry(surname, name, lastname):  # удалить запись с бд взяв с консоли
    csv = pandas.read_csv('data_base.csv', delimiter=',')
    # if csv[csv['Фамилия'] == surname]:
    df = csv[::]
    df = df.drop(df[(df.Фамилия == surname) & (df.Имя == name) & (df.Отчество == lastname)].index)
    df.to_csv('data_base.csv', index=False,)
    print('Готово! Удаление произойдет после выхода из программы.')
    # else:
    #     print('Такого сотрудника в базе данных не существует!')


def data_import(file):  # Импорт из какого-то csv файла
    df = pandas.read_csv(file)
    add = pandas.DataFrame(df)
    add.to_csv('data_base.csv', mode='a', index=False)


def data_export():  # Экспорт
    df = pandas.read_csv('data_base.csv', delimiter=',')
    df.to_csv('Export.txt', sep='\t', encoding='utf-8')
