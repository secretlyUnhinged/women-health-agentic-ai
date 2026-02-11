# backend/agents/risk_agent.py

def assess_risk(parsed_report: dict):

    text = parsed_report["cleaned_text"].lower()

    high_keywords = [
        "malignant",
        "rupture",
        "severe pain",
        "heavy bleeding",
        "large mass"
    ]

    moderate_keywords = [
        "cyst",
        "fibroid",
        "irregular",
        "elevated"
    ]

    red_flags = []

    for word in high_keywords:
        if word in text:
            red_flags.append(word)

    if red_flags:
        return {"risk_level": "high", "red_flags": red_flags}

    for word in moderate_keywords:
        if word in text:
            red_flags.append(word)

    if red_flags:
        return {"risk_level": "moderate", "red_flags": red_flags}

    return {"risk_level": "low", "red_flags": []}
