import os
import sys
import importlib.util

class CREBridgeFixed:
    """
    FIXED BRIDGE to Cosmic Resonance Evaluation modules with absolute paths
    """
    
    def __init__(self):
        # Absolute path to cosmic-projects
        self.cre_path = r"C:\Users\X\Documents\cosmic-projects"
        self.modules = {}
        self.available = False
        
        if os.path.exists(self.cre_path):
            print(f" CRE Path Found: {self.cre_path}")
            self.initialize_cre_modules()
        else:
            print(f" CRE Path Not Found: {self.cre_path}")
    
    def load_module(self, module_name):
        """Dynamically load a CRE module with absolute path"""
        module_path = os.path.join(self.cre_path, f"{module_name}.py")
        
        if not os.path.exists(module_path):
            print(f" Module not found: {module_path}")
            return None
            
        try:
            # Add the directory to sys.path for imports
            if self.cre_path not in sys.path:
                sys.path.append(self.cre_path)
            
            # Import the module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            print(f" Loaded: {module_name}")
            return module
        except Exception as e:
            print(f" Failed to load {module_name}: {e}")
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
        
        loaded_count = 0
        for name in module_names:
            module = self.load_module(name)
            if module:
                self.modules[name] = module
                loaded_count += 1
        
        self.available = loaded_count > 0
        print(f" CRE Bridge: {loaded_count}/{len(module_names)} modules loaded")
    
    def calculate_cosmic_resonance(self, narrative1, narrative2):
        """Calculate cosmic resonance between narratives"""
        if 'evaluation_metrics' in self.modules:
            try:
                return self.modules['evaluation_metrics'].calculate_resonance(narrative1, narrative2)
            except Exception as e:
                print(f"Resonance calculation failed: {e}")
        return 0.75  # Default resonance
    
    def synthesize_narrative(self, seed, creativity=0.8):
        """Synthesize cosmic narrative"""
        if 'narrative_synthesis' in self.modules:
            try:
                return self.modules['narrative_synthesis'].synthesize(seed, creativity)
            except Exception as e:
                print(f"Narrative synthesis failed: {e}")
        return f"Cosmic narrative: {seed}"  # Fallback

# Test the bridge
if __name__ == '__main__':
    bridge = CREBridgeFixed()
    if bridge.available:
        print(" CRE Bridge:  OPERATIONAL")
        # Test a function
        resonance = bridge.calculate_cosmic_resonance("test1", "test2")
        print(f"Test Resonance: {resonance}")
    else:
        print(" CRE Bridge:  BASIC MODE")
