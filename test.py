from slackeventsapi import SlackEventAdapter
from slacker import Slacker


slack_signing_secret = '07255a5f310735dcd02aab5359de8690'
slack_events_adapter = SlackEventAdapter(slack_signing_secret, '/slack/events')


slack_bot_token = 'xoxb-698200255669-1054001583987-cmeRD19uLu4iu03BUnAp2wvQ'
slack_client = Slacker(slack_bot_token)


# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    print(message)
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.chat.post_message(channel, message)


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.chat.post_message(channel, text)


# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(host='0.0.0.0', port=3000)
