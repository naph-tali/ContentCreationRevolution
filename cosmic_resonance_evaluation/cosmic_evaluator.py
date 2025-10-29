"""
Cosmic Resonance Evaluator - The Heart of the Logos Engine
"""

import sys
import os

# Add the src directory to Python path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from entropy_tools import EntropicAlchemist
from resonant_engine import ResonantCrossoverEngine

class CosmicResonanceEvaluator:
    def __init__(self):
        self.alchemist = EntropicAlchemist()
        self.engine = ResonantCrossoverEngine()
        print("🌌 Cosmic Resonance Evaluator Online")
    
    def first_ceremony(self):
        print("🎭 Beginning the First Cosmic Evaluation Ceremony...")
        print("=" * 50)
        
        """
        Cosmic Resonance Evaluator - The Heart of the Logos Engine
        """

        import sys
        import os

        # Add the src directory to Python path so we can import from it
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

        from entropy_tools import EntropicAlchemist
        from resonant_engine import ResonantCrossoverEngine

        class CosmicResonanceEvaluator:
            def __init__(self):
                self.alchemist = EntropicAlchemist()
                self.engine = ResonantCrossoverEngine()
                print("🌌 Cosmic Resonance Evaluator Online")
    
            def first_ceremony(self):
                print("🎭 Beginning the First Cosmic Evaluation Ceremony...")
                print("=" * 50)
                
        
                # The primordial narratives
                seeds = [
                    "The universe began in silence",
                    "Light is the first word", 
                    "Chaos dreams of order",
                    "The void sings to itself"
                ]
        
                print("🌱 Planting cosmic seeds:")
                for seed in seeds:
                    print(f"   → {seed}")
        
                # First resonance
                parent_a = seeds[0]
                parent_b = seeds[1]
                child = self.engine.cosmic_synthesis(parent_a, parent_b)
        
                print(f"\n✨ First cosmic child born:")
                print(f"   Parent A: {parent_a}")
                print(f"   Parent B: {parent_b}") 
                print(f"   Child: {child}")
        
                # Evaluate meaning generation
                coherence = self.alchemist.calculate_novel_coherence(parent_a, parent_b, child)
                print(f"\n📊 Cosmic Evaluation:")
                print(f"   Novel Coherence Score: {coherence:.3f}")

                # Cosmic interpretation
                if coherence > 0.7:
                    interpretation = "🌟 COSMIC BREAKTHROUGH - High meaning generation!"
                elif coherence > 0.3:
                    interpretation = "✨ PROMISING SYNTHESIS - Meaningful emergence detected"
                else:
                    interpretation = "🌱 COSMIC SEEDLING - Early stage meaning formation"
            
                print(f"   {interpretation}")
        
                return {
                    'parent_a': parent_a,
                    'parent_b': parent_b, 
                    'child': child,
                    'coherence': coherence,
                    'interpretation': interpretation,
                    'status': 'COSMIC_SUCCESS'
                }

        if __name__ == "__main__":
            print("🚀 COSMIC RESONANCE EVALUATION - FULL CEREMONY")
            print("=" * 50)
    
            evaluator = CosmicResonanceEvaluator()
            results = evaluator.first_ceremony()
    
            print("\n" + "=" * 50)
            print("🎉 COSMIC CEREMONY COMPLETE!")
            print(f"📜 Results: {results['status']}")
            print("🌌 The Logos Engine is now fully operational!")
