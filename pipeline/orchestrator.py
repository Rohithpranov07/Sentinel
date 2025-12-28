from agents.intent_extraction import extract_intent
from agents.behavior_monitor import extract_behavior
from agents.drift_detection import detect_drift
from agents.action_orchestrator import orchestrate_action
from agents.global_escalator import evaluate_global_escalation
from evaluation.evaluator import evaluate_decision


def process_single_service(service: dict) -> dict:
    """
    Process one service end-to-end.
    Used by live agent runner.
    """

    intent = extract_intent(service["document_text"], service["source_file"])
    behavior = extract_behavior(service["logs"], service["service"])
    drift = detect_drift(intent, behavior)
    action = orchestrate_action(drift)

    evaluation = evaluate_decision(
        intent=intent,
        behavior=behavior,
        drift=drift,
        action=action,
    )

    return {
        "service": service["service"],
        "intent": intent,
        "behavior": behavior,
        "drift": drift,
        "action": action,
        "evaluation": evaluation,
    }


def run_sentinel_pipeline(services: list[dict]) -> dict:
    """
    Run Sentinel across multiple services
    + apply global escalation logic.
    """

    results = []
    actions = []

    for svc in services:
        result = process_single_service(svc)
        results.append(result)
        actions.append(result["action"])

    escalation = evaluate_global_escalation(actions)

    return {
        "services": results,
        "global_escalation": escalation,
    }
