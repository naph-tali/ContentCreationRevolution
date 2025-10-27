import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class LocalGPT2Service:
    \"\"\"Local GPT-2 for backup synthesis - runs on CPU\"\"\"
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.initialized = False
        self.initialize_model()
    
    def initialize_model(self):
        \"\"\"Load GPT-2 model locally\"\"\"
        try:
            print(' Loading GPT-2 for backup synthesis...')
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')
            
            # Add padding token
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
                
            print(' GPT-2 loaded successfully!')
            self.initialized = True
        except Exception as e:
            print(f' GPT-2 loading failed: {e}')
            self.initialized = False
    
    def generate_synthesis(self, narrative1, narrative2):
        \"\"\"Perform GPT-2 based synthesis\"\"\"
        if not self.initialized:
            return 'GPT-2 model not initialized'
        
        prompt = f\"\"\"Synthesize cosmic insight from these concepts:

\"{narrative1}\"
\"{narrative2}\"

Unified perspective that reveals deeper truth:
\"\"\"
        
        try:
            inputs = self.tokenizer.encode(prompt, return_tensors='pt', max_length=512, truncation=True)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + 80,
                    temperature=0.85,
                    do_sample=True,
                    top_p=0.92,
                    pad_token_id=self.tokenizer.eos_token_id,
                    no_repeat_ngram_size=2,
                    repetition_penalty=1.1
                )
            
            generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Extract just the new synthesis part
            synthesis = generated[len(prompt):].strip()
            return synthesis if synthesis else 'Synthesis produced empty result'
            
        except Exception as e:
            return f'GPT-2 generation failed: {e}'
