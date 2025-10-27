import os
import sys
import importlib.util

class CREBridge:
    """
    Bridge to Cosmic Resonance Evaluation modules from cosmic-projects
    """
    
    def __init__(self):
        self.cre_path = self.find_cre_path()
        self.modules = {}
        self.available = False
        
        if self.cre_path:
            self.initialize_cre_modules()
    
    def find_cre_path(self):
        """Find the cosmic-projects directory"""
        possible_paths = [
            os.path.join(os.path.dirname(__file__), "..", "..", "cosmic-projects"),
            os.path.join(os.path.dirname(__file__), "..", "cosmic-projects"),
            "C:/Users/X/Documents/cosmic-projects"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None
    
    def load_module(self, module_name):
        """Dynamically load a CRE module"""
        if not self.cre_path:
            return None
            
        module_path = os.path.join(self.cre_path, f"{module_name}.py")
        if not os.path.exists(module_path):
            return None
            
        try:
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            print(f"Failed to load {module_name}: {e}")
            return None
    
    def initialize_cre_modules(self):
        """Initialize all available CRE modules"""
        module_names = [
            "mathematical_foundation",
            "entropy_tools", 
            "evaluation_metrics",
            "narrative_synthesis",
            "resonant_engine",
            "cosmic_core"
        ]
        
        for name in module_names:
            module = self.load_module(name)
            if module:
                self.modules[name] = module
                print(f" Loaded CRE module: {name}")
        
        self.available = len(self.modules) > 0
        print(f"CRE Bridge: {' READY' if self.available else ' UNAVAILABLE'}")
    
    def calculate_cosmic_resonance(self, narrative1, narrative2):
        """Calculate cosmic resonance between narratives"""
        if 'evaluation_metrics' in self.modules:
            try:
                return self.modules['evaluation_metrics'].calculate_resonance(narrative1, narrative2)
            except:
                pass
        return 0.7  # Default resonance
    
    def synthesize_narrative(self, seed, creativity=0.8):
        """Synthesize cosmic narrative"""
        if 'narrative_synthesis' in self.modules:
            try:
                return self.modules['narrative_synthesis'].synthesize(seed, creativity)
            except:
                pass
        return f"Cosmic narrative: {seed}"  # Fallback
    
    def measure_entropic_flow(self, content):
        """Measure entropic flow of content"""
        if 'entropy_tools' in self.modules:
            try:
                return self.modules['entropy_tools'].calculate_entropy(content)
            except:
                pass
        return 0.5  # Default entropy

# Example usage
if __name__ == '__main__':
    bridge = CREBridge()
    if bridge.available:
        resonance = bridge.calculate_cosmic_resonance("CCR Content", "CRE Metrics")
        print(f"Cosmic Resonance: {resonance}")
    else:
        print("CRE modules not available")
