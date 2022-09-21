# file1 = '5x^5 + 3 x ^ 2 + 3 * x - 22 * x^7 - 77'
# file2 = '3x^2 - 2x + 5'
#
#
# def get_ones(line):
#     tmp = []
#     last = 0
#     positive = True
#     for i, item in enumerate(line):
#         if item in {'+', '-'}:
#             if positive:
#                 tmp.append(line[last:i])
#             else:
#                 tmp.append('-' + line[last:i])
#             last = i + 1
#             positive = item == '+'
#
#     if positive:
#         tmp.append(line[last:])
#     else:
#         tmp.append('-' + line[last:])
#     return tmp
#
#
# def get_coef(one):
#     for i, item in enumerate(one):
#         if item == 'x':
#             return int(one[:i]), one[i:]
#     return int(one), None
#
#
# lst1 = get_ones(file1.replace(' ', '').replace('*', ''))
# lst2 = get_ones(file2.replace(' ', '').replace('*', ''))
#
# dct1 = {item[1]: item[0] for item in map(get_coef, lst1)}
# dct2 = {item[1]: item[0] for item in map(get_coef, lst2)}
#
# print(dct1)
# print(dct2)


'''1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.'''

# line = "1 3 4 5 6"
# lst = list(map(int, line.split()))
# for i in range(len(lst)-1):
# if lst[i+1]- lst[i] > 1:
# n = lst[i]+1
# print(n)


# lst = '1 2 4 5'
# lst = list(map(int, lst.split()))
# print(lst)
#
#
# def f(lst2):
# i = 1
# a = 0
# while i < len(lst2):
# if lst2[i]-1 != lst2[i-1]:
# a = lst2[i-1]+1
# i+=1
# return (a)
#
#
# print(f(lst))

'''2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
Порядок элементов менять нельзя.
*Пример:*
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.'''
lst = [1, 5, 2, 3, 4, 6, 1, 7]



def posled(spisok):
    new_list = []


'''3. Напишите программу, удаляющую из текста все слова, содержащие "абв".'''

stroka = 'абвешка абв fsz wefef hello worldабв'
print(" ".join(filter(lambda x: 'абв' not in x, stroka.split())))