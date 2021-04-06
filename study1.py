from telegram.ext import Updater
import telegram
import logging
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
#bot = telegram.Bot(token='1709227246:AAHprWyr-JKWtDe_nhDdbnJd_Zih2vKIvec')
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
#print(bot.get_me())
