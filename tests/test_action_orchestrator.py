from agents.action_orchestrator import orchestrate_action

def test_action_orchestrator():
    drift = {
        "status": "violation",
        "metric": "response_time",
        "expected": "<= 100 milliseconds",
        "observed": "150 milliseconds",
        "severity": "high",
        "reason": "Observed value violates documented intent"
    }

    action = orchestrate_action(drift)

    assert action["priority"] == "P1"
    assert action["action"] == "alert_team"
    assert "Violation detected" in action["message"]

    print("🎯 Action orchestration works:", action)
if __name__ == "__main__":
    test_action_orchestrator()
