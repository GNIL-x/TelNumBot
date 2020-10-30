from .keyboards import *
from RACK.parsers.number import *
from .Callback_to_user import *
import random
import time

sl_of_users = dict()  # Надо сделать бд
bot = telebot.TeleBot('1136386527:AAFRT-Oq7BzF0RjEfIxkyqF2JGWHwB0qfOg')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Этот бот определяет существует ли такой телефонный номер!', reply_markup=key1)


@bot.message_handler(commands=['error'])
def analytics_message(message):
    bot.send_message(message.chat.id, 'Что вы хотите отправить богу (админу)?')
    sl_of_users[message.chat.id] = True


@bot.message_handler(commands=['hack'])
def hack(message):
    bot.send_message(message.chat.id, 'Взлом пентагона начался! 😎')
    time.sleep(1)
    x = 0
    while x < 100:

        try:
            bot.edit_message_text(f'Процесс взлома завершен на {x}%...', message.chat.id, message.message_id + 1)
            time.sleep(0.3)
            x += random.randint(1, 4)
        except:
            pass
    bot.edit_message_text('Пентагон взломаааан! 😎', message.chat.id, message.message_id + 1)
    bot.send_message(message.chat.id)


@bot.message_handler(content_types=['text'])
def text_mes(message):
    n = is_num(message.text)
    if n[0]:
        bot.send_message(message.chat.id, f'Верно ли введен номер телефона? \n{n[1]}', reply_markup=key2)
    elif sl_of_users[message.chat.id]:
        send_analytic(message, 'CARAMBOJAbot')
        bot.send_message(message.chat.id, 'Успешно отправлено', reply_markup=key1)
        sl_of_users[message.chat.id] = False
    elif message.chat.id == 380907452:
        try:
            moy = message.text.split('\n')
            bot.send_message(int(moy[0]), moy[1])
        except IndexError:
            bot.send_message(message.chat.id, 'Мой царь, у меня что-то не получилось')


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def except_message(message):
    bot.send_message(message.chat.id, 'Извините, я принимаю только текстовые сообщения')


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if 'number' in call.data:
        numb = call.message.text.split('\n')[1]
        if call.data == 'number.all_inf':
            bot.send_message(call.message.chat.id, f'Оператор сети: {oper(numb)}\n'
                                                   f'Регион: {reg(numb)}')
        elif call.data == 'number.reg':
            bot.send_message(call.message.chat.id, f'Регион: {reg(numb)}')
        elif call.data == 'number.operator':
            bot.send_message(call.message.chat.id, f'Оператор сети: {oper(numb)}')
        bot.answer_callback_query(call.id)


def is_num(text):
    list_to_replace = ['(', ')', '-', '+']
    for i in list_to_replace:
        text = text.replace(i, '')
    if len(text) == 11:
        if text.isdigit():
            if text[0] == '7':
                return True, f'8{text[1::]}'
            elif text[0] == '8':
                return True, text
    return False, '0'
