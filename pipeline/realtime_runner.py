import pathway as pw
from pipeline.pathway_ingestion import contracts_stream, logs_stream

def run_sentinel_realtime(contracts_dir: str, logs_dir: str):
    print("🚀 Starting Sentinel REALTIME runner")

    contracts = contracts_stream(contracts_dir)
    logs = logs_stream(logs_dir)

    joined = contracts.join(
        logs,
        pw.left.service == pw.right.service,
        how=pw.JoinMode.INNER
    )

    # DEBUG ONLY — print raw joined stream
    pw.debug.compute_and_print_update_stream(
        joined.select(
            service=pw.this.service,
            document_text=pw.this.document_text,
            logs=pw.this.logs
        )
    )


if __name__ == "__main__":
    run_sentinel_realtime("./data/contracts", "./data/logs")
