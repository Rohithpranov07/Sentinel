import json
from kafka import KafkaConsumer
from pipeline.orchestrator import run_sentinel_pipeline

KAFKA_TOPIC = "sentinel-logs"
BOOTSTRAP = "localhost:9092"
CACHE_FILE = "live_results.jsonl"

def run_live_agent():
    print("🟢 SENTINEL Live Agent Runner started")
    print("📡 Listening to Kafka...")

    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=BOOTSTRAP,
        auto_offset_reset="latest",
        enable_auto_commit=True,
        group_id="sentinel-agent",
        value_deserializer=lambda m: m.decode("utf-8"),
    )

    for msg in consumer:
        raw = msg.value.strip()

        # 🚑 Ignore empty / invalid messages
        if not raw or not raw.startswith("{"):
            continue

        try:
            event = json.loads(raw)
        except json.JSONDecodeError:
            print("⚠️ Skipping malformed Kafka message")
            continue

        print(f"📥 Event received: {event['service']}")

        result = run_sentinel_pipeline(
            services=[event]
        )

        # Persist for Streamlit
        with open(CACHE_FILE, "a") as f:
            f.write(json.dumps(result) + "\n")

        print("✅ Processed and cached")

if __name__ == "__main__":
    run_live_agent()
