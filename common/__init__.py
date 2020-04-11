import os
import json


with open('./config.json') as json_file:
    config = json.load(json_file)
    log_level = config['log_level']
    slack_signing_secret = config['slack_signing_secret']

slack_bot_token = os.environ['SLACK_BOT_TOKEN']
