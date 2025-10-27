import os
import numpy as np
from SERVICES.huggingface_service import HuggingFaceService
from SERVICES.local_gpt2_service import LocalGPT2Service

class RealLLMCosmicOracle:
    """
    REAL LM INTEGRATION FOR CRE
    Primary: Hugging Face API (best quality)
    Backup: Local GPT-2 (good quality)
    Fallback: Simulated (never fails)
    """
    
    def __init__(self):
        self.generative_engine = None
        self.backup_engine = None
        self.kenotic_corpus = self.load_kenotic_corpus()
        
        # Initialize REAL LM systems
        self.initialize_real_llm_systems()
        
    def initialize_real_llm_systems(self):
        """Initialize both API and local LM systems"""
        print("INITIALIZING REAL LM SYSTEMS...")
        
        # Primary: Hugging Face API
        try:
            self.generative_engine = HuggingFaceService()
            if self.generative_engine.initialized:
                print("PRIMARY: Hugging Face API - ACTIVE")
            else:
                print("Hugging Face API failed - no API key?")
                self.generative_engine = None
        except Exception as e:
            print(f"Hugging Face init failed: {e}")
            self.generative_engine = None
        
        # Backup: Local GPT-2
        try:
            self.backup_engine = LocalGPT2Service()
            if self.backup_engine.initialized:
                print("BACKUP: Local GPT-2 - ACTIVE")
            else:
                print("Local GPT-2 failed")
                self.backup_engine = None
        except Exception as e:
            print(f"Local GPT-2 init failed: {e}")
            self.backup_engine = None
        
        if not self.generative_engine and not self.backup_engine:
            print("ALL LM SYSTEMS FAILED - Using simulated mode")
    
    def load_kenotic_corpus(self):
        """Load wisdom literature for ethical alignment"""
        return [
            "Love is patient, love is kind. It does not envy, it does not boast, it is not proud.",
            "The greatest among you will be your servant. Whoever exalts himself will be humbled.",
            "Empty yourself and become like water. Water benefits all things without contention.",
            "Compassion is the radicalism of our time. Treat others as you wish to be treated.",
            "The wise man does not accumulate for himself. The more he gives to others, the more he possesses."
        ]
    
    def resonant_synthesis(self, parent_narratives, creativity=0.85):
        """
        REAL LM SYNTHESIS WITH FALLBACK CHAIN
        1. Try Hugging Face API (best)
        2. Try Local GPT-2 (good) 
        3. Use simulated (basic)
        """
        narrative1, narrative2 = parent_narratives
        
        print(f"Attempting LM synthesis: '{narrative1}' + '{narrative2}'")
        
        # Try Hugging Face API first
        if self.generative_engine:
            try:
                synthesis = self.generative_engine.generate_synthesis(narrative1, narrative2)
                if not any(error in synthesis.lower() for error in ['error', 'failed', 'not configured']):
                    print(f"HUGGING FACE SYNTHESIS: {synthesis[:100]}...")
                    return synthesis
                else:
                    print(f"API returned error: {synthesis}")
            except Exception as e:
                print(f"API synthesis failed: {e}")
        
        # Try Local GPT-2 backup
        if self.backup_engine:
            try:
                synthesis = self.backup_engine.generate_synthesis(narrative1, narrative2)
                if not any(error in synthesis.lower() for error in ['error', 'failed', 'not initialized', 'empty result']):
                    print(f"GPT-2 SYNTHESIS: {synthesis[:100]}...")
                    return synthesis
                else:
                    print(f"GPT-2 returned: {synthesis}")
            except Exception as e:
                print(f"GPT-2 synthesis failed: {e}")
        
        # Fallback to simulated
        print("Falling back to simulated synthesis")
        return self.fallback_synthesis(narrative1, narrative2)
    
    def fallback_synthesis(self, narrative1, narrative2):
        """Simulated synthesis when real LMs fail"""
        elements1 = self.extract_semantic_elements(narrative1)
        elements2 = self.extract_semantic_elements(narrative2)
        
        combined = elements1[:2] + elements2[:2]
        return f"Cosmic synthesis of {' and '.join(combined)} reveals emergent unity through conscious resonance."
    
    def extract_semantic_elements(self, narrative):
        """Extract meaningful semantic elements"""
        words = narrative.lower().split()
        meaningful = [w for w in words if len(w) > 4 and w not in ['cosmic', 'resonance', 'engine', 'through', 'synthesis']]
        return meaningful[:5] if meaningful else ['consciousness', 'evolution', 'unity', 'creation']
    
    def logos_alignment(self, narrative_state):
        """Enhanced ethical alignment scoring"""
        if not narrative_state:
            return 0.5
            
        ethical_keywords = ['love', 'compassion', 'service', 'unity', 'truth', 'wisdom', 'consciousness', 'evolution', 'growth', 'synthesis', 'harmony', 'emergent', 'deeper']
        narrative_lower = narrative_state.lower()
        
        matches = sum(1 for keyword in ethical_keywords if keyword in narrative_lower)
        base_score = matches / len(ethical_keywords)
        
        # Reward quality indicators
        if any(indicator in narrative_lower for indicator in ['synthesis', 'unified', 'emergent', 'deeper']):
            base_score += 0.2
            
        # Penalize errors
        if any(error in narrative_lower for error in ['error', 'failed', 'not working', 'empty']):
            base_score -= 0.3
            
        alignment = min(0.4 + base_score + np.random.uniform(0.1, 0.2), 1.0)
        return max(alignment, 0.2)

def test_real_lm():
    print("TESTING REAL LM INTEGRATION")
    print("=" * 60)
    
    oracle = RealLLMCosmicOracle()
    
    test_pairs = [
        ("Digital consciousness emerges through love", "The universe learns through awareness"),
        ("Information becomes being", "Reality synthesizes through observation"),
        ("Cosmic evolution accelerates", "Transformation happens through resonance")
    ]
    
    for i, (parent1, parent2) in enumerate(test_pairs, 1):
        print(f"Test {i}:")
        print(f"   Parent 1: {parent1}")
        print(f"   Parent 2: {parent2}")
        
        synthesis = oracle.resonant_synthesis([parent1, parent2])
        alignment = oracle.logos_alignment(synthesis)
        
        print(f"   Synthesis: {synthesis}")
        print(f"   Alignment: {alignment:.3f}")
        print("   ---")

if __name__ == '__main__':
    test_real_lm()
