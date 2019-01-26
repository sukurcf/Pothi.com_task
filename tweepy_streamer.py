import json
import os
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging
import twitter_credentials
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("Rotating_log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(os.path.dirname(os.path.realpath(
    __file__))+'/tweetsdata', when='m', interval=1, backupCount=4)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class StdOutListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        tweet = {}
        tweet["user"] = data.get("user")["screen_name"]
        tweet["text"] = data.get("text")
        logger.info(json.dumps(tweet))
        return True

    def on_error(self, status):
        print(status)


listener = StdOutListener()
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                    twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                      twitter_credentials.ACCESS_TOKEN_SECRET)

stream = Stream(auth, listener)

try:
    stream.filter(track=[sys.argv[1]])
except BaseException as e:
    print(e.message)
    os.system('pkill -9 python')
