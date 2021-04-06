import telebot
from telebot import types
import csv
from pathlib import Path
import telegram_token

token = telegram_token.API_TOKEN

bot = telebot.TeleBot(token)

#@bot.message_handler(content_types=['text'])

#def get_text_messages(message):
    #if message.text.lower() == "привет":
        #bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    #elif message.text == "/help":
        #bot.send_message(message.from_user.id, "Напиши привет")
    #else:
        #bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
name = ''
last_name = ''
age = 0
def greeting():
    global name, age, last_name
    my_file = Path("name.csv")
    if my_file.is_file():
        txt = open('name.csv', 'r')
        f = txt.read().split(',')
        print (f)
        name = f[1]
        last_name = f[2]
        age = f[0]
    else: 
        name = ''
        last_name = ''
        age = 0
    if name !='':
        greet = "Привет, " + str(name) + ", чем я могу тебе помочь?"
    else: 
        greet = "Привет, чем я могу тебе помочь?"
    return greet


@bot.message_handler(content_types = ['text'])
def start(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, greeting())
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")      
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /reg.")
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global last_name
    last_name = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    while age == 0:
        try:
            age = int (message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text = "Да", callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+last_name+'?' 
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        data = [age, name, last_name]

        with open('name.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(data)
        bot.send_message(call.from_user.id, "Запомню")
    elif call.data == 'no':
        bot.send_message(call.from_user.id, "Давай начнем сначала")
        bot.send_message(call.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(call.message, get_name)
    
bot.polling(none_stop=True, interval=0)