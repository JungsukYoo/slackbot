from slackeventsapi import SlackEventAdapter
from common.logger import Logger
from common import slack_api


class SlackBot(object):
    logger = Logger('SlackBot')

    def __init__(self):
        self.slack_client = SlackEventAdapter(slack_api)
        self.starterbot_id = None

