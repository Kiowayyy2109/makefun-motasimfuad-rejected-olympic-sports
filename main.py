import os

LINE = "Synchronised napping: two athletes, one sofa, judged on who drools first. The 2024 final ended in a draw — everyone was asleep."

LIMIT = 200
if len(LINE) != 127 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 127 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
