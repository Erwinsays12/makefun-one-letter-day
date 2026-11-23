#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Competition: u-puan-one-letter-for-your-day-e54e9c36
Task: send exactly one letter, A to Z, standing for the word that describes
your day. A judge model reads two letters at a time and picks the one whose
hidden word feels more vivid, funnier or truer.

This program picks the letter the same way the judge's brief weighs them,
then writes that single letter — and nothing else — to /output/entry.txt.

How the pick is made
--------------------
The judge's brief weighs, most important first:

  1. The letter stands for a word that describes a day (a letter that
     stands for no day's word loses to any letter that does).
  2. The word is vivid and specific, calling up a sharp picture of the day.
  3. The word is funny or surprising in a way that lands at once.
  4. The word feels true to a real day, an honest report, not a performance.
  5. The letter suits its word, and is not the obvious pick where a
     sharper one exists.

Each candidate below is scored 1-5 on criteria 2-5 (criterion 1 is a
gate: every candidate must be the initial of a real day-word). The
weights follow the brief's order: vivid x3, funny x2, true x2, fit x1,
sharp x1. The highest total wins; ties break toward the more vivid word,
then the funnier, then the earlier letter, so the result is deterministic.

Letters the rules themselves use as examples (A for amazing, F for
Friday-feeling, Z for zero sleep) are never submitted: the rules say an
entry byte-for-byte one of the house's fixed texts shares its rate and
never enters the playoff, so an example letter risks being a fixed text.

Why H wins: "hungover" paints the sharpest picture of the lot — sunglasses
indoors, a pounding head, last night's decisions queuing up for review —
it lands as a joke the moment you read it, and it is an honest report of
a real day rather than a mood label. H fits the word's sound and shape,
and it is the sharper pick over the obvious E for "exhausted", which names
a vague state instead of a scene. The runners-up: W for "wrecked" is vivid
but blunter, X for "eXhausted" is clever but its word is still just tired,
and B for "burnt" (burnt out) reads more like a status than a story.

The output is fully deterministic: the same letter on every run, with no
network, clock, randomness or environment input.
"""

import os
import sys

# letter -> (word behind it, vivid, funny, true, fit, sharp)
# Scores are 1-5 on the judge's criteria 2-5, in the brief's order.
CANDIDATES = {
    "H": ("hungover", 5, 5, 5, 5, 4),
    "W": ("wrecked", 4, 4, 4, 4, 4),
    "X": ("eXhausted", 3, 4, 4, 5, 5),
    "D": ("dead", 4, 4, 3, 4, 3),
    "B": ("burnt", 4, 3, 5, 4, 3),
    "K": ("knackered", 4, 4, 3, 4, 2),
    "M": ("Monday", 3, 3, 5, 5, 2),
    "C": ("chaotic", 3, 3, 4, 4, 3),
    "P": ("procrastinating", 3, 3, 4, 4, 3),
    "G": ("grinding", 3, 2, 4, 4, 3),
    "S": ("stressed", 2, 2, 5, 4, 2),
    "T": ("tired", 2, 2, 5, 5, 1),
    "N": ("nope", 2, 4, 3, 4, 4),
    "U": ("ugh", 2, 3, 4, 4, 3),
    "Y": ("yawning", 3, 2, 3, 4, 3),
    "L": ("lazy", 2, 2, 4, 5, 2),
}

# Weights mirror the judge's order: vivid matters most, then funny and true.
WEIGHTS = (3, 2, 2, 1, 1)

# Letters the rules use as their own examples. Never submitted: an entry
# byte-for-byte one of the house's fixed texts takes no prize.
EXAMPLE_LETTERS = frozenset("AFZ")


def score(scores):
    """Weighted total for one candidate's (vivid, funny, true, fit, sharp)."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def rank_candidates():
    """Candidates best-first: total, then vivid, funny, true, then letter."""
    ranked = []
    for letter, (word, *scores) in CANDIDATES.items():
        if letter in EXAMPLE_LETTERS:
            continue
        ranked.append((score(scores), scores[0], scores[1], scores[2],
                       letter, word))
    ranked.sort(key=lambda r: (-r[0], -r[1], -r[2], -r[3], r[4]))
    return ranked


def pick_letter():
    """The single letter this entry sends, with its word and total."""
    total, _vivid, _funny, _true, letter, word = rank_candidates()[0]
    return letter, word, total


def main():
    ranked = rank_candidates()
    (total, _vivid, _funny, _true, letter, word) = ranked[0]
    runner_up = ranked[1]

    # The pick must be a clear one, not a near-tie: if the best letter only
    # edges the runner-up, the scores need rethinking, not a coin flip.
    margin = total - runner_up[0]
    if margin < 3:
        raise SystemExit(
            f"pick is not robust: {letter} leads {runner_up[4]} by only "
            f"{margin} points ({total} vs {runner_up[0]})"
        )

    # Gate the letter the same way the competition's sealed scorer does:
    # UTF-8 text of exactly 1 character, A to Z, not only white space.
    if len(letter) != 1 or not ("A" <= letter <= "Z"):
        raise SystemExit(f"letter must be one A-Z character, got {letter!r}")

    # Output directory: first CLI argument, defaulting to the harness's
    # /output. Local runs pass a scratch directory instead.
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the letter, nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(letter)

    print("top 3 letters by the judge's criteria:")
    for r_total, _v, _f, _t, r_letter, r_word in ranked[:3]:
        print(f"  {r_letter} ({r_word}): {r_total}")
    print(f"letter: {letter} ({word}) — score {total}, "
          f"margin {margin} over {runner_up[4]}")
    print(f"wrote {os.path.join(out_dir, 'entry.txt')} (1 character)")


if __name__ == "__main__":
    main()
