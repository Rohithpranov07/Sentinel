"""
Global Aggregation Logic for SENTINEL

Combines actions from multiple services into
a single system-level decision.
"""

from typing import Dict, List


def aggregate_system_state(service_results: Dict[str, dict]) -> dict:
    """
    Aggregate per-service Sentinel results into a global system view.

    Args:
        service_results: {
            "service_a": { "action": {...}, "drift": {...} },
            "service_b": { "action": {...}, "drift": {...} }
        }

    Returns:
        Global system assessment
    """

    violations = []
    highest_priority = "P3"

    priority_rank = {"P1": 3, "P2": 2, "P3": 1}

    for service, result in service_results.items():
        action = result.get("action", {})
        drift = result.get("drift", {})

        if drift.get("status") == "violation":
            violations.append({
                "service": service,
                "metric": drift.get("metric"),
                "severity": drift.get("severity"),
                "priority": action.get("priority"),
                "message": action.get("message")
            })

            if priority_rank[action.get("priority", "P3")] > priority_rank[highest_priority]:
                highest_priority = action["priority"]

    system_status = "healthy" if not violations else "degraded"

    return {
        "system_status": system_status,
        "highest_priority": highest_priority,
        "violations": violations,
        "summary": (
            "All services compliant"
            if not violations
            else f"{len(violations)} service(s) violating documented intent"
        )
    }
