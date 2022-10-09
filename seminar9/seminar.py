# # import emoji
# #
# #
# # print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#
# '''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''
#
# import telebot
#
# TOKEN = '5728083512:AAFs6oRV_0KsEn5_v-S7nQ2zKEc_uTqTsDI'
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start_answer(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=f'Вы прислали команду: {msg.text}')
#
#
# @bot.message_handler()
# def answer(msg: telebot.types.Message):
#     new_text = " ".join(filter(lambda x: 'абв' not in x, msg.text.split()))
#     bot.send_message(chat_id=msg.from_user.id, text=new_text)
#
#
# bot.polling()
#
#
#
# # вариант человека против бота:
# #
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
