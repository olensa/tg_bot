import telebot
import telegram_token

bot = telebot.TeleBot(telegram_token.API_TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}. Напиши мне "привет"')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, жирная. Eще что-то?')
    else:
        bot.send_message (message.from_user.id, "Ты жирная, смирись")
bot.polling(none_stop=True)
