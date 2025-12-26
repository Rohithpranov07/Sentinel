import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from pipeline.orchestrator_graph import build_sentinel_graph

st.set_page_config(page_title="Sentinel", layout="wide")

st.title("🛡️ SENTINEL — Semantic Drift Guardian")

st.markdown("Detects drift between **contract intent** and **system behavior**")

document_text = st.text_area(
    "📄 Contract / SLA Text",
    "The service response time shall not exceed 100 milliseconds."
)

logs = st.text_area(
    "📊 Runtime Logs",
    "INFO service-a avg_response_time=150ms"
)

if st.button("🚀 Run Sentinel"):
    graph = build_sentinel_graph()

    initial_state = {
        "document_text": document_text,
        "logs": logs,
        "source_file": "service_a_contract.txt",
        "service": "service_a"
    }

    result = graph.invoke(initial_state)

    st.subheader("🧠 Extracted Intent")
    st.json(result["intent"])

    st.subheader("👁️ Observed Behavior")
    st.json(result["behavior"])

    st.subheader("⚠️ Drift Analysis")
    st.json(result["drift"])

    st.subheader("🎯 Action")
    st.json(result["action"])
