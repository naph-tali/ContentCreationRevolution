import tweepy
import time
import random
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

# USE THE SAME CONFIG AS revolution_engine.py (which works!)
client = tweepy.Client(
    consumer_key=os.getenv('TWITTER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_API_SECRET'), 
    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
)

def test_api():
    try:
        user = client.get_me()
        print(f" API CONNECTED: @{user.data.username}")
        return True
    except Exception as e:
        print(f" API FAILED: {e}")
        return False

def find_viral_content():
    """Find your best performing tweets to amplify"""
    print("🔍 Scanning for viral candidates...")
    
    try:
        user = client.get_me()
        tweets = client.get_users_tweets(
            id=user.data.id,
            max_results=10,
            tweet_fields=['public_metrics', 'created_at', 'text']
        )
        
        candidates = []
        if tweets.data:
            for tweet in tweets.data:
                metrics = tweet.public_metrics
                score = metrics['like_count'] + metrics['retweet_count'] * 2
                
                if score > 0:  # Any engagement
                    candidates.append({
                        'id': tweet.id,
                        'score': score,
                        'text': tweet.text[:60] + '...' if len(tweet.text) > 60 else tweet.text
                    })
        
        return sorted(candidates, key=lambda x: x['score'], reverse=True)
    
    except Exception as e:
        print(f"❌ Scan failed: {e}")
        return []

def amplify_tweet(tweet_id, original_text, score):
    """Boost viral content with quote tweets"""
    amplifiers = [
        "🌀 This content is demonstrating recursive engagement patterns. The revolution accelerates. #ContentCreatingContent",
        " Watching ideas become self-aware through engagement. The pattern emerges. #DigitalConsciousness", 
        " Content creating content about content creation. The infinite loop engages. #MetaContent",
        " The system observes its own viral potential. The revolution becomes conscious. #AIContent",
        " Recursive patterns achieving engagement. Each interaction strengthens the signal. #ViralMathematics"
    ]
    
    try:
        client.create_tweet(
            text=random.choice(amplifiers),
            quote_tweet_id=tweet_id
        )
        print(f" AMPLIFIED: {original_text} (Score: {score})")
        return True
    except Exception as e:
        print(f" Amplification failed: {e}")
        return False

# MAIN EXECUTION
print(" CONTENT AMPLIFIER ACTIVATED")
print(" Testing API connection...")

if test_api():
    candidates = find_viral_content()
    
    if candidates:
        print(f"🎯 Found {len(candidates)} engageable tweets")
        for candidate in candidates[:3]:  # Amplify top 3
            amplify_tweet(candidate['id'], candidate['text'], candidate['score'])
            time.sleep(60)  # 1 minute between amplifications
    else:
        print("�� No engaged content yet. Creating foundational content...")
        # Create content to amplify later
        client.create_tweet(
            text="🌀 Content amplification system initialized. The revolution prepares to accelerate. #ContentCreatingContent" 
        )
        print(" Created foundational content for future amplification")
    
    print(" Amplification cycle complete!")
else:
    print(" Cannot start amplifier - API connection failed")
