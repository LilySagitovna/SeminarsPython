# with open('my_file.txt', 'r') as f:
#     lines = list(f.readlines())
# print(1, lines)
# print(2, lines)

'''Укус Питона - https://myrobot.ru/downloads/a_byte_of_python.php
Грокаем алгоритмы - https://codernet.ru/books/software_development/grokaem_algoritmy/
Изучаем Python. 5-е изд. Том 1 - https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_1_mark_lutc/
Изучаем Python. 5-е изд. Том 2 - https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_2_mark_lutc/
Остальные книги - https://codernet.ru/books/python/'''

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# stroka = input('Данные: ').split()
# max_ = int(stroka[0])
# min_ = int(stroka[0])
#
# for i in stroka:
#     num = int(i)
#     if num > max_:
#         max_ = num
#     elif num < min_:
#         min_ = num
# print(max_, min_)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0

# def my_function(a, b, c):
#     if a != 0:
#         discr = b ** 2 + 4 * (a * c)
#         if discr > 0:
#             x1 = (-b - discr ** 0.5) / (2 * a)
#             x2 = (-b + discr ** 0.5) / (2 * a)
#             return x1, x2
#         elif discr == 0:
#             x = -b / (2 * a)
#             return x
#         elif discr < 0:
#             return None
#
# print(my_function(2, 4, 1))
#
# def my_function(a, b, c):
#     if a != 0:
#         discr = b ** 2 + 4 * (a * c)
#         if discr > 0 or discr < 0:
#             x1 = (-b - discr ** 0.5) / (2 * a)
#             x2 = (-b + discr ** 0.5) / (2 * a)
#             return x1, x2
#         elif discr == 0:
#             x = -b / (2 * a)
#             return x
#
# print(my_function(2, 4, 1))

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd

def my_gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return my_gcd(a - b, b)
    else:
        return my_gcd(b - a, a)


def lcm(a, b):
    return abs(a * b) / my_gcd(a, b)

print(lcm(17, 34))