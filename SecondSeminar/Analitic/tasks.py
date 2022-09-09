'''1. Напишите программу, которая принимает на вход число N и
выдаёт последовательность из N членов.
*Пример:*
- Для N = 5: 1, -3, 9, -27, 81
numberN = int(input('Введите число: '))
num = [1]
for i in range(1, numberN):
    num.append(num[-1] * -3)
print(num)

for i in range(int(input('Введите число: '))):
    print((-3)**i)'''

'''2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
*Пример:*
1, 4, 7, 10'''

size = 4
num = []
for i in range(size):
    num.append(3 * i + 1)
print(num)

size = 4
num = [3 * i + 1 for i in range(size)] #list comprehensions
print(num)

print([3 * i + 1 for i in range(size)])

'''3. Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
aaabba aa -> 2'''
element_One = [input('Введите первую строку: ')]
element_Two = [input('Введите вторую строку: ')]

if i