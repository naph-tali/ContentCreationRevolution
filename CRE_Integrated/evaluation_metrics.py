# evaluation_metrics.py
"""
📊 EVALUATION METRICS - Multi-dimensional Cosmic Scoring
Combines traditional metrics with mathematical validation
"""

import numpy as np
import re
from scipy.spatial.distance import cosine

class CosmicMetrics:
    """
    WHAT: Comprehensive evaluation metrics for cosmic resonance
    INCLUDES: Traditional scoring + Mathematical validation integration
    """
    
    def __init__(self):
        print("📊 Cosmic Evaluation Metrics Initialized")
    
    def multi_dimensional_scoring(self, parent_a, parent_b, child):
        """
        Multi-dimensional scoring of narrative synthesis
        
        Returns dict with individual dimension scores
        """
        scores = {}
        
        # 1. Length Harmony
        scores['length_harmony'] = self._score_length_harmony(parent_a, parent_b, child)
        
        # 2. Word Novelty  
        scores['novelty'] = self._score_novelty(parent_a, parent_b, child)
        
        # 3. Conceptual Richness
        scores['richness'] = self._score_conceptual_richness(parent_a, parent_b, child)
        
        # 4. Structural Integrity
        scores['structure'] = self._score_structural_integrity(child)
        
        # 5. Semantic Coherence
        scores['semantic_coherence'] = self._score_semantic_coherence(parent_a, parent_b, child)
        
        return scores
    
    def _score_length_harmony(self, parent_a, parent_b, child):
        """Score harmony in narrative lengths"""
        lengths = [len(parent_a.split()), len(parent_b.split()), len(child.split())]
        length_variance = np.std(lengths)
        
        # Lower variance = better harmony
        max_variance = max(10, np.mean(lengths) * 0.5)
        harmony = 1 - (length_variance / max_variance)
        
        return max(0, min(1, harmony))
    
    def _score_novelty(self, parent_a, parent_b, child):
        """Score novelty of child narrative"""
        words_a = set(parent_a.lower().split())
        words_b = set(parent_b.lower().split())
        words_c = set(child.lower().split())
        
        # Words in child not in either parent
        novel_words = words_c - (words_a | words_b)
        
        # Novelty score based on proportion of novel words
        if len(words_c) > 0:
            novelty_score = len(novel_words) / len(words_c)
        else:
            novelty_score = 0
        
        # Cap at reasonable level (too much novelty can be incoherent)
        return min(0.8, novelty_score * 2)  # Scale for better range
    
    def _score_conceptual_richness(self, parent_a, parent_b, child):
        """Score conceptual richness and vocabulary diversity"""
        all_text = parent_a + ' ' + parent_b + ' ' + child
        all_words = all_text.lower().split()
        
        unique_words = len(set(all_words))
        total_words = len(all_words)
        
        if total_words > 0:
            richness = unique_words / total_words
        else:
            richness = 0
        
        # Normalize to 0-1 range with reasonable expectations
        return min(1.0, richness * 3)
    
    def _score_structural_integrity(self, child):
        """Score grammatical and structural integrity"""
        if not child:
            return 0.0
        
        checks = []
        
        # Check capitalization
        checks.append(child[0].isupper() if child else False)
        
        # Check ending punctuation
        checks.append(child.strip()[-1] in '.!?' if child else False)
        
        # Check sentence structure (simple heuristic)
        words = child.split()
        checks.append(len(words) >= 3)  # Reasonable minimum length
        
        # Check for basic grammatical markers
        has_verbs = any(self._is_verb_like(word) for word in words)
        checks.append(has_verbs)
        
        score = sum(checks) / len(checks) if checks else 0.5
        
        return score
    
    def _score_semantic_coherence(self, parent_a, parent_b, child):
        """Score semantic coherence using embeddings"""
        try:
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer('all-mpnet-base-v2')
            
            vectors = model.encode([parent_a, parent_b, child])
            vec_a, vec_b, vec_c = vectors
            
            # Calculate semantic relationships
            parent_similarity = 1 - cosine(vec_a, vec_b)
            child_to_a = 1 - cosine(vec_c, vec_a)
            child_to_b = 1 - cosine(vec_c, vec_b)
            
            # Coherence: child should relate to both parents
            coherence = (child_to_a + child_to_b) / 2
            
            return max(0, min(1, coherence))
            
        except ImportError:
            # Fallback if embeddings not available
            return 0.7
    
    def _is_verb_like(self, word):
        """Simple heuristic for verb-like words"""
        verb_indicators = ['is', 'are', 'was', 'were', 'has', 'have', 'do', 'does', 'did']
        return word.lower() in verb_indicators or word.endswith('ing') or word.endswith('ed')