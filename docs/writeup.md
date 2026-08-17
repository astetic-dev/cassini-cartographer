# The 100-word writeup

Per `reference/submission-kit.md`: who it is for / what it does / one design
choice and why. Counted below.

---

Cassini maps a body of work you did not write. Point it at anything someone will
change and it leaves one card per thing that matters. A cold reader opens one
card and stops.

The design choice: a card may never contain a code fence. Run a plain "map this
repo" prompt on our fixture and the map comes back three times the size of the
thing it maps, with source pasted in. Cassini's is half the size, every claim
anchored, every card stamped with its commit.

A map bigger than its subject is not a map.

---

**97 words**, counted mechanically. An earlier draft claimed 98 and was 117 — the
count is now checked with a script, not by eye.

## Why this is the choice worth naming

Three candidates were considered:

1. **The four sightings.** Chosen. It is the most arguable claim in the entry —
   it costs real work, and the payoff is a number a reader can check: 4 → 1.
   It also states the asymmetry that justifies the whole discipline.
2. *"Every card carries the commit it was true at."* Cheap to implement, nobody
   else will have it, and maps rot silently everywhere. Kept as the second
   sentence of the README's opening instead.
3. *"The catalog is written last and read first."* The most quotable, but it
   describes an ordering rather than a defended trade-off.

## The hook line for the comment

> It does not answer the question. It shortens it.

Taken from the refusal in `examples.md`, where Cassini declines to say whether a
subsystem is well built and hands over three anchors instead of thirty files.
