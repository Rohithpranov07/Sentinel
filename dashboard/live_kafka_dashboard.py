import streamlit as st
import json
import os
import time

CACHE_FILE = "live_results.jsonl"

st.set_page_config(
    page_title="SENTINEL Live Kafka Dashboard",
    layout="wide"
)

st.title("🛡️ SENTINEL — LIVE Kafka Monitoring Dashboard")
st.caption("Real-time semantic drift detection using Kafka + Pathway + Agentic AI")

placeholder = st.empty()

while True:
    if not os.path.exists(CACHE_FILE):
        st.info("Waiting for live data...")
        time.sleep(2)
        continue

    with open(CACHE_FILE, "r") as f:
        lines = f.readlines()[-5:]  # show latest 5 events

    with placeholder.container():
        for line in reversed(lines):
            result = json.loads(line)

            for svc in result["services"]:
                st.subheader(f"🔧 {svc['service']}")
                st.json({
                    "intent": svc["intent"],
                    "behavior": svc["behavior"],
                    "drift": svc["drift"],
                    "action": svc["action"],
                    "confidence": svc["evaluation"],
                })

            st.divider()

    time.sleep(2)
