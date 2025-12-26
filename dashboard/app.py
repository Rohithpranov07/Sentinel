import streamlit as st
from pipeline.orchestrator_graph import build_sentinel_graph

st.set_page_config(page_title="SENTINEL", layout="wide")

st.title("🛡️ SENTINEL — Live Semantic Drift Monitor")

graph = build_sentinel_graph()

st.sidebar.header("📄 Input Simulation")

document_text = st.sidebar.text_area(
    "Contract / Spec",
    "The service response time shall not exceed 100 milliseconds."
)

logs = st.sidebar.text_area(
    "Service Logs",
    "INFO service-a avg_response_time=150ms"
)

source_file = st.sidebar.text_input(
    "Source File",
    "service_a_contract.txt"
)

service = st.sidebar.text_input(
    "Service Name",
    "service_a"
)

if st.sidebar.button("🚀 Run Sentinel"):
    with st.spinner("Running agentic pipeline..."):
        result = graph.invoke({
            "document_text": document_text,
            "logs": logs,
            "source_file": source_file,
            "service": service
        })

    st.success("Pipeline executed")

    st.subheader("🎯 Final Action")
    st.json(result["action"])
