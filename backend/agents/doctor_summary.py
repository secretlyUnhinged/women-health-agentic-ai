# backend/agents/doctor_summary.py

from backend.model_loader import run_medgemma

def generate_doctor_summary(parsed_report, interpretation, risk):

    prompt = f"""
Generate a structured gynecology summary.

Include:
- Key findings
- Interpretation summary
- Risk note
- Suggested follow-up questions

No definitive diagnosis.

Parsed:
{parsed_report}

Interpretation:
{interpretation}

Risk:
{risk}
"""

    return run_medgemma(prompt)
