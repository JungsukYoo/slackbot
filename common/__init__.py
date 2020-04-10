import json


with open('../config.json') as json_file:
    config = json.load(json_file)
    log_level = config['log_level']
    slack_api = config['slack_api']
