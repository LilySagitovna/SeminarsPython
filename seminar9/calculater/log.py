import telebot
import xlsxwriter
import datetime as dt

# count = 1


def log(message):
    file = open('log.csv', 'a')
    file.write(f'{str(dt.datetime.now().date())}, {str(dt.datetime.now().time())[0:8]}, {message.from_user.id}')
    file.close()
# workbook = xlsxwriter.Workbook('log.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write(0, 0, 'Date')
# worksheet.write(0, 1, 'Time')
# worksheet.write(0, 2, 'Вид сообщения')
# worksheet.write(0, 3, 'Отправитель')
# worksheet.write(0, 4, 'ID отправителя')
# worksheet.write(0, 5, 'Сообщение')
# bot = telebot.TeleBot('5728083512:AAFs6oRV_0KsEn5_v-S7nQ2zKEc_uTqTsDI')


# @bot.message_handler(content_type=['text'])
# def send_text(message):
#     print(message)
#     global count
#     if message.content_type == 'text':
#         if message.text != 'stop':
#             worksheet.write(count, 0, str(dt.datetime.now().date()))
#             worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
#             worksheet.write(count, 2, 'текст')
#             worksheet.write(count, 3, message.from_user.first_name + ' ' + message.from_user.last_name)
#             worksheet.write(count, 4, message.from_user.id)
#             worksheet.write(count, 5, message.text)
#             count += 1
#         else:
#             workbook.close()
#
#
# bot.polling(none_stop=True)
