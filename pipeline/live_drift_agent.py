"""
SENTINEL — Day 11.2
LIVE Drift Detection Agent (Pathway Streaming)

Streams logs → detects drift → prints results live
"""

import pathway as pw
import time
import random
from typing import Optional


# -------------------------------------------------------
# 1️⃣ Custom ConnectorSubject (REQUIRED for pw.io.python)
# -------------------------------------------------------
class LiveLogStream(pw.io.python.ConnectorSubject):
    def run(self):
        """
        Simulate live logs every 2 seconds
        """
        while True:
            response_time = random.choice([80, 95, 120, 150])

            self.next(
                service="service_a",
                avg_response_time=response_time,
            )

            time.sleep(2)


# -------------------------------------------------------
# 2️⃣ Schema (MANDATORY)
# -------------------------------------------------------
class LogSchema(pw.Schema):
    service: str
    avg_response_time: int


# -------------------------------------------------------
# 3️⃣ Drift Logic (PURE PYTHON)
# -------------------------------------------------------
def detect_drift(value: int) -> str:
    if value > 100:
        return "VIOLATION"
    return "OK"


# -------------------------------------------------------
# 4️⃣ Live Drift Agent
# -------------------------------------------------------
def run_live_drift_agent():
    print("\n🚀 Starting SENTINEL Live Drift Agent...")
    print("🟢 Streaming logs and detecting drift in real-time...\n")

    # Read live logs
    logs = pw.io.python.read(
        subject=LiveLogStream(),
        schema=LogSchema,
    )

    # Apply drift detection (COLUMN-WISE)
    drift_table = logs.select(
        service=pw.this.service,
        response_time=pw.this.avg_response_time,
        status=pw.apply(detect_drift, pw.this.avg_response_time),
    )

    # THIS is the key for terminal output
    pw.debug.compute_and_print_update_stream(drift_table)


# -------------------------------------------------------
# 5️⃣ Entry Point
# -------------------------------------------------------
if __name__ == "__main__":
    run_live_drift_agent()
