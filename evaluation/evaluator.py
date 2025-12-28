# evaluation/evaluator.py

def evaluate_decision(intent, behavior, drift, action):
    """
    Produce confidence score + rationale for explainability
    """

    if drift["status"] != "violation":
        return {
            "confidence_score": 0.95,
            "confidence_level": "high",
            "rationale": "System behavior matches documented intent."
        }

    severity = drift.get("severity", "low")

    score_map = {
        "high": 0.92,
        "medium": 0.75,
        "low": 0.6
    }

    return {
        "confidence_score": score_map.get(severity, 0.5),
        "confidence_level": severity,
        "rationale": (
            f"Action '{action['action']}' taken because "
            f"{behavior['observed_value']} {behavior['unit']} "
            f"violates documented constraint {intent['operator']} "
            f"{intent['threshold']} {intent['unit']}."
        )
    }
