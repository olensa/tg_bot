from telegram.ext import Updater
import telegram
import logging
import telegram_token
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import InlineQueryHandler, CallbackQueryHandler, CallbackContext
import csv
from pathlib import Path
from csv import reader


a = 0
updater = Updater(token= telegram_token.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton('Register a link', callback_data='reg')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi I'm bot. Press '/reg' and your link to register", reply_markup=reply_markup)


def reg(update,context):
    day = 1
    link = str(context.args[0])
    day_link = '?showall=&start='
    chat_id = update.message.chat_id
    data = [day, link+day_link, chat_id]
    save_to_file(data)
    keyboard = [
        [
            InlineKeyboardButton("Today's link", callback_data='link')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Ok, I will remember your program',reply_markup=reply_markup)
def save_to_file(data):
    with open('links.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(data)
def send_link (update, context):
    read = read_file(update.message.chat_id)
    my_link = read[1]+read[0]
    context.bot.send_message(chat_id=update.message.chat.id, text='Here is your link '+my_link)
    options(update, context) 

def options (update, context):
    keyboard = [
            [
                InlineKeyboardButton("Next Day", callback_data='next'),
                InlineKeyboardButton("Previous Day", callback_data='Previous')
            ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:',reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    if query.data == 'next':
        next(update.callback_query,context)
    elif query.data == 'Previous':
        prev(update.callback_query, context)
    elif query.data == 'link':
        send_link(update.callback_query,context)
    elif query.data =='reg':
        reg(update.callback_query, context)
    query.answer()


def read_file(user_id):
    my_file = Path("links.csv")
    if my_file.is_file():
        with open('links.csv', 'r') as f:
            csv_reader = reader(f)
            for row in csv_reader:
                if str(user_id)==row[-1]:
                    link = row[1]
                    id = row[-1]
                    day = row[0]
    else:
        day = str(1)
        id = user_id
        link = ''
    data_list=[day,link,id]
    return data_list
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand the command")

def next(update, context):
    data = read_file(update.message.chat_id)
    day = int(data[0])
    day+=1
    data[0]=day
    save_to_file(data)
    send_link(update, context)


def prev(update, context):
    data = read_file(update.message.chat_id)
    day = int(data[0])
    day-=1
    data[0]=day
    save_to_file(data)
    send_link(update, context)

next_handler = CommandHandler('next', next)
prev_handler = CommandHandler('previous', prev)
start_handler = CommandHandler('start', start)
reg_handler = CommandHandler('reg', reg)
send_link_handler = CommandHandler ('link', send_link)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(send_link_handler)
dispatcher.add_handler(reg_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(next_handler)
dispatcher.add_handler(prev_handler)
dispatcher.add_handler(unknown_handler)


updater.start_polling()
updater.idle()
updater.stop()
