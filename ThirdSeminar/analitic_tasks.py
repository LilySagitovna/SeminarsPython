'''def func(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    tmp = []
    while start < stop:
        tmp.append(start)
        start += step
    return tmp


print(func(12, 5, 6))

t = """Hello
friend
wq
qwe
wqe wqe qwe
"""

print(', '.join(t.split()))


mem = {1: 1, 2: 1}


def fib(n):
    if n not in mem:
        mem[n] = fib(n - 1) + fib(n - 2)  кеширование чтобы запоминал то,что уже сделал
    return mem[n]


print(fib(500))
/////////////////////////////////////////

from random import randrange, randint, random

print(randint(1, 5))
print(randrange(1, 5))
print(random())

from time import time

print(time())
'''
'''1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
#from time import time
# print(time())
# a = str(time())
# print(int(a[16])**4 % 100)
'''
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
# exit()
'''2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.'''
# a= ["qwe", "asd", "zxc","67", "qwe", "ertqwe"]
# for i in a:
#     if i.isdigit():
#         print('Да')



'''3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
*Пример:*
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1

a=["йцу", "фыв", "ячс", "цук", "йцукен"]
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
'''

list

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))

'''Дан список чисел. Определите, сколько в нем встречается различных чисел.'''
lst = list(map(float, input("Введите числа через пробел:\n").split()))

lst = [1, 5, 2, 2, 2, 4]
for i in range(len(lst)):
    if lst[i] !=


