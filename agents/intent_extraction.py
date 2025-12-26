import subprocess
import json
from config.prompts import INTENT_EXTRACTION_PROMPT


def extract_intent(document_text: str, source_file: str):
    prompt = INTENT_EXTRACTION_PROMPT.format(
        document_text=document_text
    )

    result = subprocess.run(
        ["ollama", "run", "llama3:8b"],
        input=prompt,
        capture_output=True,
        text=True
    )

    raw_output = result.stdout.strip()

    # 🔐 SAFETY: extract JSON block only
    start = raw_output.find("{")
    end = raw_output.rfind("}") + 1

    if start == -1 or end == -1:
        raise ValueError(
            f"Ollama did not return JSON.\nOutput was:\n{raw_output}"
        )

    json_str = raw_output[start:end]

    intent_json = json.loads(json_str)
    intent_json["source_file"] = source_file

    return intent_json
