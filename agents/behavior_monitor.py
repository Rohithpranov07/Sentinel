import re
from typing import Dict


def extract_behavior(log_text: str, source: str) -> Dict:
    """
    Extract actual system behavior from logs.
    For Day 3, this is rule-based (no LLM yet).

    Example log line:
    "avg_response_time=150ms"
    """

    response_time_match = re.search(r"(\d+)\s*ms", log_text)

    if not response_time_match:
        return {
            "error": "No measurable behavior found",
            "source": source,
        }

    return {
        "metric": "response_time",
        "observed_value": int(response_time_match.group(1)),
        "unit": "milliseconds",
        "window": "last_5_minutes",
        "source": source,
    }
