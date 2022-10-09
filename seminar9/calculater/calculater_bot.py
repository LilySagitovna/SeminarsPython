import telebot
from telebot import types
import xlsxwriter
import datetime as dt
import log

bot = telebot.TeleBot('5728083512:AAFs6oRV_0KsEn5_v-S7nQ2zKEc_uTqTsDI')
value = ''  # хранит текущее знчение калькулятора
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()  # создание кнопок
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),  # создание строк кнопок
             telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


# Обработчик событий, когда боту придет команда
@bot.message_handler(commands=['start', 'calculater'])
def get_message(message):
    log.log(message)
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


# обработчик событий, который будет вызван при нажатии на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_func(qwery):
    global value, old_value
    data = qwery.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=qwery.message.chat.id, message_id=qwery.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=qwery.message.chat.id, message_id=qwery.message.message_id, text=value, reply_markup=keyboard)
            old_value = value

    old_value = value
    if value == 'Ошибка!':
        value = ''


count = 1

workbook = xlsxwriter.Workbook('log.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Date')
worksheet.write(0, 1, 'Time')
worksheet.write(0, 2, 'Вид сообщения')
worksheet.write(0, 3, 'Отправитель')
worksheet.write(0, 4, 'ID отправителя')
worksheet.write(0, 5, 'Сообщение')


@bot.message_handler(content_type=['text'])
def send_text(message):
    print(message)
    global count
    if message.content_type == 'text':
        if message.text != 'stop':
            worksheet.write(count, 0, str(dt.datetime.now().date()))
            worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
            worksheet.write(count, 2, 'текст')
            worksheet.write(count, 3, message.from_user.first_name + ' ' + message.from_user.last_name)
            worksheet.write(count, 4, message.from_user.id)
            worksheet.write(count, 5, message.text)
            count += 1
        else:
            workbook.close()


bot.polling(none_stop=False, interval=0)

