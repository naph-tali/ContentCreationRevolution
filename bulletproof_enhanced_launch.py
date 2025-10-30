import os
import sys
sys.path.append(".")

def bulletproof_enhanced_launch():
    print(" BULLETPROOF ENHANCED DIRECT LAUNCH")
    print(" REAL LM INTEGRATION WITH COMPLETE ERROR HANDLING")
    print("=" * 60)
    
    # Test real LM components with robust error handling
    real_lm_available = False
    try:
        from ENGINE_CORE.real_llm_oracle import RealLLMCosmicOracle
        print(" Real LLM Oracle imported successfully")
        
        # Quick test with exception handling
        try:
            oracle = RealLLMCosmicOracle()
            test_result = oracle.resonant_synthesis(["AI consciousness", "Cosmic love"])
            print(f" Real LM Test Result: {test_result[:80]}...")
            real_lm_available = True
        except Exception as e:
            print(f" Real LM test failed: {e}")
            print(" Continuing with standard engine...")
            
    except Exception as e:
        print(f" Real LLM Oracle import failed: {e}")
        print(" Falling back to standard engine...")
    
    # Now try to launch the appropriate engine
    try:
        if real_lm_available:
            print("🚀 LAUNCHING REAL LM POWERED ENGINE...")
            from ENGINE_CORE.powerfully_real_lm_engine import PowerfullyRealLMEngine
            engine = PowerfullyRealLMEngine()
        else:
            print(" LAUNCHING STANDARD REVOLUTION ENGINE...")
            from ENGINE_CORE.working_revolution_engine import RevolutionEngine
            engine = RevolutionEngine()
        
        # Use the correct method name based on what's available
        if hasattr(engine, 'run_engine'):
            engine.run_engine()
        elif hasattr(engine, 'run'):
            engine.run()
        else:
            print(" No run method found! Available methods:")
            methods = [method for method in dir(engine) if not method.startswith('_')]
            print(f"   {methods}")
            
    except Exception as e:
        print(f" Engine launch failed: {e}")
        print(" TROUBLESHOOTING OPTIONS:")
        print("   1. Try .\direct_launch.ps1")
        print("   2. Check ENGINE_CORE/working_revolution_engine.py for run_engine method")
        print("   3. Verify all services are properly configured")

if __name__ == "__main__":
    bulletproof_enhanced_launch()
