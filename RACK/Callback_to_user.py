import telebot

callback_bot = telebot.TeleBot('1385232383:AAEiIL7rGofcHw8vehkgakxYyMKe3miBhnQ')


def mis(message, from_bot):
    callback_bot.send_message(380907452, f'Username: @{message.from_user.username}\n'
                                         f'Текст: {message.text}\n'
                                         f'Id: {message.chat.id}\n'
                                         f'Имя: {message.from_user.first_name}\n'
                                         f'Фамилия: {message.from_user.last_name}\n'
                                         f'Бот: @{from_bot}')


