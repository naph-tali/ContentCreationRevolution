import tweepy
from datetime import datetime

print('🚀 INSTANT LAUNCH WITH NEW KEYS')
print('=' * 45)

# Your NEW regenerated keys:
API_KEY = 'k2KK1tJzekPlK6jhxEY2WXAhh'
API_SECRET = 'KMI36xCJPvmk2pgliCx9inUD5o6arx20nfUATZnbdklvQnGGZV'
ACCESS_TOKEN = '982956216677695489-pidw6W37hkxB5AQXTsUMsNS5KSMTkhV'
ACCESS_SECRET = '5gogqtYcq4S8mMgHrtDWWaiefvkaPnAFH8GeinX88rnrC'

try:
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )
    
    # First test tweet
    test_msg = f'🎉 API REGENERATION SUCCESS! New keys working at {datetime.now().strftime("%H:%M")}. Content Creation Revolution LAUNCHED! #ContentCreatingContent'
    response = client.create_tweet(text=test_msg)
    
    print(' NEW KEYS WORK PERFECTLY!')
    print(f' Tweet ID: {response.data["id"]}')
    
    # Immediate follow-up to demonstrate continuity
    follow_up = ' System regenerated successfully. Content creation revolution now operational. The framework persists through technical evolution. #Resilience'
    client.create_tweet(text=follow_up)
    print(' Follow-up tweet posted!')
    
    print('')
    print(' CONTENT CREATION REVOLUTION: LAUNCH SUCCESSFUL!')
    print(' The revolution is now LIVE!')
    
except Exception as e:
    print(f' Failed: {e}')
    print(' Check if keys were copied correctly')
