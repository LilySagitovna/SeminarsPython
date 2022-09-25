# from __future__ import print_function

# def print_list():  # вывести весь список в консоль
#     with open('data_base.csv', 'r') as base:
#         print(base.read())


# def print_list():  # вывести весь список в консоль
#     # import csv
#     import pandas
#     # with open('telefonsbook.csv', 'r', encoding='UTF-8') as base:
#     #     data = csv.reader(base, delimiter=',')
#     #     for row in data:
#     #         print(row)
#     csv = pandas.read_csv('telefonsbook.csv', delimiter=',')
#     print(csv)


# def search_surname(surname):  # поиск по фамилии (encoding="utf-8")
#     import io
#     with io.open('data_base.csv', 'r') as file:
#         search = False
#         for lin in file:
#             if surname in lin:
#                 print(lin, end='')
#                 search = True
#         if not search:
#             print('Такого контакта не найденно')


# def add_a_note(surname, name, lastname, tel, text):  # добавить запись в базу данных взяв их с консоли (нужно делать проверки на корректность введенных данных)
#     with open('data_base.csv', 'a+') as file:
#         file.write(surname + ' ')
#         file.write(name + ' ')
#         file.write(lastname + ' ')
#         file.write(tel + ' ')
#         file.write(text + '\n')


# def add_a_note(surname, name, lastname, tel, text):  # добавить запись в базу данных
# # Append Pandas DataFrame to Existing CSV File
# # importing pandas module
# import pandas as pd
# # data of Player and their performance
# data = {
#     'Фамилия': ['Hardik', 'Pollard', 'Bravo'],
#     'Run': [50, 63, 15],
#     'Wicket': [0, 2, 3],
#     'Catch': [4, 2, 1]
# }
#
# # Make data frame of above data
# df = pd.DataFrame(data)
#
# # append data frame to CSV file
# df.to_csv('GFG.csv', mode='a', index=False, header=False)
#
# # print message
# print("Data appended successfully.")


# def delete_entry(): # удалить запись с бд взяв с консоли
#     import re
#     with open('data_base.csv', 'r') as fi:
#         lines = fi.readlines()
#     delete = input('Введите фамилию: ')
#     pattern = re.compile(re.escape(delete))
#     with open('data_base.csv', 'w') as f:
#         for lin in lines:
#             result = pattern.search(lin)
#             if result is None:
#                 f.write(lin)


# def data_import(): # Импорт из какого-то файла csv (добавление в бд из файла другого в нескольких форматах,
#                       # а хранение в своем формате
#
# def data_export(): # Экспорт(Вывод данных в разных форматах столбиком или строчкой в другой файл c расширением txt или сsv?)



# print_list()

# surname = input('Введите фамилию: ')
# search_surname(surname)

# surnam = input("Фамилия: ")
# nam = input("Имя: ")
# lastnam = input('Отчество: ')
# telef = input("Телефон: ")
# txt = input('Описание: ')
# add_a_note(surnam, nam, lastnam, telef,txt)
