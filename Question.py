from Settings import questions_file
import csv
from Answer import Answer

class Question(object):
    def __init__(self, text, answers, ratio):
        self.text = text
        self.answers = answers
        self.ratio = ratio

    @classmethod
    def init_questions(cls):
        f = open(questions_file, 'r', encoding="WINDOWS-1251")
        reader = csv.DictReader(f, delimiter=';')
        all_questions = []
        for line in reader:
            count_of_answer = int((len(line) - 2) // 3)
            all_answers = []
            for k in range(1, count_of_answer + 1):
                if line['answer' + str(k)] != '':
                    all_answers.append(
                        Answer(line['answer' + str(k)], line['measure' + str(k)], line['scale' + str(k)]))
            all_questions.append(Question(line['text'], all_answers, line['ratio']))
        return all_questions