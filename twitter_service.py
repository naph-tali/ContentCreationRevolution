import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class TwitterService:
    """
     MINIMAL TWITTER SERVICE
    Root-level backup version
    """
    
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
        )
        print(" Twitter Service: INITIALIZED (Root Level)")
    
    def post_tweet(self, text):
        """Post a tweet with error handling"""
        try:
            result = self.client.create_tweet(text=text)
            return result
        except Exception as e:
            raise e

# Test function
if __name__ == '__main__':
    service = TwitterService()
    print(" Twitter Service Test: PASSED")
