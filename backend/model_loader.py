# backend/model_loader.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "google/medgemma-2b-it"  # change if needed

print("Loading MedGemma...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto"
)

model.eval()

def run_medgemma(prompt, max_tokens=600):
    with torch.no_grad():
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.2,
            do_sample=True
        )

        return tokenizer.decode(outputs[0], skip_special_tokens=True)
