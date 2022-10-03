import csv
with open("data_base.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Фамилия", "Имя", "Отчество", "Телефон", "Должность"])
    file_writer.writerow(["Петров", "Иван", "Иванович", "89174562456", "маркетолог"])
    file_writer.writerow(["Кукушкин", "Авдон", "Авдеевич", "89189522335", "юрист"])
    file_writer.writerow(["Любимцев", "Исхак", "Исхакович", "89873214598", "бухгалтер"])
    file_writer.writerow(["Ромашкова", "Роза", "Васильковна", "89873214598", "менеджер"])
    file_writer.writerow(["Добрыня", "Мира", "Смельчакова", "89873214598", "аналитик"])
