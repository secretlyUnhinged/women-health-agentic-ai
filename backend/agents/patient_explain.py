# backend/agents/patient_explain.py

from backend.model_loader import run_medgemma

def generate_patient_explanation(interpretation, risk):

    prompt = f"""
You are a calm women's health assistant.

Explain this in simple language.

Do NOT diagnose.
Encourage doctor consultation.
Avoid fear language.

Interpretation:
{interpretation}

Risk:
{risk}

Add this sentence at the end:
"This tool is for educational purposes and does not replace professional medical consultation."
"""

    return run_medgemma(prompt)
