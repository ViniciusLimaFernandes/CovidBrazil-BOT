import tweepy
from utils.tools import AuthData

userData = AuthData.oauthData()

consumer_key = userData.consumer_key
consumer_secret = userData.consumer_secret
access_token = userData.access_token
access_token_secret = userData.access_token_secret


def oAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except:
        return None


def postTweetMessage(message):
    oauth = oAuth()
    api = tweepy.API(oauth)

    api.update_status(message)
