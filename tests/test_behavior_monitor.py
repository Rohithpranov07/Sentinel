from agents.behavior_monitor import extract_behavior

sample_logs = """
INFO service-a avg_response_time=150ms
INFO service-a requests=1200
"""


def test_extract_behavior():
    behavior = extract_behavior(sample_logs, "service_a_logs")

    assert behavior["metric"] == "response_time"
    assert behavior["observed_value"] == 150
    assert behavior["unit"] == "milliseconds"

    print("✅ Behavior extraction works:", behavior)
if __name__ == "__main__":
    test_extract_behavior()
