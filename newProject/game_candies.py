# import os
# import sys
# from django.conf import settings
#
# settings.configure()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
# # sys.path.append(BASE_DIR)
import random

import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

# import emoji


reply_keyboard = [['/play', '/rules'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5728083512:AAFs6oRV_0KsEn5_v-S7nQ2zKEc_uTqTsDI'

candy = 0


def start(update, context):
    update.message.reply_text(
        f"Я бот-играю в игру конфеты.Давай поиграем?"
        f" play - начало игры, rules - правила игры, exit - выход",
        reply_markup=markup
    )


def play(update, context):
    update.message.reply_text(
        "Введите количество конфет"
        # reply_markup=markup
    )
    return 1


def stop(update, context):
    update.message.reply_text(f"Всего доброго!")
    return ConversationHandler.END


def get_candies(update, context):
    global candy
    try:
        candy = int(update.message.text)
        update.message.reply_text(f"В игре {candy} конфет. Вы ходите первым.")
        update.message.reply_text("Введите количество конфет, которое Вы хотите взять.")
        print(candy)
    except ValueError:
        logging.warning('Ошибка: неверный тип данных')
        update.message.reply_text("Введите число больше 28")
        return 1
    return 2


def user_hod(update, context):
    global candy
    new_candy = int(update.message.text)
    if new_candy > 28:
        update.message.reply_text("Введите число от 1 до 28")
        return 2
    candy -= new_candy
    if candy <= 28:
        update.message.reply_text(f"Поздравляю, Выйграл бот!", reply_markup=markup)
        return ConversationHandler.END
    else:
        numb = random.randint(1, 28)
        update.message.reply_text(f"В игре осталось {candy}  конфет")
        update.message.reply_text(f"Я беру {numb} конфет")
        candy -= numb
        update.message.reply_text(f"В игре осталось {candy}  конфет. Ваш ход.")
        if candy <= 28:
            update.message.reply_text(f"Вы победили!", reply_markup=markup)
            return ConversationHandler.END
    return 2


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "Здесь правила игры.Игра с конфетами человек против человека."
        "Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга." 
        "За один ход можно забрать не более чем 28 конфет.")


def exit_mi(update, context):
    update.message.reply_text(f"Пока-пока.Приходи ещё)")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, get_candies)],
            2: [MessageHandler(Filters.text & ~Filters.command, user_hod)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit_mi))

    dp.add_handler(play_handler)

    updater.start_polling()

main()






