# with open('data_base.csv', 'w+') as data:
#     data.write('Петров Иван Иванович 89174562456 коллега\n')
#     data.write('Кукушкин Авдон Авдеевич 89189522335 юрист\n')
#     data.write('Любимцев Исхак Исхакович 89873214598 историк\n')



import csv
with open("telefonsbook.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Фамилия", "Имя", "Отчество", "Телефон", "Описание"])
    file_writer.writerow(["Петров", "Иван", "Иванович", "89174562456", "коллега"])
    file_writer.writerow(["Кукушкин", "Авдон", "Авдеевич", "89189522335", "юрист"])
    file_writer.writerow(["Любимцев", "Исхак", "Исхакович", "89873214598", "историк"])
