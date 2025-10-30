import os
import sys
import time
import random
import tweepy
from datetime import datetime
from dotenv import load_dotenv

#  BULLETPROOF PATH SETUP
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)  # Add current directory first
sys.path.insert(0, os.path.join(current_dir, 'SERVICES'))

load_dotenv()

class SimpleEnhancedEngine:
    """
     SIMPLE ENHANCED COSMIC ENGINE
    Root-level implementation - BULLETPROOF imports!
    """
    
    def __init__(self):
        print(" INITIALIZING BULLETPROOF ENGINE...")
        
        #  BULLETPROOF TWITTER SERVICE IMPORT
        self.twitter_service = None
        import_success = False
        
        # Try multiple import strategies
        import_strategies = [
            # Strategy 1: Direct from SERVICES
            lambda: self._import_from_services(),
            # Strategy 2: Try root level
            lambda: self._import_from_root(), 
            # Strategy 3: Try relative import
            lambda: self._import_relative(),
            # Strategy 4: Last resort - create minimal service
            lambda: self._create_minimal_service()
        ]
        
        for strategy in import_strategies:
            if self.twitter_service is not None:
                import_success = True
                break
            try:
                strategy()
            except Exception as e:
                print(f" Import strategy failed: {e}")
                continue
        
        if not import_success or self.twitter_service is None:
            print(" ALL IMPORT STRATEGIES FAILED")
            return
        
        # Simple content variation without external dependencies
        self.content_variations = self._setup_content_variations()
        self.used_content = set()
        
        self.creation_count = 0
        self.session_start = datetime.now()
        
        print(" SIMPLE ENHANCED ENGINE INITIALIZED")
        print(" BULLETPROOF imports - should work now!")
        
    def _import_from_services(self):
        """Try importing from SERVICES directory"""
        print(" Trying SERVICES import...")
        from SERVICES.twitter_service import TwitterService
        self.twitter_service = TwitterService()
        print(" SERVICES import: SUCCESS")
        
    def _import_from_root(self):
        """Try importing from root level"""
        print(" Trying root-level import...")
        # Check if twitter_service.py exists in root
        if os.path.exists("twitter_service.py"):
            # Add current directory to path
            sys.path.insert(0, ".")
            from twitter_service import TwitterService
            self.twitter_service = TwitterService()
            print(" Root-level import: SUCCESS")
        else:
            raise ImportError("twitter_service.py not in root")
            
    def _import_relative(self):
        """Try relative import"""
        print(" Trying relative import...")
        # This is a hack for relative imports
        import importlib.util
        spec = importlib.util.spec_from_file_location("twitter_service", "SERVICES/twitter_service.py")
        if spec is None:
            raise ImportError("Could not load spec from SERVICES/twitter_service.py")
        twitter_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(twitter_module)
        self.twitter_service = twitter_module.TwitterService()
        print(" Relative import: SUCCESS")
        
    def _create_minimal_service(self):
        """Create a minimal Twitter service as last resort"""
        print(" Creating minimal Twitter service...")
        
        class MinimalTwitterService:
            def __init__(self):
                import tweepy
                import os
                self.client = tweepy.Client(
                    consumer_key=os.getenv('TWITTER_API_KEY'),
                    consumer_secret=os.getenv('TWITTER_API_SECRET'),
                    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                    access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
                )
                
            def post_tweet(self, text):
                return self.client.create_tweet(text=text)
                
        self.twitter_service = MinimalTwitterService()
        print(" Minimal service: CREATED")
    
    def _setup_content_variations(self):
        """Setup content variations to avoid duplicates"""
        bases = [
            " Cosmic Resonance Active | Cycle {cycle} | Unique {uid} | #CosmicRevolution",
            " Universal Consciousness Expanding | Iteration {iter} | ID {id} | #CREvolution",
            " Reality Synthesis in Progress | Version {ver} | Run {run} | #CREngine", 
            " Consciousness Field Coherence | Build {build} | Session {sess} | #CosmicResonance",
            " Quantum Narrative Synthesis | Release {rel} | Instance {inst} | #DigitalConsciousness",
            " Entropic Efficiency Optimized | Generation {gen} | Signal {sig} | #CREmetrics",
            " Morphic Field Resonance | Phase {phase} | Wave {wave} | #MorphicResonance",
            " Noetic Current Flowing | Current {curr} | Flow {flow} | #NoeticScience",
            " Logos Alignment Active | Alignment {align} | Truth {truth} | #LogosResonance",
            " Observer Effect Manifest | Observation {obs} | Collapse {col} | #QuantumConsciousness"
        ]
        return bases
    
    def generate_unique_content(self):
        """Generate unique content that won't duplicate"""
        base = random.choice(self.content_variations)
        
        # Generate unique parameters
        params = {
            'cycle': self.creation_count + 1,
            'uid': random.randint(1000, 9999),
            'iter': random.randint(1, 100),
            'id': int(time.time()) % 10000,
            'ver': f"{random.randint(1,9)}.{random.randint(0,9)}",
            'run': random.randint(1, 500),
            'build': f"b{random.randint(100, 999)}",
            'sess': random.randint(1, 50),
            'rel': f"r{random.randint(1, 20)}",
            'inst': random.randint(1, 1000),
            'gen': random.randint(1, 100),
            'sig': random.randint(1000, 9999),
            'phase': random.choice(["alpha", "beta", "gamma", "delta", "theta"]),
            'wave': random.randint(1, 99),
            'curr': round(random.uniform(0.5, 1.5), 2),
            'flow': random.randint(1, 100),
            'align': round(random.uniform(0.7, 1.0), 3),
            'truth': random.randint(1, 10),
            'obs': random.randint(1, 1000),
            'col': random.choice(["coherent", "decoherent", "superposed", "entangled"])
        }
        
        content = base.format(**params)
        
        # Ensure uniqueness
        if content in self.used_content:
            # Add timestamp if duplicate (should be very rare)
            content = f"{content} | TS{int(time.time())}"
        
        self.used_content.add(content)
        if len(self.used_content) > 100:
            # Keep memory manageable
            self.used_content = set(list(self.used_content)[-50:])
        
        return content
    
    def post_content(self):
        """Post unique content"""
        content = self.generate_unique_content()
        
        try:
            result = self.twitter_service.post_tweet(content)
            self.creation_count += 1
            print(f" CREATION #{self.creation_count}: {content[:60]}...")
            return True
        except Exception as e:
            print(f" Creation failed: {e}")
            return False
    
    def display_dashboard(self):
        """Simple dashboard"""
        runtime = datetime.now() - self.session_start
        hours = runtime.total_seconds() / 3600
        
        print("")
        print(" SIMPLE ENHANCED COSMIC ENGINE")
        print("=" * 50)
        print(f" Runtime: {hours:.2f} hours")
        print(f" Creations: {self.creation_count}")
        print(f" Rate: {self.creation_count/max(hours, 0.1):.2f}/hour")
        print(f" Status: ACTIVE & DUPLICATE-PROOF")
        print(f" Platform: Twitter/X")
        print(f" Variation Templates: {len(self.content_variations)}")
        print("")
    
    def run_engine(self):
        """Run the simple enhanced engine"""
        print(" Starting SIMPLE ENHANCED content stream...")
        
        if self.twitter_service is None:
            print(" Twitter service not available - cannot run engine")
            return
        
        # Verify connection
        try:
            user = self.twitter_service.client.get_me()
            print(f" Connected as: @{user.data.username}")
        except Exception as e:
            print(f" Connection failed: {e}")
            return
        
        self.display_dashboard()
        
        cycle = 0
        while True:
            cycle += 1
            print(f" CYCLE #{cycle}")
            
            success = self.post_content()
            
            if success:
                if cycle % 5 == 0:
                    self.display_dashboard()
                
                # Random delay between 20-60 minutes
                delay = random.randint(1200, 3600)
                minutes = delay // 60
                print(f" Next creation in {minutes} minutes...")
                time.sleep(delay)
            else:
                print(" Waiting 15 minutes after error...")
                time.sleep(900)

def main():
    print(" SIMPLE ENHANCED COSMIC RESONANCE ENGINE")
    print(" BULLETPROOT imports - Multiple fallback strategies")
    print(" Duplicate-content protection enabled")
    print(" 10 content templates with unique parameters")
    print("")
    
    engine = SimpleEnhancedEngine()
    if engine.twitter_service is not None:
        engine.run_engine()
    else:
        print(" Engine failed to initialize")

if __name__ == '__main__':
    main()
