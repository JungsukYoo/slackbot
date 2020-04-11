import os
import platform
import json


with open('./config.json') as json_file:
    config = json.load(json_file)
    log_level = config['log_level']


if platform.system() == 'Windows':
    slack_signing_secret = None
    slack_bot_token = None
else:
    slack_signing_secret = os.environ['SLACK_SIGNING_SECRET']
    slack_bot_token = os.environ['SLACK_BOT_TOKEN']
