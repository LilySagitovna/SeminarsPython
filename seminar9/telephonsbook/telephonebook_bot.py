import urllib
import urllib.request
import telebot
import function_pandas
import pandas

TOKEN = '5728083512:AAFs6oRV_0KsEn5_v-S7nQ2zKEc_uTqTsDI'
bot = telebot.TeleBot(TOKEN)


keyboard = telebot.types.InlineKeyboardMarkup()  # создание кнопок
keyboard.row(telebot.types.InlineKeyboardButton('Меню. Выберите нужное действие:', callback_data='no'))  # создание строк кнопок
# keyboard.row(telebot.types.InlineKeyboardButton('Добавить контакт', callback_data='add_contact'),
#              telebot.types.InlineKeyboardButton('Удалить контакт', callback_data='delete_entry'))
keyboard.row(telebot.types.InlineKeyboardButton('Импорт', callback_data='data_import'),
             telebot.types.InlineKeyboardButton('Экспорт', callback_data='data_export'))
keyboard.row(telebot.types.InlineKeyboardButton('Посмотреть контакты', callback_data='print_list'))
             # telebot.types.InlineKeyboardButton('Найти контакт по фамилии', callback_data='search_surname'))
keyboard.row(telebot.types.InlineKeyboardButton('Выход из справочника', callback_data='exit_program'))


@bot.message_handler(commands=['start', 'telephonesbook'])
def get_message(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'no':
            pass
        # elif call.data == 'add_contact':
        #     surname = bot.send_message(call.message.chat.id, 'Напишите фамилию')
        #     name = bot.send_message(call.message.chat.id, 'Напишите имя')
        #     lastname = bot.send_message(call.message.chat.id, 'Напишите отчество')
        #     tel = bot.send_message(call.message.chat.id, 'Напишите номер телефона')
        #     text_id = bot.send_message(call.message.chat.id, 'Напишите описание')
        #     list_data = [surname, name, lastname, tel, text_id]
        #     bot.register_next_step_handler(list_data, function.search_surname)
        #     # function.add_a_note(surname, name, lastname, tel, text_id)
        #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text='Контакт добавлен!')
        # elif call.data == 'delete_entry':
        #     delet = bot.send_message(call.message.chat.id, 'Введите фамилию')
        #     bot.register_next_step_handler(delet, function.delete_entry)
        elif call.data == 'data_import':
            file = bot.send_message(call.message.chat.id, 'Отправьте файл')
            bot.register_next_step_handler(file, addfile)
        elif call.data == 'data_export':
            function_pandas.data_export()
            file = open('Export.txt', 'rb')
            bot.send_document(call.message.chat.id, file)
            bot.send_message(call.message.chat.id, 'Готово')
        elif call.data == 'print_list':
            bot.send_message(call.message.chat.id, function_pandas.print_list())
        # if call.data == 'search_surname':
        #     surname = bot.send_message(call.message.chat.id, 'Введите фамилию')
        #     bot.register_next_step_handler(surname, function_pandas.search_surname)
        elif call.data == 'exit_program':
            bot.send_message(call.message.chat.id, 'Вы вышли из программы!' )
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text='Вы вышли из программы!', reply_markup=keyboard)


@bot.message_handler(content_types=['document'])
def addfile(message):
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    function_pandas.data_import(file_name)
    bot.send_message(message.from_user.id, 'Данные импортированы')


bot.polling(none_stop=False, interval=0)
