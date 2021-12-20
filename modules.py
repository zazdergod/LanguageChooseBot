import csv
import copy
from Settings import languages_file, questions_file


class Language(object):
    def __init__(self, name, description, measure):
        self.result = 0
        self.name = name
        self.description = description
        self.measure = measure

    def calculate(self, m, s, r):
        self.result = self.result + int(self.measure[m]) * int(s) * int(r)


class Question(object):
    def __init__(self, text, answers, ratio):
        self.text = text
        self.answers = answers
        self.ratio = ratio


class Answer(object):
    def __init__(self, text, measure, scale):
        self.text = text
        self.measure = measure
        self.scale = scale


def init_languages():
    f = open(languages_file, 'r', encoding="utf-8")
    reader = csv.DictReader(f, delimiter=';')
    all_languages = []
    for line in reader:
        name = line['name']
        line.pop('name')
        description = line['description']
        line.pop('description')
        measure = {}
        for k in line:
            measure.update({k: line[k]})
        all_languages.append(Language(name, description, measure))
    return all_languages


def init_questions():
    f = open(questions_file, 'r')
    reader = csv.DictReader(f, delimiter=';')
    all_questions = []
    for line in reader:
        count_of_answer = int((len(line) - 2) // 3)
        all_answers = []
        for k in range(1, count_of_answer + 1):
            if line['answer' + str(k)] != '':
                all_answers.append(Answer(line['answer' + str(k)], line['measure' + str(k)], line['scale' + str(k)]))
        all_questions.append(Question(line['text'], all_answers, line['ratio']))
    return all_questions


languages = init_languages()
questions = init_questions()


def write_answer(l, q, a):
    measure = questions[q].answers[a].measure
    scale = questions[q].answers[a].scale
    ratio = questions[q].ratio
    for i in l:
        i.calculate(measure, scale, ratio)
    if q == len(questions) - 1:
        return generate_finish(l)
    else:
        return None


def generate_finish(l):
    l.sort(key=lambda p_iter: p_iter.result, reverse=True)
    st = ''
    for i in range(0, 10):
        st += l[i].name + ' - ' + str(l[i].result) + '\n'
    return st


# l1 = copy.deepcopy(languages)
# 
# for q in range(0, len(questions)):
#     print(questions[q].text)
#     for a in range(0, len(questions[q].answers)):
#         print(' - ' + questions[q].answers[a].text)
#     ask = input('')
#     new_answer = write_answer(l1, q, int(ask)-1)
#     if new_answer:
#         print(new_answer)
# del l1


