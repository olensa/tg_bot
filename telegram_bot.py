import telebot

bot = telebot.TeleBot('1722790569:AAHh_sP43w8VGdclJUIbwvC3YnE5RWROPDc')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'I am Bot. Noce to meet you, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'Hello!')
    else:
        bot.send_message (message.from_user.id, "Sorry, I don't understand")
bot.polling(none_stop=True)