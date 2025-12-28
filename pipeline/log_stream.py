import time
import random
import pathway as pw


class LogSchema(pw.Schema):
    service: str
    avg_response_time: int


class LogStream(pw.io.python.ConnectorSubject):
    """
    Artificial live log stream for services.
    Simulates real-time telemetry.
    """

    def run(self):
        services = ["service_a", "service_b"]

        while True:
            for service in services:
                self.next(
                    service=service,
                    avg_response_time=random.randint(80, 200),
                )

            # Commit batch
            self.commit()
            time.sleep(2)  # simulate real-time delay


def stream_logs():
    print("🚀 Starting LIVE log stream (Pathway)...")

    logs = pw.io.python.read(
        LogStream(),
        schema=LogSchema,
        autocommit_duration_ms=1000,
    )

    # Print streaming updates to terminal (DEBUG VIEW)
    pw.debug.compute_and_print_update_stream(logs)

    pw.run()
