# SERVICES/platform_manager.py
class PlatformManager:
    """Manages all platform integrations in one place"""
    
    def __init__(self):
        from SERVICES.twitter_service import TwitterService
        self.twitter = TwitterService()
        self.platforms = [self.twitter]  # Add Instagram, TikTok later
        
    def distribute_content(self, content):
        """Send to all active platforms"""
        for platform in self.platforms:
            try:
                platform.post_content(content)
            except Exception as e:
                print(f"Platform error: {e}")