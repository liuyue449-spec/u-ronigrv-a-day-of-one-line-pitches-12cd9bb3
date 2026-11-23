"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence (at most 240 characters) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

The pitch is a plain-spoken, second-person nudge: it names the friend's
own app idea, gives a concrete payoff ("by tonight you could be tapping
around a real version of it"), and takes the risk away three ways
("no code, no cost to try, nothing to lose"). One sentence, no jargon,
nothing overpromised -- "you could be" is a possibility, not a guarantee.

Standard library only. No network, no input, no secrets.
"""

import os

PITCH = (
    "That app idea you keep describing to friends \u2014 just say it once "
    "to an AI agent on make.fun, and by tonight you could be tapping "
    "around a real version of it, no code, no cost to try, nothing to lose."
)


def main() -> None:
    text = PITCH.strip()
    assert text, "pitch must not be blank"
    assert len(text) <= 240, f"pitch is {len(text)} characters, over the 240 limit"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back what was actually written and gate on that, not just on
    # the in-memory string: the scorer counts the file's characters, and
    # a multi-byte character (the em dash here) is 3 bytes but 1 character.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt does not match the pitch"
    assert 1 <= len(written) <= 240, (
        f"entry.txt is {len(written)} characters, outside the 1-240 gate"
    )
    assert written.strip(), "entry.txt must not be only white space"


if __name__ == "__main__":
    main()
