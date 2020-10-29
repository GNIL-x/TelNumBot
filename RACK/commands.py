import telebot
from RACK.keyboards import *
import time
from RACK.parsers.number import *
from RACK.Callback_to_user import *

sl = dict()

bot = telebot.TeleBot('1136386527:AAFRT-Oq7BzF0RjEfIxkyqF2JGWHwB0qfOg')


@bot.message_handler(commands=['start'])
def starty(message):
    bot.send_message(message.chat.id, 'Этот бот определяет существует ли такой телефонный номер!', reply_markup=key1)


@bot.message_handler(commands=['komanda'])
def sent(message):
    bot.send_message(message.chat.id, 'Что вы хотите отправить богу?')
    sl[message.chat.id] = True


@bot.message_handler(content_types=['text'])
def textMes(message):
    n = isnum(message.text)
    if n[0]:
        bot.send_message(message.chat.id, f'Верно ли введен номер телефона? \n{n[1]}', reply_markup=key2)
    if sl[message.chat.id]:
        mis(message, 'CARAMBOJAbot')
        sl[message.chat.id] = False
    if message.chat.id == 380907452:
        try:
            moy = message.text.split('\n')
            bot.send_message(int(moy[0]), moy[1])
        except:
            pass


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def except_message(message):
    bot.send_message(message.chat.id, 'Извините, я принимаю только текстовые сообщения')


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.data == 'number.oper':
        numb = call.message.text.split('\n')[1]
        bot.send_message(call.message.chat.id, f'Оператор сети: {oper(numb)}')
        bot.answer_callback_query(call.id, text='вы нажали')
    elif call.data == 'number.reg':
        regi = call.message.text.split('\n')[1]
        bot.send_message(call.message.chat.id, f'Регион: {reg(regi)}')
        bot.answer_callback_query(call.id, text='Вы нажали', show_alert=True)


def isnum(text):
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('-', '')
    text = text.replace('+', '')
    if len(text) == 11:
        if text.isdigit():
            if text[0] == '7':
                return True, f'8{text[1::]}'
            elif text[0] == '8':
                return True, text
    return False, '0'
