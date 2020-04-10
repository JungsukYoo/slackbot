from flask import Flask
from slackeventsapi import SlackEventAdapter
from slacker import Slacker

from common import slack_signing_secret, slack_bot_token
from common.logger import Logger
from slackbot.slackbot import SlackBot


# This `app` represents your existing Flask app
app = Flask(__name__)


# An example of one of your Flask app's routes
@app.route('/')
def hello():
    return "hello there!"


# Bind the Events API route to your existing Flask app by passing ther server
# instance as the last param, or with `server=app`
slack_event_adapter = SlackEventAdapter(slack_signing_secret, '/slack/events', app)


# Slacker setting
slack_client = Slacker(slack_bot_token)


# Create an event listener for "message" events and print the message
@slack_event_adapter.on('message')
def handle_message(event_data):
    message = event_data['event']

    # If the incoming message respond
    if message.get('subtype') is None:
        msg = message.get('text')
        channel = message['channel']
        response = slackbat.handle_command(msg)
        slack_client.chat.post_message(channel, 'msg')

    print(message)


# Create an event listener for "reaction_added" events and print the emoji name
@slack_event_adapter.on('reaction_added')
def reaction_added(event_data):
    emoji = event_data['event']['reaction']
    print(emoji)


# Start the server on port 3000
if __name__ == '__main__':
    slackbat = SlackBot()
<<<<<<< Updated upstream
    slack_client.chat.post_message('#bot', 'test')
=======
    slack_client.chat.post_message('#bot', 'msg')
>>>>>>> Stashed changes
    app.run(host='0.0.0.0', port=3000)
