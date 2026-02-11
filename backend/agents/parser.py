# backend/agents/parser.py

import re

def parse_report(raw_text: str) -> dict:

    text = re.sub(r'\s+', ' ', raw_text.strip())

    findings = []
    measurements = []

    sentences = re.split(r'(?<=[.!?]) +', text)

    for sentence in sentences:
        lower = sentence.lower()

        if any(k in lower for k in ["cm", "mm", "ml", "size", "volume", "thickness"]):
            measurements.append(sentence.strip())
        else:
            findings.append(sentence.strip())

    return {
        "cleaned_text": text,
        "findings": findings,
        "measurements": measurements
    }
