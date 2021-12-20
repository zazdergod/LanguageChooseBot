from modules import languages, questions, write_answer
import copy

l1 = copy.deepcopy(languages)

for q in range(0, len(questions)):
    print(questions[q].text)
    for a in range(0, len(questions[q].answers)):
        print(' - ' + questions[q].answers[a].text)
    ask = input('')
    new_answer = write_answer(l1, q, int(ask)-1)
    if new_answer:
        print(new_answer)

del l1
