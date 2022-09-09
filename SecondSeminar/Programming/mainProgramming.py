'''1 Даны три целых числа. Определите, сколько среди них совпадающих. Программа
должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0
(если все числа различны).
Входные данные 10,5,10
Выходные данные 2'''
'''a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('3')
elif a == b or a == c or b == c:
    print('2')
elif a != b and a != c and b != c:
    print('0')'''

'''2 Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B
включительно, в порядке убывания. В этой задаче можно обойтись без инструкции
if.
Входные данные 7,1
Выходные данные 7 5 3 1'''

'''a = 7
b = 1
while a >= b:
    if a % 2 != 0:
        print(a)
    a -= 1
///////////////////////////////
a = 7
b = 1
for i in range(a, b):
    if a % 2 != 0:
        print(a)
    a -= 1
    ////////////////////////
a = int(input())
b = int(input())
for i in range(a - (a+1)%2, b - b%2, 2)
    print(i, end = ' ')
    '''

'''3 Напишите программу, которая принимает на вход число N и выдаёт
последовательность из N членов.
Пример:
Для N = 5: 1, -3, 9, -27, 81'''

'''n = int(input("n = "))
ls = [1]
for i in range(n):
    print((-3) ** i)'''

'''4 Напишите программу, которая проверяет пятизначное число на палиндром.'''

'''ls = input()
if ls[0] == ls[4] and ls[1] == ls[3]:
    print('Палиндром')
else:
    print('Не палиндром')
    ///////////////////
n = input()
print(n == n[::-1])
////////////////////////
num = int(input())
palindrome = True
for i in range(len(num) // 2):
    if num[i] != num[-i-1]:
        palindrome = False
        break
if palindrome:
    print('Палиндром')
else:
    print('Не палиндром') 
    '''

'''5 Удалить вторую цифру трёхзначного числа.'''

'''n = int(input('n = '))
if n > 99:
    n1 = n // 100
    n2 = n % 10
    print(n1 * 10 + n2)'''

'''6 Напишите программу, в которой пользователь будет задавать две строки, а
программа - определять количество вхождений одной строки в другой.'''

'''first = input()
second = input()
count = 0
s = 0
for i in first:
    if i == second[0]:
        vhozd = True
        j = s
        for k in second:
            if j == len(first):
                vhozd = False
                break
            if k != first[j]:
                vhozd = False
            j += 1
        if vhozd:
            count += 1
    s += 1
print(count)'''

string = input()
find = input()
count = 0
i= 0
while i< len(string):
    if string[i:+len(find)] == find:
        count+=1
        i+= len(find)
    else:i+=1
print(count)

print(string.count(find))



'''1 По данному целому числу N распечатайте все квадраты натуральных чисел, не
превосходящие N, в порядке возрастания.
Входные данные 50
Выходные данные 1,4,9,16,25,36,49'''

'''n = 50
for i in range(1, n + 1):
    res = i ** 2
    if res < n:
        print(res)
    else:
        break
    ////////////////////////////////////    
n = int(input())
i = 1
while i ** 2 < n:
    print(i ** 2)
    i+=1
'''

'''2 Определите среднее значение всех элементов последовательности,
завершающейся числом 0
Входные данные 1,7,9,0
Выходные данные 5.666666666666667'''

'''i = True
summ = 0
count = 0 # -1
while i:
    i = int(input())
    if i != 0: # тогда это не надо
        summ += i
        count += 1
    else: # тогда это не надо
        break # тогда это не надо
print(summ)
print(count)        
print(summ / count)'''

'''Дан список чисел определите сколько в данном списке чисел, которые больше двух своих соседних,
и выведите количество. Крайние элементы никогда не учитываются так как у них не достаточно соседей'''
'''lst = [2, 7, 9, 2, 6, 4]
i = 0
count = 0
for j in lst:
    if i != 0 and i != len(lst) - 1:
        if lst[i - 1] < j > lst[i + 1]:
            count += 1
    i += 1
print(count)
////////////////////////
s = input()
i = 0
res = 0
for n in s:
    if i != 0 and i != len(lst) - 1:
        if int(n) > int(lst[i - 1]) and int(n) > int(lst[i + 1]):
            res += 1
    i += 1
print(res)'''
'''
s = input()
result = ''
for i in range(1, len(s), 2):
    result+= s[i] + s[i-1]
if len(s)%2 !=0:
    result += s[-1]
print(result)'''
