"""
SENTINEL — LangGraph Orchestrator
Day 7–9: Agentic graph with evaluation + explainability
"""

from typing import TypedDict, Dict, Any

from langgraph.graph import StateGraph, END

from agents.intent_extraction import extract_intent
from agents.behavior_monitor import extract_behavior
from agents.drift_detection import detect_drift
from agents.action_orchestrator import orchestrate_action
from evaluation.evaluator import evaluate_decision


# -----------------------------
# 🧠 Shared Graph State
# -----------------------------
class SentinelState(TypedDict):
    document_text: str
    logs: str
    source_file: str
    service: str

    intent: Dict[str, Any]
    behavior: Dict[str, Any]
    drift: Dict[str, Any]
    action: Dict[str, Any]
    evaluation: Dict[str, Any]


# -----------------------------
# 🔗 Graph Nodes
# -----------------------------
def intent_node(state: SentinelState) -> Dict[str, Any]:
    intent = extract_intent(state["document_text"], state["source_file"])
    return {"intent": intent}


def behavior_node(state: SentinelState) -> Dict[str, Any]:
    behavior = extract_behavior(state["logs"], state["service"])
    return {"behavior": behavior}


def drift_node(state: SentinelState) -> Dict[str, Any]:
    drift = detect_drift(state["intent"], state["behavior"])
    return {"drift": drift}


def action_node(state: SentinelState) -> Dict[str, Any]:
    action = orchestrate_action(state["drift"])

    # 🔍 Decision trace for explainability
    action["trace"] = {
        "intent": state["intent"],
        "behavior": state["behavior"],
        "drift": state["drift"],
    }

    return {"action": action}


def evaluation_node(state: SentinelState) -> Dict[str, Any]:
    evaluation = evaluate_decision(
        state["intent"],
        state["behavior"],
        state["drift"],
        state["action"],
    )
    return {"evaluation": evaluation}


# -----------------------------
# 🧩 Build LangGraph
# -----------------------------
def build_sentinel_graph():
    graph = StateGraph(SentinelState)

    graph.add_node("intent", intent_node)
    graph.add_node("behavior", behavior_node)
    graph.add_node("drift", drift_node)
    graph.add_node("action", action_node)
    graph.add_node("evaluation", evaluation_node)

    graph.set_entry_point("intent")

    graph.add_edge("intent", "behavior")
    graph.add_edge("behavior", "drift")
    graph.add_edge("drift", "action")
    graph.add_edge("action", "evaluation")
    graph.add_edge("evaluation", END)

    return graph.compile()
