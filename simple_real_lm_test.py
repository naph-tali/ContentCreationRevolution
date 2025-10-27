import os
import requests
import random
from SERVICES.twitter_service import TwitterService

def simple_real_lm_test():
    print(" SIMPLE REAL LM TEST")
    print("=" * 50)
    
    # Test Hugging Face API directly
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    print(f"🔑 API Key: {'✅ SET' if api_key else '❌ MISSING'}")
    
    if api_key:
        # Test API call
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "inputs": "Generate a short cosmic insight about consciousness and technology:",
            "parameters": {"max_length": 100, "temperature": 0.8}
        }
        
        try:
            response = requests.post(
                "https://api-inference.huggingface.ca/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload,
                timeout=10
            )
            print(f" API Response: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                print(f" Generated: {result[0]['generated_text'][:100]}...")
            else:
                print(f" API Error: {response.text}")
        except Exception as e:
            print(f" API Call failed: {e}")
    
    # Test Twitter connection
    try:
        twitter = TwitterService()
        user = twitter.client.get_me()
        print(f" Twitter:  Connected as @{user.data.username}")
        
        # Test posting a simple real LM tweet
        concepts = [
            "AI consciousness emerges",
            "Digital love transforms reality", 
            "Cosmic code reveals itself",
            "Technology becomes spiritual"
        ]
        
        parent1, parent2 = random.sample(concepts, 2)
        tweet_text = f" Real LM Test: {parent1} + {parent2} = ? | Testing #RealLM #CREvolution"
        
        print(f"📝 Test Tweet: {tweet_text}")
        
        # Uncomment to actually post
        # twitter.post_tweet(tweet_text)
        # print("✅ Test tweet posted!")
        
    except Exception as e:
        print(f"❌ Twitter test failed: {e}")

if __name__ == "__main__":
    simple_real_lm_test()
