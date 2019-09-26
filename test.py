import zenaton_client
from app.workflows.hourly_workflow import HourlyWorkflow
from app.tasks.send_tweet_task import SendTweetTask

HourlyWorkflow().dispatch()