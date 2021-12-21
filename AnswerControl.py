from User import User


class AnswerControl:

    def __init__(self, cacher):
        self.users = []
        self.cacher = cacher

    def get_user_progress(self, user_id):
        # result = list(filter(lambda x: x.id == user_id, self.users))
        result = self.cacher.find_user(user_id)
        if result is not None:
            return result['progress']
        else:
            return

    def register_user(self, user_id):
        user = User(user_id)
        self.users.append(user)
        buf = User.convert_user_to_mongo_object(user)
        # print(self.cacher.find_user(user_id))
        self.cacher.insert_user(buf)

    def delete_user(self, user_id):
        self.cacher.delete_user(user_id)
        # self.users = list(filter(lambda x: x.id != user_id, self.users))

    def get_answer(self, user_id, m, s, r):
        result = self.cacher.find_user(user_id)
        # result = list(filter(lambda x: x.id == user_id, self.users))
        if result is not None:
            user = User.convert_user_from_mongo_object(result)
            user.progress += 1
            for language in user.languages:
                language.calculate(m, s, r)
            self.cacher.update_user(user)

    def get_user_result(self, user_id):
        result_message = ""
        # result = list(filter(lambda x: x.id == user_id, self.users))
        result = self.cacher.find_user(user_id)
        if result is not None:
            user = User.convert_user_from_mongo_object(result)
            languages = sorted(user.languages, key=lambda x: x.result, reverse=True)
            for language in languages:
                result_message += "{0} - {1}\n".format(language.name, language.result)
            return result_message
