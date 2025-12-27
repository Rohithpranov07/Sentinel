# agents/global_escalator.py

def evaluate_global_escalation(service_actions: list[dict]) -> dict:
    """
    Decide if a system-wide escalation is required
    based on multiple service-level actions.
    """

    # Count priorities
    p1_count = sum(1 for a in service_actions if a["priority"] == "P1")
    total_violations = sum(
        1 for a in service_actions if a["action"] != "no_action"
    )

    # Escalation rules
    if p1_count >= 2 or total_violations >= 3:
        return {
            "escalation": True,
            "level": "SYSTEM_INCIDENT",
            "reason": (
                f"{p1_count} critical violations across "
                f"{total_violations} services"
            ),
            "recommended_action": "page_oncall_and_leadership",
        }

    return {
        "escalation": False,
        "level": "NONE",
        "reason": "Violations are isolated",
        "recommended_action": "standard_service_alerts",
    }
