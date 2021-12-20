import telebot
from AnswerControl import AnswerControl


class Controller:

    def __init__(self, token, answer_control):
        self.bot = telebot.TeleBot(token)
        self.answer_control = answer_control

    def check_message(self, message):
        progress = self.answer_control.get_user_progress(message.chat.id)


answer = AnswerControl()
controller = Controller("5036242550:AAFlwSBYIaGiuB8rptSUoP5UuCEIEm3LpiQ", answer)


@controller.bot.message_handler()
def send_message(message):
    controller.check_message(message)


controller.bot.infinity_polling()
