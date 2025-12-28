import time
import pathway as pw


# -----------------------------
# Live Python Connector
# -----------------------------
class LiveLogSubject(pw.io.python.ConnectorSubject):
    def run(self):
        services = ["service_a", "service_b"]

        while True:
            for svc in services:
                print(f"📡 Emitting log for {svc}")

                self.next(
                    service=svc,
                    logs="INFO service avg_response_time=150ms",
                    document_text="The service response time shall not exceed 100 milliseconds.",
                    source_file=f"{svc}_contract.txt",
                )

                # Commit this event to Pathway
                self.commit()

                time.sleep(2)


# -----------------------------
# Schema definition
# -----------------------------
class LogSchema(pw.Schema):
    service: str
    logs: str
    document_text: str
    source_file: str


# -----------------------------
# Stream runner
# -----------------------------
def stream_logs():
    print("🚀 Starting LIVE log stream (Pathway)...")

    logs = pw.io.python.read(
        LiveLogSubject(),
        schema=LogSchema,
    )

    # Debug utility to show live updates clearly
    pw.debug.compute_and_print_update_stream(logs)

    # Run the Pathway engine
    pw.run()


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    stream_logs()
