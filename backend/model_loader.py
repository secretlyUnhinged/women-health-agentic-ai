# backend/model_loader.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "google/medgemma-1.5-4b-it"

print("Loading MedGemma 1.5 4B...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    token=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto",
    token=True
)

model.eval()

def run_medgemma(prompt, max_new_tokens=300):  # ✅ using your edited setting
    with torch.no_grad():
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.2,
            do_sample=True
        )

        return tokenizer.decode(outputs[0], skip_special_tokens=True)
