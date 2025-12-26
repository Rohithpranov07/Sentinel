def detect_drift(intent: dict, behavior: dict) -> dict:
    """
    Compare intent vs observed behavior and detect semantic drift.
    """

    metric_match = intent["metric"] == behavior["metric"]
    unit_match = intent["unit"] == behavior["unit"]

    if not metric_match or not unit_match:
        return {
            "status": "unknown",
            "reason": "Metric or unit mismatch",
        }

    threshold = intent["threshold"]
    observed = behavior["observed_value"]
    operator = intent["operator"]

    violated = False

    if operator == "<=":
        violated = observed > threshold
    elif operator == "<":
        violated = observed >= threshold
    elif operator == ">=":
        violated = observed < threshold
    elif operator == ">":
        violated = observed <= threshold

    if violated:
        return {
            "status": "violation",
            "metric": intent["metric"],
            "expected": f"{operator} {threshold} {intent['unit']}",
            "observed": f"{observed} {intent['unit']}",
            "severity": "high",
            "reason": "Observed value violates documented intent",
        }

    return {
        "status": "compliant",
        "metric": intent["metric"],
        "observed": f"{observed} {intent['unit']}",
        "expected": f"{operator} {threshold} {intent['unit']}",
    }
