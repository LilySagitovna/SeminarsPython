'''1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

# num = input('Введите вещественное число: ')
#
# def summ(n):
#     sum = 0
#     for i in n:
#         if i != '.':
#             sum += int(i)
#     return sum
#
# print(summ(num))

'''2.Напишите программу, которая принимает на вход число N и
выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

# nu = int(input('Введите число: '))
# def mult(n):
#     i, j = 1, 2
#     lst = [1]
#     while i < n:
#         lst.append(j * lst[i - 1])
#         j += 1
#         i += 1
#     return lst
#
# print(mult(nu))

'''3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}'''

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

'''4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях. Позиции хранятся
 в файле file.txt в одной строке одно число.'''

# n = int(input('Введите число: '))
# spisok = list(range(-n, n+1))
# print(spisok)
# import for_dz
# new_a = for_dz.a-1
# new_b = for_dz.b-1
# print(f'Произведение {spisok[new_a]} и {spisok[new_b]} = {spisok[new_a] * spisok[new_b]} ')

'''5.Реализуйте алгоритм перемешивания списка.'''

# lst = list(range(1, 100, 4))
# # print(lst)
#
# import random
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