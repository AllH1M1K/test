import telebot
token='6445401383:AAHJJN6O9xQSFn7-cEwl-WuHdDaw1c5LZ6k'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"хуй ")
bot.infinity_polling()