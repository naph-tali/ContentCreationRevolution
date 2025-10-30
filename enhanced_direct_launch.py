import os
import sys
sys.path.append(".")

def enhanced_direct_launch():
    print("🚀 ENHANCED DIRECT LAUNCH - REAL LM INTEGRATION")
    print("🎯 Testing Real LM Systems First...")
    
    # Test real LM components
    try:
        from ENGINE_CORE.real_llm_oracle import RealLLMCosmicOracle
        print(" Real LLM Oracle available")
        
        # Quick test
        oracle = RealLLMCosmicOracle()
        test_result = oracle.resonant_synthesis(["AI consciousness", "Cosmic love"])
        print(f" Quick LM Test: {test_result[:80]}...")
        
    except Exception as e:
        print(f" Real LM test failed: {e}")
        print(" Falling back to standard engine...")
    
    # Launch the standard engine (which should now have real LM)
    from ENGINE_CORE.working_revolution_engine import RevolutionEngine
    engine = RevolutionEngine()
    engine.run_engine()

if __name__ == "__main__":
    enhanced_direct_launch()
