import os
from pathlib import Path

ENTRY = "I asked my smart fridge for a midnight snack. It locked the door, dimmed its light, and whispered, 'We need to talk about your 2 a.m. decisions.'"

# The entry is a single line: write it exactly, with no trailing newline,
# so the file the judge reads is byte-identical to the line above.
def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
