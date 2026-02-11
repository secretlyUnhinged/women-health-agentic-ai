# backend/workflows/report_workflow.py

from backend.agents.parser import parse_report
from backend.agents.gynac_interpret import interpret_gynac_report
from backend.agents.risk_agent import assess_risk
from backend.agents.patient_explain import generate_patient_explanation
from backend.agents.doctor_summary import generate_doctor_summary


def gynac_report_workflow(raw_text):

    parsed = parse_report(raw_text)

    interpretation = interpret_gynac_report(parsed)

    risk = assess_risk(parsed)

    patient = generate_patient_explanation(interpretation, risk)

    doctor = generate_doctor_summary(parsed, interpretation, risk)

    return {
        "parsed_report": parsed,
        "interpretation": interpretation,
        "risk_assessment": risk,
        "patient_explanation": patient,
        "doctor_summary": doctor
    }
