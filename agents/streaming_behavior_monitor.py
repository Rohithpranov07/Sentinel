import pathway as pw
import re

def extract_behavior_stream(logs: pw.Table):
    """
    Convert raw log stream into structured behavior metrics.
    """

    def parse_log(text: str):
        match = re.search(r"avg_response_time=(\d+)ms", text)
        if match:
            return int(match.group(1))
        return None

    parsed = logs.select(
        metric=pw.this._metadata.path,
        observed_value=pw.apply(parse_log, pw.this.data),
        unit=pw.lit("milliseconds"),
    )

    return parsed.filter(pw.this.observed_value.is_not_none())
