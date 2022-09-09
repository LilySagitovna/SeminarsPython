'''Задание 1 Напишите программу, которая принимает на
вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11'''
import random

# def summ(num=input('Введите вещественное число: ')):
#     sum = 0
#     for i in num:
#         if i != '.':
#             sum += int(i)
#     return sum
#
#
# print(summ())

'''Задание 2 Напишите программу, которая принимает на 
вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

# n = int(input('Введите число: '))
# def mult(n):
#     i, j = 1, 2
#     lst = [1]
#     while i < n:
#         lst.append(j * lst[i - 1])
#         j += 1
#         i += 1
#     return lst
# print(mult(n))

'''Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072'''

# num = int(input('Введите число: '))
#
# def spisok_posl(n):
#     tls = []
#     for i in range(1, n+1):
#         tls.append(round((1 + 1 / i) ** i, 3))
#     return tls
#
#
# def smm(ls):
#     sm=0
#     for i in range(len(ls)):
#         sm += ls[i]
#     return sm
#
# res = spisok_posl(num)
# print(f'{res}  Сумма = {smm(res)}')

# ///////////////////////////////////////////////////////////////
# n = int(input('Enter number: '))
#
# def sequence(n):
#     return[round((1 + 1 / x)**x, 3) for x in range(1, n + 1)]
#
# print(sequence(n))
# print(round(sum(sequence(n)), 3))

'''Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.'''

# n = int(input('Введите число: '))
# spisok = list(range(-n, n+1))
# print(spisok)
# # a = int(input('Введите номер позиции первого числа: '))
# # b = int(input('Введите номер позиции первого числа: '))
# # print(f'Произведение {spisok[a-1]} и {spisok[b-1]} = {spisok[a-1] * spisok[b-1]} ')
# import for_dz
# new_a = for_dz.a-1
# new_b = for_dz.b-1
# print(f'Произведение {spisok[new_a]} и {spisok[new_b]} = {spisok[new_a] * spisok[new_b]} ')

'''Задание 5 Реализуйте алгоритм перемешивания списка.'''
# lst = list(range(1, 100, 4))
# print(ls)
#
# def mix_list(ls):
#     new_ls = ls.copy()
#     for i in range(len(new_ls)):
#         ind_rand = random.randint(0, len(new_ls) - 1)
#         temp = new_ls[i]
#         new_ls[i] = new_ls[ind_rand]
#         new_ls[ind_rand] = temp
#     return new_ls
#
#
# print(mix_list(lst))

'''Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
Пример
-Для "abababb" и "aba" -> 2'''

# stroka = "abababb"
# search = "aba"
# count = 0
# i = 0
# while i < len(stroka):
#     if stroka[i:i + len(search)] == search:
#         count += 1
#         i += 1
#     else:
#         i += 1
# print(count)
