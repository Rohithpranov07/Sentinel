import pathway as pw


class KafkaLogSchema(pw.Schema):
    service: str
    logs: str
    document_text: str
    source_file: str


def stream_logs_from_kafka():
    print("🚀 Connecting to Kafka (sentinel-logs topic)...")

    logs = pw.io.kafka.read(
        topic="sentinel-logs",
        bootstrap_servers="localhost:9092",
        schema=KafkaLogSchema,
        format="json",
    )

    pw.debug.compute_and_print_update_stream(logs)
    pw.run()
