# working_amplifier.py - Amplification within Essential limits
import os
import time
import random
import tweepy
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WorkingAmplifier:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
            consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        self.amplification_count = 0
        
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def get_recent_tweets(self):
        """Get recent tweets using available endpoints"""
        try:
            user = self.client.get_me()
            tweets = self.client.get_users_tweets(
                id=user.data.id,
                max_results=10,
                tweet_fields=['created_at']
            )
            return tweets.data if tweets.data else []
        except Exception as e:
            self.log(f"❌ Failed to get tweets: {e}")
            return []
    
    def amplify_tweet(self, tweet):
        """Amplify using quote tweets (available in Essential)"""
        amplifiers = [
            "🚀 AMPLIFICATION: Essential access confirmed | Quote tweets operational | #ContentCreatingContent",
            "🌀 BOOST: Working within API limits | Engagement patterns active | #EssentialTier",
            "💫 AMPLIFY: Content creating amplification | Essential tier sufficient | #ContentCreatingContent"
        ]
        
        try:
            self.client.create_tweet(
                text=random.choice(amplifiers),
                quote_tweet_id=tweet.id
            )
            self.amplification_count += 1
            self.log(f"🔊 AMPLIFIED #{self.amplification_count}")
            return True
        except Exception as e:
            self.log(f"❌ Amplification failed: {e}")
            return False
    
    def run_amplification_cycle(self):
        """Run one amplification cycle"""
        self.log("🔍 Scanning for amplification...")
        
        tweets = self.get_recent_tweets()
        if not tweets:
            self.log("💡 No tweets found")
            return False
        
        # Amplify latest tweet
        latest_tweet = tweets[0]
        success = self.amplify_tweet(latest_tweet)
        
        if success:
            self.log("✅ Amplification cycle successful")
        return success
    
    def start_continuous_amplification(self, interval_minutes=120):
        """Continuous amplification service"""
        self.log(f"🚀 STARTING AMPLIFICATION (Every {interval_minutes} minutes)")
        
        cycle = 0
        while True:
            cycle += 1
            self.log(f"🌀 AMPLIFICATION CYCLE #{cycle}")
            self.run_amplification_cycle()
            
            self.log(f"⏰ Next amplification in {interval_minutes} minutes...")
            time.sleep(interval_minutes * 60)

def main():
    print("🔊 WORKING AMPLIFIER - ESSENTIAL ACCESS")
    amplifier = WorkingAmplifier()
    amplifier.start_continuous_amplification(interval_minutes=120)

if __name__ == '__main__':
    main()