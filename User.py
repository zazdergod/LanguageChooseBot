from modules import init_languages


class User:

    def __init__(self, user_id):
        self.id = user_id
        self.progress = 0
        self.languages = init_languages()


