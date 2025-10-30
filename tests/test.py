import tweepy
from datetime import datetime

API_KEY = 'k2KK1tJzekPlK6jhxEY2WXAhh'
API_SECRET = 'KMI36xCJPvmk2pgliCx9inUD5o6arx20nfUATZnbdklvQnGGZV'
ACCESS_TOKEN = '982956216677695489-pidw6W37hkxB5AQXTsUMsNS5KSMTkhV'
ACCESS_SECRET = '5gogqtYcq4S8mMgHrtDWWaiefvkaPnAFH8GeinX88rnrC'

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

test_msg = ' CONTENT CREATION REVOLUTION LAUNCHED! New API keys working! #ContentCreatingContent'
response = client.create_tweet(text=test_msg)
print('SUCCESS! Tweet ID:', response.data['id'])
