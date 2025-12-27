# pipeline/orchestrator.py

from agents.intent_extraction import extract_intent
from agents.behavior_monitor import extract_behavior
from agents.drift_detection import detect_drift
from agents.action_orchestrator import orchestrate_action
from agents.global_escalator import evaluate_global_escalation
from evaluation.evaluator import evaluate_confidence


def run_sentinel_pipeline(services: list[dict]) -> dict:
    """
    Run Sentinel across multiple services and apply global escalation logic.
    """

    service_results = []
    service_actions = []

    for svc in services:
        intent = extract_intent(svc["document_text"], svc["source_file"])
        behavior = extract_behavior(svc["logs"], svc["service"])
        drift = detect_drift(intent, behavior)
        action = orchestrate_action(drift)
        evaluation = evaluate_confidence(intent, behavior, drift)

        service_results.append({
            "service": svc["service"],
            "intent": intent,
            "behavior": behavior,
            "drift": drift,
            "action": action,
            "evaluation": evaluation,
        })

        service_actions.append(action)

    # 🌍 GLOBAL ESCALATION STEP (NEW)
    escalation = evaluate_global_escalation(service_actions)

    return {
        "services": service_results,
        "global_escalation": escalation,
    }
