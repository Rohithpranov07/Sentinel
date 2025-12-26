from typing import TypedDict, Optional, Dict, Any


class SentinelState(TypedDict):
    document_text: str
    source_file: str

    logs: str

    intent: Optional[Dict[str, Any]]
    behavior: Optional[Dict[str, Any]]
    drift: Optional[Dict[str, Any]]
    action: Optional[Dict[str, Any]]
