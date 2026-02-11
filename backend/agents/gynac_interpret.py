# backend/agents/gynac_interpret.py

import json
from backend.model_loader import run_medgemma

def interpret_gynac_report(parsed_report: dict):

    prompt = f"""
You are a clinical decision-support AI for gynecology.

Interpret the following structured report.

STRICT RULES:
- No diagnosis.
- Use cautious language.
- Mention uncertainty.
- Return ONLY valid JSON.

Findings:
{parsed_report["findings"]}

Measurements:
{parsed_report["measurements"]}

Return JSON in this exact format:

{{
  "clinical_interpretation": "...",
  "possible_context": "...",
  "uncertainties": "..."
}}
"""

    response = run_medgemma(prompt)

    return response
