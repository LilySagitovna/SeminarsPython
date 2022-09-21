'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

# with open('file.txt', 'w') as data:
#     data.write('абвешка абв fsz wefef hello worldабв\n')
#
#
# with open('file.txt', 'r') as line:
#     old_data = line.read()
#
#
# def delt_char(text):
#     new_text = " ".join(filter(lambda x: 'абв' not in x, text.split()))
#     return new_text
#
#
# with open('file.txt', 'w') as new_line:
#     new_data = delt_char(old_data)
#     new_line.write(new_data)
#
#####################################################################################3
# # data_rez = open('file.txt', 'r')
# # for line in data_rez:
# #     print(line)
# #     print(" ".join(filter(lambda x: 'абв' not in x, line.split())))
# # data_rez.close()
#########################################################################################
# with open('file.txt', 'w+') as data:
#     data.writelines('абвешка абв fsz wefef hello worldабв\n')
#     data.seek(0, 0)
#     print('Иcходный текст: ')
#     print(data.readlines())
#     data.seek(0, 0)
#     data.write(" ".join(filter(lambda x: 'абв' not in x, data.readline().split())))
#     data.seek(0, 0)
#     print('Итоговый текст: ')
#     print(data.readlines()[1:])
#####################################################################################
# with open('file.txt', 'w+') as data:
#     data.writelines('абвешка абв fsz wefef hello worldабв\n')
#     data.seek(0, 0)
#     print('Иcходный текст: ')
#     print(data.readlines())
#     data.seek(0, 0)
#     replaced = data.readlines()[0].split()
#     replaced = [word for word in replaced if 'абв' not in word]
#
# with open('file.txt', 'w+') as data:
#     data.write(str(replaced))
#     data.seek(0, 0)
#     print('Итоговый текст: ')
#     print((' '.join(data.readlines())))
'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота. Достаточно сделать так, 
чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
b) Подумайте как наделить бота ""интеллектом"". 
Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. 
Достаточно довести игру до такой ситуации.'''

# вариант человека против человека:

# from random import randint
#
# candies = int(input('Введите общее количество конфет для игры: '))
# gamer1 = input('Введите имя первого игрока: ')
# gamer2 = input('Введите имя второго игрока: ')
# flag = randint(0, 2)
# if flag:
#     print(f'Первым ходит {gamer1}')
# else:
#     print(f'Первым ходит {gamer2}')
#
#
# def step_check(name):
#     number = int(input(f'{name}, введите количество конфет, которое возьмете, в диапазоне от 1 до 28: '))
#     if 1 <= number <= 28:
#         return number
#     else:
#         number = int(input("Необходимо взять конфеты в диапазоне от 1 до 28 шт.: "))
#         return number
#
#
# def step_print(name, numb, candy):
#     print(f'{name} взял {numb} конфет. В куче осталось {candy} конфет')
#
#
# while candies > 0:
#     if flag:
#         num = step_check(gamer1)
#         candies -= num
#         flag = False
#         step_print(gamer1, num, candies)
#     else:
#         num = step_check(gamer2)
#         candies -= num
#         flag = True
#         step_print(gamer2, num, candies)
# if flag:
#     print(f'Выиграл {gamer2}')
# else:
#     print(f'Выиграл {gamer1}')


##############################################################################################3
# вариант человека против бота:
#
# from random import randint
#
# candies = 51
# print(f'Играете против бота, на столе {candies} конфет.Выигрывает тот,кто забирает последние конфеты')
# step = randint(0, 2)
# while candies > 0:
#     if step:
#         if candies > 28:
#             bot_step = randint(0, 29)
#         else:
#             bot_step = randint(0, candies)
#         candies -= bot_step
#         print(f'Бот взял {bot_step} конфет, на столе осталось {candies}')
#         step = False
#     else:
#         people_step = int(input('Сколько конфет возьмете от 1 до 28? \n'))
#         if 1 <= people_step <= 28:
#             candies -= people_step
#             print(f'На столе осталось {candies} конфет')
#             step = True
#         else:
#             people_step = int(input('Введите количество от 1 до 28: '))
# if step:
#     print('Вы победили!)')
# else:
#     print('Вы проиграли(')

#####################################################################################################
# вариант игры с интеллектуальным ботом

def bot_calc(candy):
    step = 0 # бот должен брать такое кол-во чтобы в кучке оставалось нечетное количество в случае если бот ходит
    # первым , либо четное,если бот ходит вторым
    return step

from random import randint, randrange

candies = 51
print(f'Играете против бота, на столе {candies} конфет.Выигрывает тот,кто забирает последние конфеты')
flag = True
while candies > 0:
    if flag:
        if candies > 28:
            bot_step = bot_calc(candies)
        else:
            bot_step = candies
        candies -= bot_step
        print(f'Бот взял {bot_step} конфет, на столе осталось {candies}')
        flag = False
    else:
        people_step = int(input('Сколько конфет возьмете от 1 до 28? \n'))
        if 1 <= people_step <= 28:
            candies -= people_step
            print(f'На столе осталось {candies} конфет')
            flag = True
        else:
            people_step = int(input('Введите количество от 1 до 28: '))
if flag:
    print('Вы победили!)')
else:
    print('Вы проиграли(')

'''Создайте программу для игры в ""Крестики-нолики"".
Пример интерфейса:

   |   | 0
-----------    
   |   |
-----------
   | X |
Ввод можно реализовать через введение двух чисел (номеров строки и столбца).'''
# board = list(range(1,10))
#
# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)
#
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клеточка уже занята")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9 чтобы совершить ход.")
#
#
# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)
#
#
# main(board)


'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные первой и четвертой задач хранятся в отдельных текстовых файлах.'''

# with open('file_encode.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWBBBWWWWWWWWWWWWWWWBWWWWWWWWWWWW')
#
#
# def coding(text):
#     count = 1
#     res = ''
#     for i in range(len(text)-1):
#         if text[i] == text[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + text[i]
#             count = 1
#     if count > 1 or (text[len(text)-2] != text[-1]):
#         res = res + str(count) + text[-1]
#     return res
#
#
# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res
#
#
# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()
#
# with open('file_decode.txt', 'w') as file:
#     encoded_string = coding(decoded_string)
#     file.write(encoded_string)
#
# print(f"Текст после кодировки: {coding(decoded_string)}")
# print(f"Текст после дешифровки: {decoding(coding(decoded_string))}")
