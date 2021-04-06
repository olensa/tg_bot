import telegram
import logging
from telegram.ext import Updater, MessageHandler, InlineQueryHandler, Filters, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from datetime import datetime
import time
import schedule

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#time_toronto = pytz.timezone('America/New_York')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
start_handler = CommandHandler('start', start)
#schedule.every().day.at("17:15").do(reminder)

def reminder():
    text='time to work'
schedule.every(10).seconds.do(reminder)
#reminder_handler = MessageHandler(Filters.text,reminder)
def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1785809449:AAFqHmcjsXqTLvlhFI_7LzBWavQzHe_k1iQ")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram

    #dispatcher.add_handler(reminder_handler)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    #dispatcher.add_handler(CommandHandler("set", set_timer))
    #dispatcher.add_handler(CommandHandler("unset", unset))

    # Start the Bot
    updater.start_polling()
    while True:
        schedule.run_pending()
        time.sleep(1)
    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()