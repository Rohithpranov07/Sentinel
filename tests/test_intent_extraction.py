from agents.intent_extraction import extract_intent

sample_text = """
The service response time shall not exceed 100 milliseconds.
"""

intent = extract_intent(sample_text, "service_a_contract.txt")
print(intent)
