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

def run_medgemma(prompt, max_tokens=300):
    with torch.no_grad():
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=False,              # 🔥 Disable sampling
            temperature=None,             # 🔥 Remove temperature
            top_p=None,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

        return tokenizer.decode(outputs[0], skip_special_tokens=True)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
