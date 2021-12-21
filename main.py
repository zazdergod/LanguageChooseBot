import telebot
from telebot import types
from AnswerControl import AnswerControl
from Question import Question
from Cacher import Cacher
from passwords import bot_token


class Controller:

    def __init__(self, bot, answer_control):
        self.bot = bot
        self.answer_control = answer_control
        self.questions = Question.init_questions()

    def start_chat(self, message):
        user_id = message.chat.id
        self.answer_control.delete_user(user_id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        items = [types.KeyboardButton("Да")]
        for item in items:
            markup.add(item)
        self.bot.send_message(user_id, "Вы готовы начать?", reply_markup=markup)

    def check_message(self, message):
        user_id = message.chat.id
        progress = self.answer_control.get_user_progress(user_id)
        if progress is None:
            self.answer_control.register_user(user_id)
            self.send_question(user_id, 0)
        elif progress < len(self.questions) - 1:
            self.validate_answers(progress, message)
        else:
            answer = self.answer_control.get_user_result(user_id)
            if answer is not None:
                self.bot.send_message(user_id, answer)
                self.bot.send_message(user_id, "Вы закончили проходить тестирование. Если хотите повторить, "
                                               "то напишите команду /start", reply_markup=types.ReplyKeyboardRemove())

    def send_question(self, user_id, progress):
        question = self.questions[progress]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for answer in question.answers:
            item = types.KeyboardButton(answer.text)
            markup.add(item)
        self.bot.send_message(user_id, question.text, reply_markup=markup)

    def validate_answers(self, progress, message):
        user_id = message.chat.id
        question = self.questions[progress]
        answers = question.answers
        result = list(filter(lambda x: x.text == message.text, answers))
        if len(result) != 0:
            answer = result[0]
            self.answer_control.get_answer(user_id, answer.measure, answer.scale, question.ratio)
        progress = self.answer_control.get_user_progress(user_id)
        self.send_question(user_id, progress)


cacher = Cacher()
answerControl = AnswerControl(cacher)
bot = telebot.TeleBot(bot_token)
controller = Controller(bot, answerControl)


@bot.message_handler(commands=['start'])
def start_chat(message):
    controller.start_chat(message)


@bot.message_handler(content_types='text')
def send_message(message):
    controller.check_message(message)


bot.infinity_polling()