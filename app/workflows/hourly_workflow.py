import datetime
from app.models import User
from app.tasks.send_tweet_task import SendTweetTask
from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable

class HourlyWorkflow(Workflow, Zenatonable):

    def handle(self):
        current_hour = datetime.datetime.now().hour
        frequencies = ['every']

        if current_hour % 2 == 0:
            frequencies.append('even')
        else:
            frequencies.append('odd')

        hours = [3, 4, 6, 8, 12]
        frequencies = frequencies + list(filter(lambda i: current_hour % i == 0, hours))
        
        users = User.query.filter(User.frequency.in_(frequencies))

        for user in users:
            print("tweeting for", user.id)
            SendTweetTask(user.id).dispatch()
