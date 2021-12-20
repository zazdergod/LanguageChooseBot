from User import User


class AnswerControl:

    def __init__(self):
        self.users = [User(499140512)]


    def get_user_progress(self, user_id):
        result = list(filter(lambda x: x.id == user_id, self.users))
        if len(result) != 0:
            return result[0].progress
        else:
            return


# 499140512