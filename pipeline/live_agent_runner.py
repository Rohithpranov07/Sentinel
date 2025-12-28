import time
from pipeline.orchestrator import process_single_service


def live_event_stream():
    """
    Simulated live stream.
    Later replace with Pathway / Kafka / FS / HTTP.
    """
    while True:
        yield {
            "service": "service_a",
            "document_text": "The service response time shall not exceed 100 milliseconds.",
            "logs": "INFO service-a avg_response_time=150ms",
            "source_file": "service_a_contract.txt",
        }
        time.sleep(5)


def run_live_agent_loop():
    print("🟢 SENTINEL Live Agent Runner started")
    print("⏳ Watching for live updates...\n")

    for event in live_event_stream():
        print("📡 New live update detected")

        result = process_single_service(event)

        print("🚨 Drift:", result["drift"])
        print("🎯 Action:", result["action"])
        print("📈 Confidence:", result["evaluation"]["confidence_score"])
        print("-" * 50)


if __name__ == "__main__":
    run_live_agent_loop()
