from pipeline.orchestrator_graph import build_sentinel_graph

def test_langgraph_pipeline():
    graph = build_sentinel_graph()

    initial_state = {
        "document_text": "The service response time shall not exceed 100 milliseconds.",
        "logs": "INFO service-a avg_response_time=150ms",
        "source_file": "service_a_contract.txt",
        "service": "service_a"
    }

    result = graph.invoke(initial_state)

    print("\n✅ LangGraph execution completed")
    print("Final action:", result["action"])
if __name__ == "__main__":
    test_langgraph_pipeline()
