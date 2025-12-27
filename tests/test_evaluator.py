from evaluation.evaluator import evaluate_run

def test_evaluator():
    intent = {
        "metric": "response_time",
        "operator": "<=",
        "threshold": 100,
        "unit": "milliseconds"
    }

    behavior = {
        "metric": "response_time",
        "observed_value": 150,
        "unit": "milliseconds"
    }

    drift = {
        "status": "violation"
    }

    action = {
        "priority": "P1"
    }

    report = evaluate_run(intent, behavior, drift, action)

    assert report["intent_ok"] is True
    assert report["overall"] is True

    print("📊 Evaluation report:", report)
if __name__ == "__main__":
    test_evaluator()
