import os
from dotenv import load_dotenv

load_dotenv()

def _mask_value(val, keep=4):
    if not val:
        return "<missing>"
    v = val.strip()
    if len(v) <= keep * 2:
        return "****"
    return f"{v[:keep]}...{v[-keep:]}"

def validate_environment():
    """Validate environment variables and provide setup guidance"""
    print("🔍 ENVIRONMENT VALIDATION")
    print("=" * 50)
    
    # Canonical keys and their common aliases
    twitter_keys_aliases = {
        'TWITTER_CONSUMER_KEY': ['TWITTER_CONSUMER_KEY', 'TWITTER_API_KEY'],
        'TWITTER_CONSUMER_SECRET': ['TWITTER_CONSUMER_SECRET', 'TWITTER_API_SECRET'],
        'TWITTER_ACCESS_TOKEN': ['TWITTER_ACCESS_TOKEN'],
        'TWITTER_ACCESS_TOKEN_SECRET': ['TWITTER_ACCESS_TOKEN_SECRET', 'TWITTER_ACCESS_SECRET']
    }
    
    print("\n📋 TWITTER CREDENTIALS CHECK:")
    missing = []
    present = []
    
    for canon, aliases in twitter_keys_aliases.items():
        value = None
        for name in aliases:
            v = os.getenv(name)
            if isinstance(v, str) and v.strip() and not v.lower().startswith('your_'):
                value = v.strip()
                break
        if value:
            present.append(canon)
            print(f"   ✅ {canon}: {_mask_value(value)}")
        else:
            missing.append(canon)
            print(f"   ❌ {canon}: MISSING")
    
    print(f"\n📊 SUMMARY:")
    print(f"   Credentials present: {len(present)}/{len(twitter_keys_aliases)}")
    
    if len(missing) == 0:
        print("🎉 All credentials configured! Live mode enabled.")
        return True
    else:
        print(f"⚠️  Missing {len(missing)} credentials. Safe mode will be used.")
        print("\n💡 SETUP INSTRUCTIONS:")
        print("   1. Go to https://developer.twitter.com/")
        print("   2. Create a Project and App")
        print("   3. Get your API keys and tokens")
        print("   4. Add them to your .env file like this:")
        print("\n# .env file contents (use any supported alias):")
        for canon in twitter_keys_aliases.keys():
            print(f"{canon}=your_actual_value_here")
        return False

def test_safe_operation():
    """Test that safe mode works without credentials"""
    print("\n🔒 SAFE MODE TEST:")
    try:
        # Try to import and instantiate the safe engine without assuming live keys
        from revolution_engine_secure import SafeRevolutionEngine
        engine = SafeRevolutionEngine()
        print("✅ Safe mode operational - can test without credentials")
        return True
    except ImportError as ie:
        print(f"❌ Safe mode test failed: missing module ({ie})")
        print("   Ensure project files are present and dependencies installed.")
        return False
    except Exception as e:
        print(f"❌ Safe mode test failed: {e}")
        return False

import sys

def verify_credentials_live():
    """Attempt to verify credentials by loading .env into this Python process and calling the REST API."""
    # Accept common aliases for backwards compatibility
    aliases_map = {
        'consumer_key': ['TWITTER_CONSUMER_KEY', 'TWITTER_API_KEY'],
        'consumer_secret': ['TWITTER_CONSUMER_SECRET', 'TWITTER_API_SECRET'],
        'access_token': ['TWITTER_ACCESS_TOKEN'],
        'access_token_secret': ['TWITTER_ACCESS_TOKEN_SECRET', 'TWITTER_ACCESS_SECRET']
    }

    creds = {}
    missing = []
    for canon, names in aliases_map.items():
        val = None
        for n in names:
            v = os.getenv(n)
            if isinstance(v, str) and v.strip() and not v.lower().startswith('your_'):
                val = v.strip()
                break
        if val:
            creds[canon] = val
        else:
            missing.append(canon)

    if missing:
        print("\n⚠️  Cannot verify: missing keys:", ", ".join(missing))
        print("Run .\\set-twitter-env.ps1 or add keys to .env and re-run this script.")
        return False

    try:
        # Use OAuth1 verification (compatible with one-liners that use tweepy.OAuthHandler)
        try:
            from tweepy import OAuth1UserHandler as OAuthHandler  # tweepy v4 alias
        except Exception:
            from tweepy import OAuthHandler  # fallback older name

        from tweepy import API
    except Exception as e:
        print(f"\n❌ Tweepy not available: {e}")
        print("Install dependencies: pip install -r requirements.txt")
        return False

    try:
        handler = OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
        handler.set_access_token(creds['access_token'], creds['access_token_secret'])
        api = API(handler)
        user = api.verify_credentials()
        if user:
            print(f"\n✅ Live verification succeeded: @{getattr(user, 'screen_name', getattr(user, 'username', '<unknown>'))}")
            return True
        else:
            print("\n❌ Live verification failed: no user returned.")
            return False
    except Exception as e:
        # Provide actionable guidance for common errors
        err_text = str(e)
        print(f"\n❌ Verification error: {err_text}")
        if '401' in err_text or 'Unauthorized' in err_text or 'Invalid or expired token' in err_text:
            print("→ Tokens may be invalid or expired. Regenerate access tokens in the Twitter developer portal and update .env.")
        else:
            print("→ Check network access and your credentials in .env.")
        return False

if __name__ == '__main__':
    env_ok = validate_environment()
    safe_ok = test_safe_operation()

    # New: attempt live verification if all env keys present
    live_ok = False
    if env_ok:
        live_ok = verify_credentials_live()

    print("\n" + "=" * 50)
    if env_ok and safe_ok and live_ok:
        print("🎉 ENVIRONMENT READY FOR LIVE OPERATION!")
        print("Run: python revolution_engine_secure.py")
    elif safe_ok:
        print("🛡️ SAFE MODE READY FOR TESTING!")
        print("Add credentials to .env for live operation")
    else:
        print("❌ ENVIRONMENT SETUP ISSUES DETECTED")
        print("Check your Python environment and dependencies")