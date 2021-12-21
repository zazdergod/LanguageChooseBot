from pymongo import MongoClient
from User import User
from passwords import CONNECTION_STRING


class Cacher:

    def __init__(self):
        self.client = MongoClient(CONNECTION_STRING)
        self.db = self.client['bot-database']
        self.users = self.db['users']

    def insert_user(self, user):
        self.users.insert_one(user)

    def find_user(self, user_id):
        return self.users.find_one({"user_id": user_id})

    def update_user(self, user):
        filter = {'user_id': user.id}
        new_values = {'$set': User.convert_user_to_mongo_object(user)}
        self.users.update_one(filter, new_values)

    def delete_user(self, user_id):
        self.users.delete_one({'user_id': user_id})
