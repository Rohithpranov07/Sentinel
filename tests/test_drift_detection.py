from agents.drift_detection import detect_drift

intent = {
    "metric": "response_time",
    "operator": "<=",
    "threshold": 100,
    "unit": "milliseconds",
}

behavior = {
    "metric": "response_time",
    "observed_value": 150,
    "unit": "milliseconds",
}

def test_detect_drift():
    result = detect_drift(intent, behavior)

    assert result["status"] == "violation"
    assert result["severity"] == "high"

    print("🚨 Drift detected correctly:", result)


if __name__ == "__main__":
    test_detect_drift()
