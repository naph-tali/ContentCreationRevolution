import tweepy
import time
from datetime import datetime

# Your API keys
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

def monitor_live_posts():
    print(' LIVE POST MONITOR - Watching @naphtali_lemma')
    print('=' * 50)
    
    last_tweet_id = None
    
    while True:
        try:
            # Get your recent tweets
            tweets = client.get_users_tweets(
                id='982956216677695489',  # Your user ID
                max_results=5,
                tweet_fields=['created_at', 'text']
            )
            
            if tweets.data:
                latest_tweet = tweets.data[0]
                
                # Check if new tweet
                if last_tweet_id != latest_tweet.id:
                    last_tweet_id = latest_tweet.id
                    timestamp = latest_tweet.created_at.strftime('%H:%M:%S')
                    print(f'🆕 [{timestamp}] NEW POST:')
                    print(f'   📝 {latest_tweet.text}')
                    print(f'   🔗 https://twitter.com/naphtali_lemma/status/{latest_tweet.id}')
                    print('   ─' * 30)
            
            time.sleep(60)  # Check every minute
            
        except KeyboardInterrupt:
            print('\n🛑 Monitor stopped')
            break
        except Exception as e:
            print(f'❌ Monitor error: {e}')
            time.sleep(30)

if __name__ == '__main__':
    monitor_live_posts()
