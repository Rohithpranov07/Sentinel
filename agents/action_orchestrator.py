def orchestrate_action(drift_result: dict) -> dict:
    """
    Decide what action to take based on drift severity.
    """

    if drift_result["status"] != "violation":
        return {
            "priority": "P3",
            "action": "no_action",
            "message": "System is compliant",
            "recommended_steps": []
        }

    severity = drift_result.get("severity", "low")

    if severity == "high":
        priority = "P1"
        action = "alert_team"
        steps = [
            "Notify service owners immediately",
            "Investigate root cause",
            "Mitigate SLA violation"
        ]
    elif severity == "medium":
        priority = "P2"
        action = "log_and_monitor"
        steps = [
            "Log violation",
            "Monitor trends",
            "Schedule fix"
        ]
    else:
        priority = "P3"
        action = "monitor"
        steps = ["Monitor for changes"]

    message = (
        f"Violation detected: {drift_result['metric']} "
        f"(expected {drift_result['expected']}, "
        f"observed {drift_result['observed']})"
    )

    return {
        "priority": priority,
        "action": action,
        "message": message,
        "recommended_steps": steps
    }
