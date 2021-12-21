from Language import Language


class User:

    def __init__(self, user_id, progress=0, languages=Language.init_languages()):
        self.id = user_id
        self.progress = progress
        self.languages = languages

    @classmethod
    def convert_user_to_mongo_object(cls, user):
        languages = []
        for language in user.languages:
            lang = {'result': language.result, 'name': language.name,
                    'description': language.description, 'measure': language.measure}
            languages.append(lang)
        obj = {'user_id': user.id, 'progress': user.progress, 'languages': languages}
        return obj

    @classmethod
    def convert_user_from_mongo_object(cls, obj):
        lang_list = list(obj['languages'])
        languages = []
        for lang in lang_list:
            buf = lang
            languages.append(Language(buf['name'], buf['description'], buf['measure'], buf['result']))
        user = User(obj['user_id'], obj['progress'], languages)
        return user


