import telebot

key1 = telebot.types.ReplyKeyboardMarkup(True, True)
key1.row('/start')
key1.row('/komanda')
key2 = telebot.types.InlineKeyboardMarkup()
key2.add(telebot.types.InlineKeyboardButton('Общая информация', callback_data='number.allinf'))
key2.add(telebot.types.InlineKeyboardButton('Оператор сети', callback_data='number.oper'))
key2.add(telebot.types.InlineKeyboardButton('Регион?', callback_data='number.reg'))
