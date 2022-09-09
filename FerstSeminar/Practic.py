# Семинар Аналитика
# a = input()
# while a != '0':  # пока не напишут ноль
#     print(a * 2)  # удваивай то что написано
#     a = input()
# while '0' not in a:  # пока не напишут ноль внутри строки
#     print(a * 2)
#     a = input()

# a = [1, 2, 3, 4, 5]
# for item in a:
#     print(item)
# for index in range(len(a)):
#     print(a[index])

# index = 0
# while index < len(a):
#     print(a[index])
#     index += 1

# a.extend([44,'3']) - расширяет в конец из какого-то списка в список
# a.appened(2,4) - добавляет в конец списка вставляет списка вкладывает
# a.insert(2,3)  - вставка в середине списка на место позиции  два вставить цифру 3
# print(dir(a)) -  какие есть методы встроенные
# print(help(list.append)) - информация о методе, что делает
# import this - дзен послание
# elif

# print (*range (3,17,4) -  итератор, от 3 до 17 с шагом 4. можно без шага и без * (распаковки)
# способ получения последовательно каких-то значений
# print(*range(len(a))  - получить длину индексов нашего списка
'''
1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

*Примеры:*

- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет

a, b = map(int, input().split()) принимает числа в одну строку
if a/b ==b: print(a квадрат b)
elif b/a == a: print( b квадрат a)
else: print('NO')

Решение:
a = int(input('Введите число '))
b = int(input('Введите число '))
if (b == (a ** 2)) or (a == (b ** 2)):
    print('Yes')
else:
    print('No')


2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
Примеры:
    
- 1, 4, 8, 7, 5 -> 8
-78, 55, 36, 90, 2 -> 90

m = int(input())
for i in range(4):
    tmp = int(input())
    if tmp > m:
    m = tmp
print(m)


n = map(int, input().split(', '))
print(n)
p = max(n)
print(p)
'''

lst = []
for i in range(5):
    lst.append(int(input()))
    mx = lst[0]
for k in lst:
    if k>mx:
        mx = k
    else: k + 1
print(mx)
