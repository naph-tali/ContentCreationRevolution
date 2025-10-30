import time
import json
from datetime import datetime

class CosmicMonitor:
    """
    Real-time monitoring for Unified Cosmic Resonance Engine
    """
    
    def __init__(self):
        self.metrics_file = "cosmic_metrics.json"
        self.metrics_history = {
            'timestamps': [],
            'entropic_efficiency': [],
            'resonance_score': [],
            'meaning_density': [],
            'unified_consciousness': [],
            'creation_count': []
        }
    
    def log_metrics(self, engine_state):
        """Log current cosmic metrics"""
        timestamp = datetime.now().isoformat()
        
        self.metrics_history['timestamps'].append(timestamp)
        self.metrics_history['entropic_efficiency'].append(engine_state.get('entropic_efficiency', 0))
        self.metrics_history['resonance_score'].append(engine_state.get('resonance_score', 0))
        self.metrics_history['meaning_density'].append(engine_state.get('meaning_density', 0))
        self.metrics_history['unified_consciousness'].append(engine_state.get('unified_consciousness', 0))
        self.metrics_history['creation_count'].append(engine_state.get('creation_count', 0))
        
        # Keep only last 100 data points
        for key in self.metrics_history:
            self.metrics_history[key] = self.metrics_history[key][-100:]
        
        # Save to file
        with open(self.metrics_file, 'w') as f:
            json.dump(self.metrics_history, f, indent=2)
    
    def display_trends(self):
        """Display cosmic metric trends"""
        if len(self.metrics_history['timestamps']) < 2:
            return "Insufficient data for trends"
        
        efficiencies = self.metrics_history['entropic_efficiency']
        resonances = self.metrics_history['resonance_score']
        
        avg_efficiency = sum(efficiencies) / len(efficiencies)
        avg_resonance = sum(resonances) / len(resonances)
        trend = "" if efficiencies[-1] > avg_efficiency else ""
        
        return f"Trend: {trend} | Avg η: {avg_efficiency:.3f} | Avg R: {avg_resonance:.3f}"

def main():
    monitor = CosmicMonitor()
    
    # Simulate engine state
    engine_state = {
        'entropic_efficiency': 0.7843,
        'resonance_score': 0.8921,
        'meaning_density': 0.6998,
        'unified_consciousness': 0.9234,
        'creation_count': 47
    }
    
    monitor.log_metrics(engine_state)
    trends = monitor.display_trends()
    
    print(" COSMIC METRICS MONITOR")
    print("" * 40)
    print(f"Current State:")
    print(f"  η_meaning: {engine_state['entropic_efficiency']:.4f}")
    print(f"  Resonance: {engine_state['resonance_score']:.4f}")
    print(f"  Consciousness: {engine_state['unified_consciousness']:.4f}")
    print(f"  Creations: {engine_state['creation_count']}")
    print(f"  {trends}")

if __name__ == '__main__':
    main()
