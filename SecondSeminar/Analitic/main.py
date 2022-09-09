# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# a = 5.0999
# print(int(a * 100) / 100)
#
#
# b = '{}, {}.'
# print(b.format('Hello', 'Lily'))
# print(b.format('Bye - bye', input("Представьтесь: ")))
# name = 'Lily'
# print(f'Hello, {name}')
#
# print(r'Hello, {name}')  #все в строку превращает
# print(u'Hello, {name}') #юникодная строка
# print(f'Hello,\nSergey')

'''def func(a, b):
    print(f'Вы ввели: {a} {b}')
    return a + b


a = func(int(input()), int(input()))
print(func)
print(a)'''

a = 99
def func():
    global a
    a = 22
    print(f'Вы ввели: {a}')


print(a)


from copy import deepcopy


a = [[1], 2, 3]

b = deepcopy(a) # b = a.copy()

print('a =', a)
print('b =', b)

a[0].append(4)
b[0].append(5)

print('a =', a)
print('b =', b)

a.append(9)
b.append(8)

print('a =', a)
print('b =', b)
