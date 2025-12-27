# tests/test_multi_service.py

from pipeline.orchestrator import run_sentinel_pipeline


def test_multi_service_pipeline():
    services = [
        {
            "service": "service_a",
            "document_text": "The service response time shall not exceed 100 milliseconds.",
            "logs": "INFO service-a avg_response_time=150ms",
            "source_file": "service_a_contract.txt"
        },
        {
            "service": "service_b",
            "document_text": "The service response time shall not exceed 300 milliseconds.",
            "logs": "INFO service-b avg_response_time=120ms",
            "source_file": "service_b_contract.txt"
        }
    ]

    for payload in services:
        result = run_sentinel_pipeline(payload)

        assert "intent" in result
        assert "behavior" in result
        assert "drift" in result
        assert "action" in result
        assert "evaluation" in result

        print(f"\n✅ Sentinel OK for {payload['service']}")
        print("Action:", result["action"])
        print("Confidence:", result["evaluation"]["confidence_score"])


if __name__ == "__main__":
    test_multi_service_pipeline()
