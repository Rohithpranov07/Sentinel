from langgraph.graph import StateGraph
from pipeline.graph_nodes import (
    intent_node,
    behavior_node,
    drift_node,
    action_node,
    debug_node,
)

def build_sentinel_graph():
    graph = StateGraph(dict)

    graph.add_node("intent", intent_node)
    graph.add_node("behavior", behavior_node)
    graph.add_node("drift", drift_node)
    graph.add_node("action", action_node)
    graph.add_node("debug", debug_node)

    graph.set_entry_point("intent")

    graph.add_edge("intent", "behavior")
    graph.add_edge("behavior", "drift")
    graph.add_edge("drift", "action")
    graph.add_edge("action", "debug")

    return graph.compile()
