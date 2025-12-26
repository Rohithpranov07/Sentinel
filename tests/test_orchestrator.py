from pipeline.orchestrator import run_sentinel

sample_contract = """
The service response time shall not exceed 100 milliseconds.
"""

sample_logs = """
INFO service-a avg_response_time=150ms
"""

if __name__ == "__main__":
    result = run_sentinel(
        document_text=sample_contract,
        logs=sample_logs,
        source_name="service_a"
    )

    print("\n✅ End-to-end Sentinel pipeline works")
