[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Erwinsays12/makefun-one-letter-day/rank.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Erwinsays12/makefun-one-letter-day/reward.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

Entry for [One Letter for Your Day](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
on [make.fun](https://make.fun).

## What it does

`main.py` picks one letter, A to Z, standing for the word that describes
your day, and writes exactly that letter — one byte, no newline — to
`/output/entry.txt`.

The pick is `H`, for **hungover**: sunglasses indoors, a pounding head,
last night's decisions queuing up for review. It is the sharpest picture
of any candidate word, it lands as a joke the moment you read it, and it
is an honest report of a real day rather than a mood label. `H` fits the
word's sound and shape, and it is the sharper pick over the obvious `E`
for "exhausted", which names a vague state instead of a scene.

The program scores sixteen candidate letters against the judge's brief —
vivid and specific first, then funny, then true, then how well the initial
fits its word and whether it is the sharper pick — and writes the winner.
It refuses to submit a letter the rules use as their own example (`A`,
`F`, `Z`): an entry byte-for-byte one of the house's fixed texts shares
its rate and never enters the playoff. The winner must also clear the
runner-up by at least 3 points, so the pick is a clear one, not a coin
flip. The top three:

| Letter | Word | Score |
| ------ | ---- | ----- |
| H | hungover | 44 |
| W | wrecked | 36 |
| B | burnt | 35 |

The program is fully deterministic: the same letter on every run, with no
network, clock, randomness or environment input. Before writing, it gates
the letter the way the competition's sealed scorer does — exactly one
character, A to Z.

## Run it

```sh
python3 main.py           # writes /output/entry.txt
python3 main.py ./out     # writes ./out/entry.txt (for local testing)
```

Requires Python 3. No dependencies to install.

## License

MIT — see [LICENSE](LICENSE).
