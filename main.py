import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])

def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать")
    markup.add(item1)
    bot.send_message(message.chat.id,', с помощью этого бота ты сможешь ставить напоминалки, давай начнём уже!',reply_markup=markup)



if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
       bot.polling(none_stop=True) # запуск бота
