"""One-line review of the most boring everyday object: a rubber band.

Decision record (weighed against the judge's criteria, most important first:
boring everyday object -> real, recognisable detail -> true -> fast landing,
last words sharpen it):

Candidate A — rubber band (CHOSEN): "One star. It held my papers together
for three years, then snapped the morning of my job interview." The object
is as boring and everyday as it gets, and the observation is literally how
an old rubber band behaves: it holds for years, then snaps without warning
exactly when it matters. The turn lands in the last words — the snap is
the punchline, and the job interview gives it stakes. The dullness itself
is the joke: three years of loyal service, one catastrophic morning.

Candidate B — doorstop: "One star. It has one job, does it perfectly, and
has never once been thanked. Honestly, same." Loses: the laugh sits in
"honestly, same", a gag bolted on from outside the object, not in any
detail of how a doorstop behaves. It would work for any thankless object.

Candidate C — tea towel: "One star. Four years on the hook, dried one dish,
and still acts like it runs the kitchen." Strong reserve: the hook detail is
true and recognisable. Loses to A because "acts like it runs the kitchen"
is anthropomorphism doing the work, and the punchline needs a beat of
thought; A's snap lands on the first read.

Candidate D — sponge: "One star. It absorbs everything except
responsibility. Smells like a pond now." Loses: "absorbs everything except
responsibility" is a wordplay gag that would fit any sponge-shaped object,
and the pond smell, while true, is a second joke competing with the first
instead of sharpening it.

Candidate E — paperclip: "One star. It has held the same three pages
together since 2019 and expects a promotion." Loses: same mechanism as A
(loyal holder, long service) but weaker — a paperclip does not betray you,
so there is no turn, just a flat complaint, and "expects a promotion" is
the same bolted-on gag as B.

Pass 1 (revision to the winner): the first draft ended "...then snapped the
day I actually needed it." I replaced the ending with "the morning of my
job interview" because "the day I needed it" is vague and trails off; the
concrete morning sharpens the last words and gives the snap real stakes.

Pass 2 (revision to the winner): I tried "It held my life together for
three years" instead of "my papers together", then reverted it. The
metaphor reads punchier, but the judge weighs truth third and the literal
version — a rubber band holding papers — is the true observation; the
metaphor weakens the recognition the laugh depends on.
"""

import os

MAX_CHARS = 200

LINE = "One star. It held my papers together for three years, then snapped the morning of my job interview."


def _is_single_line(text):
    """True when the entry contains no newline (one-line gate rule)."""
    return "\n" not in text


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    # Pass 3 revision: single-line check split out into _is_single_line
    # so the gate reads as separate, reviewable rules; behaviour unchanged.
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not _is_single_line(text):
        raise ValueError("entry must be a single line")
    return True


def entry_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    return os.path.join(out, "entry.txt")


def main():
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
