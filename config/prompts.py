INTENT_EXTRACTION_PROMPT = """
You are an AI system that extracts machine-readable requirements
from software contracts and SLAs.

Extract ALL enforceable rules.

Return STRICT JSON only.
DO NOT add explanations.
DO NOT add markdown.
DO NOT add extra text.

JSON format:
{{
  "metric": "response_time",
  "operator": "<=",
  "threshold": 100,
  "unit": "milliseconds",
  "severity": "high"
}}

Text:
{document_text}
"""
