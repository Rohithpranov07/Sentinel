import pathway as pw

def run_day1_live_stream():
    print("\n" + "=" * 60)
    print("🛡️  SENTINEL — DAY 1: LIVE DOCUMENT STREAM")
    print("=" * 60)
    print("📁 Monitoring: ./data/contracts")
    print("✏️  Edit / add files to see output\n")

    # 1️⃣ STREAMING file connector
    docs = pw.io.fs.read(
        path="./data/contracts",
        format="binary",
        mode="streaming",
        with_metadata=True,
    )

    # 2️⃣ Convert binary → text
    parsed = docs.select(
        text=pw.apply(
            lambda b: b.decode("utf-8", errors="ignore"),
            pw.this.data
        )
    )

    # 3️⃣ Create preview column (SAFE)
    preview = parsed.select(
        preview=pw.apply(
            lambda t: t[:120].replace("\n", " "),
            pw.this.text
        )
    )

    # 4️⃣ STREAMING TERMINAL OUTPUT (THIS IS THE KEY)
    pw.debug.compute_and_print_update_stream(preview)

if __name__ == "__main__":
    run_day1_live_stream()
