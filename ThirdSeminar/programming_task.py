# lst = [int(i) for i in input().split()]
# lst = list(map(int, input().split()))
# print(lst)

'''Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в
списке.
Входные данные  1 2 2 3 3 3
Выходные данные 1'''

# lst = [int(i) for i in input().split()]
# lst2 = []
#
# for i in lst:
#     if lst.count(i) == 1:
#         lst2.append(i)
# print(*lst2)

# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента.

# lst = [int(i) for i in input().split()]
#
# for i in range(len(lst)):
#     if lst[i] > lst[i - 1]:
#         print(lst[i])

# Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.

# from time import time
#
# print(time())
# print(type(time()))
# def run(n):
#     a = time()
#     b = int(a)
#     c = (a - b) * 10
#     print(int((b**c) % n))
#
# run(20)

# Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.

# lst = [i for i in input().split()]
# n = int(input('Введите число: '))
# flag = 0
#
# for i in lst:
#     if i.find(str(n)) != -1:
#         print('Yes')
#         break
#     else:
#         flag += 1
# if flag == len(lst):
#     print('No')

# Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.

# lst = [i for i in input().split()]
# n = input('Введите строку: ')
# f = 0
#
# for i in lst:
#     i.find()

# a=["йцу", "фыв", "ячс", "цук", "цук", "йцукен"]
# b= input('Введите искомый элемент: ')
# count = 0
# for i in range(len(a)):
#     if a[i] == b:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# else:
#     print(-1)

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# lst = [i for i in input().split()]
# set1 = set(lst)
# print(len(set1))

# Даны два списка чисел. Найдите все числа, которые входят как в первый,
# так и во второй список и выведите их в порядке возрастания.

# lst = [int(i) for i in input().split()]
# lst2 = [int(i) for i in input().split()]
#
# print(sorted(set(lst)&set(lst2)))
# print(sorted(set(lst)|set(lst2)))

"""
Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:
MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..'}
Входные данные
Выходные данные
Help me SOS
.... . .-.. .--.
-- .
... --- ...
"""

# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#          'D': '-..', 'E': '.', 'F': '..-.',
#          'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..',
#          'M': '--', 'N': '-.', 'O': '---',
#          'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-',
#          'V': '...-', 'W': '.--', 'X': '-..-',
#          'Y': '-.--', 'Z': '--..'}
#
# help = 'Help me SOS'.upper()
#
# for i in help:
#     if i in MORSE:
#         print(MORSE[i], end='')
#     else:
#         print('\n')

"""
Для каждого слова исходного текста выведите одно целое число — номер
вхождения этого слова в текст. Числа выведите через пробел. Количество
чисел должно совпадать с количеством слов в исходном тексте.
Входные данные
Раз раз раз как меня слышно Повторяю раз раз раз
Повторяю
Выходные
данные
1 1 2 1 1 1 1 3 4 5 2
"""

num_dict = {}

lst = input('Введите: ').split(' ')

for i in lst:
    # if i not in num_dict:
    #     num_dict[i] = 1
    # else:
    #     num_dict[i] += 1
    num_dict[i] = num_dict.get(i, 0) + 1
    print(num_dict[i])