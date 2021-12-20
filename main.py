import telebot


class Controller:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)


controller = Controller("5036242550:AAFlwSBYIaGiuB8rptSUoP5UuCEIEm3LpiQ")


@controller.bot.message_handler()
def message(message):
    controller.bot.send_message(message.chat.id, "FFFF")


controller.bot.infinity_polling()
