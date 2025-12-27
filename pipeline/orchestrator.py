# pipeline/orchestrator.py

from agents.intent_extraction import extract_intent
from agents.behavior_monitor import extract_behavior
from agents.drift_detection import detect_drift
from agents.action_orchestrator import orchestrate_action
from evaluation.evaluator import evaluate_decision


def run_sentinel_pipeline(input_data: dict) -> dict:
    """
    Run Sentinel pipeline for ANY service.

    Expected input_data:
    {
        "document_text": str,
        "logs": str,
        "source_file": str,
        "service": str
    }
    """

    # ---- Step 1: Intent Extraction ----
    intent = extract_intent(
        input_data["document_text"],
        input_data["source_file"]
    )

    # ---- Step 2: Behavior Monitoring ----
    behavior = extract_behavior(
        input_data["logs"],
        input_data["service"]
    )

    # ---- Step 3: Drift Detection ----
    drift = detect_drift(intent, behavior)

    # ---- Step 4: Action Orchestration ----
    action = orchestrate_action(drift)

    # ---- Step 5: Confidence / Evaluation Layer ----
    evaluation = evaluate_decision(
        intent=intent,
        behavior=behavior,
        drift=drift,
        action=action
    )

    # ---- Final Structured Output ----
    return {
        "service": input_data["service"],
        "intent": intent,
        "behavior": behavior,
        "drift": drift,
        "action": action,
        "evaluation": evaluation
    }
