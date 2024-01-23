import telebot;
from telebot import types
bot = telebot.TeleBot('6354825947:AAGyPr1Y_Rc1LnQu_zW5fYYxNFWvmea4UWI');
@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id,'давай поиграем?')
         bot.send_message(message.from_user.id, 'привет')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)