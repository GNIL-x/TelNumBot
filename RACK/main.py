from telebot.apihelper import *
from RACK.commands import *

while __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass
