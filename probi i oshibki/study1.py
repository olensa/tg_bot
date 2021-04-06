from telegram.ext import Updater
import telegram
import logging
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

updater = Updater(token='1709227246:AAHprWyr-JKWtDe_nhDdbnJd_Zih2vKIvec', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
def inline_caps(update, context):
    query=update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand the command")

inline_caps_handler = InlineQueryHandler(inline_caps, pass_groups=True)
caps_handler = CommandHandler('caps', caps)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
start_handler = CommandHandler('start', start)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
updater.stop()
#print(bot.get_me())