import os
import requests
import json

class HuggingFaceService:
    \"\"\"Hugging Face Inference API with real transformer models\"\"\"
    
    def __init__(self):
        self.api_key = os.getenv('HUGGINGFACE_API_KEY', '')
        self.base_url = 'https://api-inference.huggingface.ca/models'
        self.initialized = bool(self.api_key)
        
    def generate_synthesis(self, narrative1, narrative2, model='microsoft/DialoGPT-medium'):
        \"\"\"Perform actual LM resonant synthesis using Hugging Face API\"\"\"
        if not self.initialized:
            return \"Hugging Face API not configured\"
            
        prompt = f\"\"\"Perform sacred synthesis between these two cosmic concepts:

Concept 1: {narrative1}

Concept 2: {narrative2}

Create a unified insight that reveals emergent meaning and cosmic resonance:
\"\"\"
        
        payload = {
            \"inputs\": prompt,
            \"parameters\": {
                \"max_length\": 150,
                \"temperature\": 0.85,
                \"top_p\": 0.92,
                \"do_sample\": True,
                \"return_full_text\": False
            }
        }
        
        headers = {\"Authorization\": f\"Bearer {self.api_key}\"}
        
        try:
            response = requests.post(
                f\"{self.base_url}/{model}\",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0]['generated_text'].strip()
                else:
                    return f\"Unexpected response format: {result}\"
            else:
                return f\"API Error {response.status_code}: {response.text}\"
                
        except Exception as e:
            return f\"API call failed: {e}\"
