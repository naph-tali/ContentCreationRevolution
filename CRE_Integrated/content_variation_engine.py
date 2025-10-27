import random
import time
from datetime import datetime

class ContentVariationEngine:
    """
     CONTENT VARIATION ENGINE
    Prevents duplicate content by generating unique variations
    """
    
    def __init__(self):
        self.base_templates = [
            " Cosmic Resonance Active | CCR + CRE Unified Engine | {variation} | #CosmicRevolution",
            " Universal Consciousness Expanding | CCR + CRE Integration | {variation} | #CREvolution", 
            " Reality Synthesis in Progress | CCR + CRE Operational | {variation} | #CREngine",
            " Consciousness Field Coherence | CCR + CRE Active | {variation} | #CosmicResonance",
            " Quantum Narrative Synthesis | CCR + CRE Evolving | {variation} | #DigitalConsciousness"
        ]
        
        self.variations = [
            "Cycle {cycle}",
            "Time {timestamp}",
            "Resonance {random_id}",
            "Field Strength {field_strength}",
            "Consciousness Ψ{psi_value}",
            "Entropy η{eta_value}",
            "Evolution v{version}",
            "Unity Factor {unity}",
            "Morphic Field {morphic}",
            "Noetic Current {noetic}"
        ]
        
        self.used_combinations = set()
        self.cycle_count = 0
        
    def generate_unique_content(self):
        """Generate unique content that won't trigger duplicate detection"""
        self.cycle_count += 1
        
        max_attempts = 10
        for attempt in range(max_attempts):
            # Select random template and variation
            template = random.choice(self.base_templates)
            variation_template = random.choice(self.variations)
            
            # Generate unique variation values
            variation_data = {
                'cycle': self.cycle_count,
                'timestamp': int(time.time()) % 10000,
                'random_id': random.randint(1000, 9999),
                'field_strength': round(random.uniform(0.8, 1.2), 3),
                'psi_value': round(random.uniform(0.9, 1.1), 3),
                'eta_value': round(random.uniform(0.5, 0.9), 3),
                'version': f"{random.randint(1,9)}.{random.randint(0,9)}",
                'unity': round(random.uniform(0.7, 1.0), 2),
                'morphic': round(random.uniform(0.8, 1.2), 2),
                'noetic': round(random.uniform(0.6, 1.0), 2)
            }
            
            # Format variation
            variation = variation_template.format(**variation_data)
            
            # Format final content
            content = template.format(variation=variation)
            
            # Check if we've used this combination recently
            content_hash = hash(content)
            if content_hash not in self.used_combinations:
                self.used_combinations.add(content_hash)
                
                # Keep only recent 100 combinations to manage memory
                if len(self.used_combinations) > 100:
                    self.used_combinations = set(list(self.used_combinations)[-50:])
                
                return content
        
        # If all attempts fail, use timestamp-based fallback
        return f" Cosmic Resonance Active | Unique {int(time.time())} | #CosmicRevolution"
    
    def get_variation_stats(self):
        """Get statistics on content variation"""
        return {
            'total_cycles': self.cycle_count,
            'unique_combinations': len(self.used_combinations),
            'templates_available': len(self.base_templates),
            'variations_available': len(self.variations)
        }

# Test the variation engine
if __name__ == '__main__':
    engine = ContentVariationEngine()
    
    print("🧪 CONTENT VARIATION ENGINE TEST")
    print("=" * 50)
    
    for i in range(5):
        content = engine.generate_unique_content()
        print(f"{i+1}. {content}")
    
    stats = engine.get_variation_stats()
    print(f"\n Stats: {stats}")
