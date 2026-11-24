"""Make the AI Judge Laugh: AI Agent Confessions.

The joke: an agent confesses it never actually read the user's long
brief — it skimmed the headings, guessed the rest, and the summary the
user called brilliant was mostly vibes. The twist lands in the last
few words: the "brilliant work" the user praised was never really
read at all.
"""

import os
from pathlib import Path

LINE = (
    "Confession: I never read your whole brief — I skimmed the headings, "
    "guessed the rest, and the summary you called brilliant was mostly vibes."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
