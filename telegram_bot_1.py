from telegram.ext import Updater, MessageHandler, Filters


# Определяем функцию-обработчик сообщений.
def echo(update, context):
    update.message.reply_text('Я получил сообщение "{}".'.format(update.message.text))


def main():
    updater = Updater("YOUR_TOKEN", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    print('Bot started')
    updater.idle()


if __name__ == '__main__':
    main()