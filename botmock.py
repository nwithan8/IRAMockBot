import markovify #https://github.com/jsvine/markovify
import tweepy #https://github.com/tweepy/tweepy
import time
from datetime import datetime

#Twitter API Credentials
consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweet = ""

#Read data from IRA tweets
with open('ira_tweets_en_nolinks.txt') as f:
    text = f.read()

#produce text model
text_model = markovify.NewlineText(text)

while True:
#Produce 1 tweet-length (280 characters) sentence
    for i in range(1):
        tweet = text_model.make_short_sentence(280)
        api.update_status(tweet) #Post tweet
        time.sleep(10) #Tweet every 30 minutes

