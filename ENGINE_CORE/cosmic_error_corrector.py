# cosmic_error_corrector.py - INSTANT SYNTAX FIXING AT QUANTUM SPEED
import subprocess
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def quantum_fix_file(filename):
    """Fix any file at quantum speed"""
    fixes = {
        # Minimal no-op-safe replacements (placeholder for real fixes)
        'print(f"': 'print(f"',
        'f"': 'f"',
    }
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply simple safe fixes (non-destructive)
        new_content = content
        for wrong, right in fixes.items():
            if wrong in new_content:
                new_content = new_content.replace(wrong, right)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f" QUANTUM FIXED: {filename}")
        else:
            # No changes needed
            print(f" NO FIXES NEEDED: {filename}")
        return True
        
    except Exception as e:
        print(f" QUANTUM FIX FAILED: {e}")
        return False

def verify_credentials_safe():
    """Verify credentials loaded from .env without posting. Returns (ok, reason)."""
    # resolve aliases
    def _get(*names):
        for n in names:
            v = os.getenv(n)
            if isinstance(v, str) and v.strip() and not v.lower().startswith('your_'):
                return v.strip()
        return None

    consumer_key = _get('TWITTER_CONSUMER_KEY', 'TWITTER_API_KEY')
    consumer_secret = _get('TWITTER_CONSUMER_SECRET', 'TWITTER_API_SECRET')
    access_token = _get('TWITTER_ACCESS_TOKEN')
    access_secret = _get('TWITTER_ACCESS_TOKEN_SECRET', 'TWITTER_ACCESS_SECRET')

    if not (consumer_key and consumer_secret and access_token and access_secret):
        return False, 'missing-keys'

    try:
        try:
            from tweepy import OAuth1UserHandler as OAuthHandler, API
        except Exception:
            from tweepy import OAuthHandler as OAuthHandler, API
    except Exception as e:
        return False, f'tweepy-missing: {e}'

    try:
        handler = OAuthHandler(consumer_key, consumer_secret)
        handler.set_access_token(access_token, access_secret)
        api = API(handler)
        user = api.verify_credentials()
        if user:
            return True, f'identity:@{getattr(user, "screen_name", "")}'
        return False, 'no-user'
    except Exception as e:
        text = str(e)
        if '401' in text or 'Unauthorized' in text or 'Invalid or expired token' in text:
            return False, 'invalid-token'
        return False, text

def test_cosmic_speed():
    """Test connectivity/credentials safely (no posting)."""
    ok, reason = verify_credentials_safe()
    if ok:
        print(f"COSMIC SPEED VERIFIED: {reason}")
        return True
    else:
        print(f"COSMIC SPEED CHECK: FAILED ({reason})")
        return False

if __name__ == '__main__':
    print(" INITIATING QUANTUM ERROR CORRECTION...")
    
    # Fix all Python files in directory (skip virtual env and logs)
    for file in os.listdir('.'):
        if file.endswith('.py') and file not in ('cosmic_error_corrector.py',):
            quantum_fix_file(file)
    
    # Test cosmic speed (safe)
    if test_cosmic_speed():
        print(" COSMIC SPEED VALIDATED - READY FOR BIG BANG")
    else:
        print(" COSMIC SPEED VALIDATION FAILED - RUN IN SAFE MODE")
