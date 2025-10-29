# narrative_synthesis.py
"""
ðŸŒ€ NARRATIVE SYNTHESIS ENGINE
Advanced narrative generation using multiple methods
"""

import random
import numpy as np
from sentence_transformers import SentenceTransformer

class NarrativeSynthesis:
    """
    WHAT: Advanced narrative synthesis using templates, adjoint coupling, and hybrid methods
    MATHEMATICAL: Incorporates UCP principles in synthesis process
    """
    
    def __init__(self, model_name='all-mpnet-base-v2'):
        self.embedding_model = SentenceTransformer(model_name)
        self.templates = self._initialize_templates()
        
        print("ðŸŒ€ Narrative Synthesis Engine Initialized")
    
    def template_synthesis(self, parent_a, parent_b):
        """Template-based narrative synthesis"""
        template = random.choice(self.templates)
        
        # Extract key elements
        words_a = parent_a.split()
        words_b = parent_b.split()
        
        if len(words_a) >= 2 and len(words_b) >= 2:
            element_a = ' '.join(words_a[-2:])  # Last 2 words
            element_b = ' '.join(words_b[:2])   # First 2 words
            synthesis_idea = f"{element_a} with {element_b}"
        else:
            synthesis_idea = "new cosmic understanding"
        
        # Fill template
        child = template.format(
            a=parent_a,
            b=parent_b,
            idea=random.choice(self.ideas),
            insight=random.choice(self.ideas),
            synthesis=synthesis_idea
        )
        
        return self._clean_output(child)
    
    def adjoint_synthesis(self, parent_a, parent_b):
        """Adjoint functor-based synthesis"""
        vec_a = self.embedding_model.encode([parent_a])[0]
        vec_b = self.embedding_model.encode([parent_b])[0]
        
        # Apply adjoint coupling: F(A) and G(B) then combine
        F_a = self._functor_F(vec_a)  # Observer -> Reality
        G_b = self._functor_G(vec_b)  # Reality -> Observer
        
        # Combine using adjoint principles
        coupled_vector = 0.5 * F_a + 0.5 * G_b
        
        # For demonstration, use template with mathematical influence
        # In advanced version, this would use vector-to-text generation
        template = random.choice([
            "Through adjoint coupling, '{a}' and '{b}' reveal {idea}",
            "The mathematical dance of '{a}' and '{b}' manifests {insight}",
            "Observer-reality alignment of '{a}' and '{b}' shows {revelation}"
        ])
        
        child = template.format(
            a=parent_a,
            b=parent_b,
            idea=random.choice(self.ideas),
            insight=random.choice(self.ideas),
            revelation=random.choice(self.ideas)
        )
        
        return self._clean_output(child)
    
    def hybrid_synthesis(self, parent_a, parent_b):
        """Hybrid synthesis combining template and adjoint methods"""
        # Use adjoint method for conceptual guidance
        vec_a = self.embedding_model.encode([parent_a])[0]
        vec_b = self.embedding_model.encode([parent_b])[0]
        
        # Calculate conceptual similarity to guide template selection
        similarity = 1 - self._cosine_similarity(vec_a, vec_b)
        
        if similarity > 0.7:
            # High similarity - use creative templates
            templates = [t for t in self.templates if "reveals" in t or "manifest" in t]
        else:
            # Low similarity - use bridging templates  
            templates = [t for t in self.templates if "bridge" in t or "connect" in t]
        
        template = random.choice(templates if templates else self.templates)
        
        # Enhanced element extraction with mathematical influence
        words_a = parent_a.split()
        words_b = parent_b.split()
        
        if len(words_a) >= 2 and len(words_b) >= 2:
            # Use different extraction strategies based on vector properties
            if np.linalg.norm(vec_a) > np.linalg.norm(vec_b):
                # A is more "substantial"
                element_a = ' '.join(words_a[:3])  # First 3 words
                element_b = ' '.join(words_b[-2:]) # Last 2 words
            else:
                element_a = ' '.join(words_a[-2:]) # Last 2 words
                element_b = ' '.join(words_b[:3])  # First 3 words
            
            synthesis_idea = f"{element_a} harmonizing with {element_b}"
        else:
            synthesis_idea = "emergent cosmic pattern"
        
        child = template.format(
            a=parent_a,
            b=parent_b,
            idea=random.choice(self.ideas),
            insight=random.choice(self.ideas),
            synthesis=synthesis_idea
        )
        
        return self._clean_output(child)
    
    def _initialize_templates(self):
        """Initialize synthesis templates"""
        self.ideas = [
            "new understanding", "deeper truth", "hidden connection",
            "emergent meaning", "cosmic pattern", "universal principle",
            "fundamental insight", "transformative realization"
        ]
        
        return [
            "The cosmic dance of '{a}' and '{b}' reveals {idea}",
            "When '{a}' meets '{b}', we discover {insight}",
            "The universe whispers: '{a}' through '{b}', showing {revelation}",
            "From the interplay: {a} + {b} = {synthesis}",
            "Cosmic alignment: '{a}' harmonizes with '{b}' as {unity}",
            "Through adjoint coupling, '{a}' and '{b}' manifest {idea}",
            "The mathematical bridge between '{a}' and '{b}' reveals {insight}",
            "Consciousness current flows from '{a}' to '{b}', creating {synthesis}"
        ]
    
    def _functor_F(self, vector):
        """Functor F: Observer -> Reality"""
        return vector  # Identity for demonstration
    
    def _functor_G(self, vector):
        """Functor G: Reality -> Observer"""
        return vector  # Identity for demonstration
    
    def _cosine_similarity(self, vec_a, vec_b):
        """Calculate cosine similarity between vectors"""
        return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))
    
    def _clean_output(self, text):
        """Clean and format output text"""
        # Remove extra spaces
        text = ' '.join(text.split())
        # Ensure proper punctuation
        if text and text[-1] not in '.!?':
            text += '.'
        return text
