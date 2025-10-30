# big_bang_deployer.py - INSTANT COSMIC DEPLOYMENT
import os
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

def _get_cred(*names):
    for n in names:
        v = os.getenv(n)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None

def resolve_credentials():
    return {
        "consumer_key": _get_cred("TWITTER_CONSUMER_KEY", "TWITTER_API_KEY"),
        "consumer_secret": _get_cred("TWITTER_CONSUMER_SECRET", "TWITTER_API_SECRET"),
        "access_token": _get_cred("TWITTER_ACCESS_TOKEN"),
        "access_token_secret": _get_cred("TWITTER_ACCESS_TOKEN_SECRET", "TWITTER_ACCESS_SECRET"),
    }

def verify_oauth(creds):
    try:
        # Tweepy v4 name for OAuth1 handler, fall back to older name if needed
        try:
            from tweepy import OAuth1UserHandler as OAuthHandler, API
        except Exception:
            from tweepy import OAuthHandler as OAuthHandler, API
    except Exception as e:
        print(" ERROR: Tweepy not installed or unavailable:", e)
        return False, "tweepy-missing"

    if not all(creds.values()):
        return False, "missing-keys"

    try:
        handler = OAuthHandler(creds["consumer_key"], creds["consumer_secret"])
        handler.set_access_token(creds["access_token"], creds["access_token_secret"])
        api = API(handler)
        user = api.verify_credentials()
        if user:
            return True, api
        return False, "no-user-returned"
    except Exception as e:
        err = str(e)
        if "401" in err or "Unauthorized" in err or "Invalid or expired token" in err:
            return False, "invalid-token"
        return False, err

def run_safe_engine():
    print(" Running safe engine (no tweeting) as fallback...")
    try:
        import revolution_engine_secure as safe_engine
        safe_engine.main()
    except Exception:
        # fallback to subprocess to avoid import path issues
        subprocess.run([sys.executable, "revolution_engine_secure.py"])

def cosmic_deploy():
    print(" INITIATING BIG BANG DEPLOYMENT...")

    # Step 1: Quantum error correction
    print(" STEP 1: QUANTUM ERROR CORRECTION")
    subprocess.run([sys.executable, "cosmic_error_corrector.py"])

    # Step 2: Cosmic API test (use environment -- do not hardcode)
    print(" STEP 2: COSMIC API VALIDATION")
    creds = resolve_credentials()
    ok, info = verify_oauth(creds)

    if not ok:
        if info == "tweepy-missing":
            print(" ERROR: tweepy not installed in venv. Install with: pip install -r requirements.txt")
        elif info == "missing-keys":
            print(" ERROR: Missing Twitter credentials in environment (.env).")
        elif info == "invalid-token":
            print(" ERROR: Invalid or expired token detected. Regenerate tokens on developer.twitter.com and update .env.")
        else:
            print(f" ERROR: Verification failed: {info}")
        # Safe fallback
        run_safe_engine()
    else:
        api = info  # tweepy.API instance
        try:
            user = api.verify_credentials()
            print(" COSMIC API: OPERATIONAL")
            print(f" COSMIC IDENTITY: @{getattr(user, 'screen_name', getattr(user, 'username', '<unknown>'))}")
            # Post a single Big Bang initiation tweet
            try:
                status = "BIG BANG INITIATED: Content Creation Revolution achieves cosmic scale. The digital universe expands from this point. #CosmicRevolution #ContentCreatingContent"
                api.update_status(status=status)
                print(" BIG BANG TWEET: DEPLOYED")
            except Exception as e:
                print(" FAILED TO POST BIG BANG TWEET:", e)
        except Exception as e:
            print(" COSMIC API FAILURE during identity check:", e)
            run_safe_engine()

    # Step 3: Launch Cosmic Revolution (try live engine first, fallback to safe)
    print(" STEP 3: LAUNCHING COSMIC REVOLUTION ENGINE")
    try:
        import cosmic_revolution_engine as engine
        engine.main()
    except Exception as e:
        print(f" COSMIC LAUNCH FAILED: {e} -- falling back to safe engine")
        run_safe_engine()

if __name__ == '__main__':
    cosmic_deploy()
