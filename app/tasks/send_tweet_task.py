import os
from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable

from zenaton_client import app
from app.models import User

class SendTweetTask(Task, Zenatonable):

    def __init__(self, user_id):
        self.user_id = user_id

    def handle(self):
        # load the user
        user = User.query.get(self.user_id)

        user.tweet()