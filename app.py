from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from slackeventsapi import SlackEventAdapter
from slacker import Slacker

from common import slack_signing_secret, slack_bot_token
from common.logger import Logger
from bot.slackbot import SlackBot


# This `app` represents your existing Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# An example of one of your Flask app's routes
@app.route('/')
def hello():
    return "hello there!"


# Bind the Events API route to your existing Flask app by passing ther server
# instance as the last param, or with `server=app`
slack_event_adapter = SlackEventAdapter(slack_signing_secret, '/jsyoo/events', app)


# Slacker setting
slack_client = Slacker(slack_bot_token)


# Create an event listener for "message" events and print the message
# @slack_event_adapter.on('message')
# def handle_message(event_data):
#     message = event_data['event']
#     print(message)


# Create an event listener for "mention" events and print the message
@slack_event_adapter.on('app_mention')
def app_mention(event_data):
    mention = event_data['event']['text']
    channel = event_data['event']['channel']

    text = mention[15:]

    slack = SlackBot()
    response = slack.handle_command(text)
    if response is not None:
        slack_client.chat.post_message(channel, response)


# Create an event listener for "reaction_added" events and print the emoji name
@slack_event_adapter.on('reaction_added')
def reaction_added(event_data):
    emoji = event_data['event']['reaction']
    print(emoji)


# Start the server on port 3000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
