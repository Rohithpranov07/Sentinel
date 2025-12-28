import pathway as pw

def contracts_stream(directory: str):
    return pw.io.fs.read(
        directory,
        format="plaintext",
        mode="streaming"
    ).select(
        document_text=pw.this.data,
        service=pw.apply(
            lambda _: "service_a",  # keep simple & deterministic
            pw.this.data
        )
    )


def logs_stream(directory: str):
    return pw.io.fs.read(
        directory,
        format="plaintext",
        mode="streaming"
    ).select(
        logs=pw.this.data,
        service=pw.apply(
            lambda _: "service_a",
            pw.this.data
        )
    )
