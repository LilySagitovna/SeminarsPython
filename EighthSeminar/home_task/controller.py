import function
import view


def button_click():
    while True:
        view.menu()
        data = view.control_menu()
        if data == 1:
            function.print_list()
        if data == 2:
            surname = input('Введите фамилию: ')
            # if " " not in surname and surname.isalpha():
            function.search_surname(surname)
            # else:
            #     print('Некорректный ввод! ')
        if data == 3:
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            lastname = input('Введите отчество: ')
            tel = input('Введите номер телефона: ')
            text = input('Введите должность: ')
            if (" " not in surname and surname.isalpha() and
                " " not in name and name.isalpha() and
                " " not in lastname and lastname.isalpha() and
                " " not in tel and tel.isdigit() and
                    " " not in text and text.isalpha()):
                function.add_a_note(surname, name, lastname, tel, text)
            else:
                print('Некорректный ввод!')
        if data == 4:
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            lastname = input('Введите отчество: ')
            if (" " not in surname and surname.isalpha() and
                " " not in name and name.isalpha() and
                    " " not in lastname and lastname.isalpha()):
                function.delete_entry(surname, name, lastname)
            else:
                print('Некорректный ввод!')
        if data == 5:
            file = input('Введите наименование файла с расширением: ')
            if "." in file:
                function.data_import(file)
            else:
                print('Некорректный ввод!')
        if data == 6:
            function.data_export()
        if data == 7:
            function.exit_program()
            break
        function.back_to_menu()

#     main = view.menu()
#     data = view.control_menu()
#     if data:
#         return {
#             1: function.print_list,
#             2: function.search_surname,
#             3: function.add_a_note,
#             4: function.delete_entry,
#             5: function.data_import,
#             6: function.data_export,
#             7: function.exit_program,
#         }.get(data, 'error')
#
#
# button_click()


