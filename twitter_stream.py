from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token_key = os.environ["ACCESS_TOKEN_KEY"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Creates a listener to streaming
class Listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    l = Listener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['data science', 'big data'])
