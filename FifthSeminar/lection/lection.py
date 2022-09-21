# # def sum(x, y):
# #     return x+y
#
# # f = sum
# # sum = lambda x, y: x+y + 1
#
# def mult(x, y):
#     return x*y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)
#
#
# calc(mult, 4, 5)
# # calc(f, 4, 5)
# # calc(sum, 4, 5)
# calc(lambda x, y: x+y + 1, 4, 5)


# lis = []
# for i in range(1, 21):
#     # if i % 2 == 0:
#         lis.append(i)
#
# print(lis)
#
# ls = [i for i in range(1, 21)]
# print(ls)
#
# lst = [i for i in range(1, 21) if i % 2 == 0]
# print(lst)
#
# lst = [(i, i) for i in range(1, 21) if i % 2 == 0] # пары кортежей список
# print(lst)
#
# def f(x):
#     return x**3
#
# lst = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(lst)
#
# # кортежи
# lst = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(lst)


# import file.py
# lst = file.py


# def f(x):
#     return x ** 2
#
#
# lst = [1, 2, 3, 5, 8, 15, 23, 38]
#
# # with open('file.py', 'r')
# lst_my = [(i, f(i)) for i in lst if i % 2 == 0]
# print(lst_my)
#
#
#
#
# # path = путь к файлу
# # f = open(path, 'r')
# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()
#
# numbers = []
#
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)







def select(f, col):
 return [f(x) for x in col]

def where(f, col):
 return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)

res = where(lambda x: not x % 2, res)

res = select(lambda x: (x, x**2), res)
print(res)



# data = '1 2 3 5 8 15 23 38'.split()
# li = [x for x in range(1,20)]
# li = list(map(lambda x: x * 10, li))
# print(li)
#
# data = list(map(int, input().split()))
# print(data)
#
#
#
# data = map(int, '1 2 3 5 8 15 23 38'.split())
# for e in data:
#  print(e)
#
# print('---')
#
# for e in data:
#  print(e)



data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)




data = [x for x in range(1,20)]
res = list(filter(lambda x: not x % 2, data))

users = ['u1', 'u2', 'u3', 'u4', 'u5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]


data = list(zip(users, ids, salary))
print(data)


users = ['u1', 'u2', 'u3', 'u4', 'u5']
data = list(enumerate(users))
print(data)



