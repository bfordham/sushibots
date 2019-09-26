from app.tasks.send_tweet_task import SendTweetTask
from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable

class TweetWorkflow(Workflow, Zenatonable):

    def __init__(self, user_id):
        self.user_id = user_id

    def handle(self):
        SendTweetTask(self.user_id).execute()
