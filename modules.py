import csv
import copy


class Language(object):
    def __init__(self, name, measure):
        self.result = 0
        self.measure = measure
        self.name = name

    def calculate(self, m, s, r):
        self.result = self.result + int(self.measure[m]) * s * r


def init_languages():
    all_languages = [
        Language('Python', {'mobile': 0, 'web': 2}),
        Language('C++', {'mobile': 1, 'web': 1}),
    ]
    return all_languages


def init_questions():
    all_questions = [
        {'text': 'В какой сфере вы хотели бы работать?',
         'answers': [
             {'text': 'Мобильная разработка',
              'measure': 'mobile',
              'scale': 1,
              },
             {'text': 'Web-разработка',
              'measure': 'web',
              'scale': 1,
              },
         ],
         'ratio': 5
         },
    ]
    return all_questions


languages = init_languages()
questions = init_questions()


def write_answer(l, q, a):
    measure = questions[q]['answers'][a]['measure']
    scale = questions[q]['answers'][a]['scale']
    ratio = questions[q]['ratio']
    for i in l:
        i.calculate(measure, scale, ratio)
    if q == len(questions) - 1:
        return generate_finish(l)
    else:
        return None


def generate_finish(l):
    answer_var = None
    maximum = 0
    st = ''
    for i in l:
        st += i.name + ' - ' + str(i.result) + '\n'
        # if i.result > maximum:
        #     maximum = i.result
        #     answer_var = i
    return st


l1 = copy.deepcopy(languages)
for i in l1:
    print(i.result)
new_answer = write_answer(l1, 0, 1)
if new_answer:
    print(new_answer)
# for i in l1:
#     print(i.result)


del l1


