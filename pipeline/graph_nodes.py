from agents.intent_extraction import extract_intent
from agents.behavior_monitor import extract_behavior
from agents.drift_detection import detect_drift
from agents.action_orchestrator import orchestrate_action

def intent_node(state: dict) -> dict:
    print("\n🧠 [LangGraph] Intent node")
    intent = extract_intent(
        state["document_text"],
        state["source_file"]
    )
    state["intent"] = intent
    return state

def behavior_node(state: dict) -> dict:
    print("\n👁️ [LangGraph] Behavior node")
    behavior = extract_behavior(
        state["logs"],
        state["service"]
    )
    state["behavior"] = behavior
    return state

def drift_node(state: dict) -> dict:
    print("\n⚠️ [LangGraph] Drift node")
    drift = detect_drift(
        state["intent"],
        state["behavior"]
    )
    state["drift"] = drift
    return state

def action_node(state: dict) -> dict:
    print("\n🎯 [LangGraph] Action node")
    action = orchestrate_action(state["drift"])
    state["action"] = action
    return state

def debug_node(state: dict) -> dict:
    print("\n🐞 [DEBUG NODE] Final State:")
    for k, v in state.items():
        print(f"{k}: {v}")
    return state
