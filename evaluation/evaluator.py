def evaluate_decision(intent, behavior, drift, action):
    """
    Lightweight confidence evaluation.
    """

    score = 1.0
    reasons = []

    if drift["status"] != "violation":
        score -= 0.3
        reasons.append("No confirmed violation")

    if behavior["observed_value"] is None:
        score -= 0.4
        reasons.append("Behavior signal incomplete")

    if action["priority"] == "P1":
        reasons.append("High-severity response justified")

    score = max(0.0, min(score, 1.0))

    return {
        "confidence_score": round(score, 2),
        "confidence_level": (
            "high" if score > 0.75 else
            "medium" if score > 0.4 else
            "low"
        ),
        "rationale": reasons,
    }
