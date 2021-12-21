from Settings import languages_file
import csv


class Language(object):
    def __init__(self, name, description, measure, result=0):
        self.result = result
        self.name = name
        self.description = description
        self.measure = measure

    def calculate(self, m, s, r):
        self.result = self.result + float(self.measure[m]) * float(s) * float(r)

    @classmethod
    def init_languages(cls):
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
