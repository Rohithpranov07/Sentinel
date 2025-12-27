"""
SENTINEL Orchestrator
Day 6: End-to-end agent pipeline
"""

from agents.intent_extraction import extract_intent
from agents.behavior_monitor import extract_behavior
from agents.drift_detection import detect_drift
from agents.action_orchestrator import orchestrate_action


def run_sentinel(document_text: str, logs: str, source_name: str):
    """
    Full agentic pipeline:
    Document → Intent → Behavior → Drift → Action
    """

    print("\n🧠 Extracting intent from document...")
    intent = extract_intent(document_text, source_name)
    print("Intent:", intent)

    print("\n👁️ Monitoring behavior from logs...")
    behavior = extract_behavior(logs, source_name)
    print("Behavior:", behavior)

    print("\n⚠️ Detecting drift...")
    drift = detect_drift(intent, behavior)
    print("Drift:", drift)
    action = orchestrate_action(drift)  

    print("\n🎯 Orchestrating action...")
    action = orchestrate_action(drift)
    action["trace"] = {
        "intent": intent,
        "behavior": behavior,
        "drift": drift
    }
    print("Action:", action)

    return {
        "intent": intent,
        "behavior": behavior,
        "drift": drift,
        "action": action,
    }
