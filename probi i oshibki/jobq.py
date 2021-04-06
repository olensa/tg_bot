import telegram
import logging
from telegram.ext import Updater, MessageHandler, InlineQueryHandler, Filters, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import datetime
import time
import schedule

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#time_toronto = pytz.timezone('America/New_York')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
start_handler = CommandHandler('start', start)
def daily_job(update, context, job_queue=None):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "setting a reminder")
    t = datetime.time(18, 1, 00, 000000)
    job_queue.run_daily(notify, t, days=tuple(range(7)), context=update)

def notify(bot,update, job):
    bot.send_message(chat_id=update.effective_chat.id, text="time to work")


def main() -> None:
    """Run bot."""
    updater = Updater("1785809449:AAFqHmcjsXqTLvlhFI_7LzBWavQzHe_k1iQ", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('notify', daily_job, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()