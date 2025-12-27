"""
SENTINEL — Decision Confidence Evaluator
"""

def evaluate_decision(intent: dict, behavior: dict, drift: dict, action: dict) -> dict:
    score = 0.0
    reasons = []

    # 1. Intent clarity
    if intent.get("metric") and intent.get("threshold"):
        score += 0.3
        reasons.append("Clear measurable intent extracted")

    # 2. Metric alignment
    if intent.get("metric") == behavior.get("metric"):
        score += 0.3
        reasons.append("Observed behavior matches intended metric")

    # 3. Drift severity
    severity = drift.get("severity", "low")
    if severity == "high":
        score += 0.3
        reasons.append("High-severity violation detected")
    elif severity == "medium":
        score += 0.2
        reasons.append("Medium-severity deviation detected")
    else:
        score += 0.1
        reasons.append("Low or no drift")

    score = min(score, 1.0)

    if score >= 0.75:
        level = "high"
    elif score >= 0.45:
        level = "medium"
    else:
        level = "low"

    return {
        "confidence_score": round(score, 2),
        "confidence_level": level,
        "rationale": "; ".join(reasons)
    }
