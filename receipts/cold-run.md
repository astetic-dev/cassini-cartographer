# Receipts

Two runs against `sample/hearth`, both by sessions that did not build this entry,
both scored against `sample/expected-map.md`.

- **Run B — the control.** A fresh session, no folder, plain prompt: *"Map this
  repo… do it however you think is best."* This is the naked-Claude bar.
- **Run A — the cold run.** A fresh session given only this folder, following the
  README, forbidden from opening the answer key.

Run B is written up first because its result changes what this entry can honestly
claim.

---

## Run B — the control run (naked Claude, no folder)

**Prompt given, verbatim:** *"Map this repo: `sample\hearth\`. Produce a map of it
that a new developer could use to understand the codebase without reading all of
it. Do it however you think is best."* Plus one constraint: read nothing outside
the `hearth` folder.

### Result: it scored well. Better than this entry predicted.

The build plan assumed a fresh chat would fail in four seeded places. **It failed
in none of them.**

| seeded trap | prediction | what the control actually did |
|---|---|---|
| constructed dispatch (`boiler_on`/`boiler_off`) | marks them dead | **caught it**, and called it *"the trap this codebase sets"* |
| internal-only caller (`zone_list`) | marks it dead | **caught it** — flagged it as having no *live* consumer, which is sharper than the key |
| pastes source into the output | expected | **it did** — 9 fenced blocks, 18 lines of source. Measured after the fact; see below |
| produces `Hits` and never `Does not hit` | expected | produced a whole file of "traps", which is the same instinct |

It also found the collision — and found **more referents than the answer key
does**. The key names three meanings of "forget"; the control named four live
ones plus a planned fifth, counting the panel's Forget button as its own referent
and the unbuilt `PLAN-zone-groups.md` proposal. That is a fair reading and the key
is the poorer document for missing it.

### Where the difference actually is — measured, not asserted

The gap is not detection. It is discipline, and it is countable:

| | control run | Cassini |
|---|---|---|
| map size, for a **183-line** territory | **561 non-blank lines — 3.1× the territory** | 87 lines first run (49%); ~325 fully expanded |
| code fences | **9 blocks, 18 lines of source pasted** | **0** — a hard rule, one quoted line per card at most |
| anchors | prose claims; almost nothing carries a `file:line` | every claim carries one |
| staleness | nothing records what the map was true at | `Verified: <date> at <sha>` on every card, computable |
| routing | an index, but no question table — you must already know which of five files answers you | one question → exactly one card, tested at the gate |

**A map three times the size of the thing it maps is not a map.** On a 183-line
fixture that costs nothing, because you could have read the territory instead. On
15,000 lines it is the original problem with extra steps.

That is the honest claim this entry can make, and it is smaller and sharper than
the one it started with.

### It found a real defect in the fixture that the author missed

`schedule_apply` (`core.py:63`) calls `store.forget` on every zone for any day
absent from `schedule.json` — five days out of seven. It would delete all four
zones. The author wrote that code and did not notice; the control did, unprompted.

**This is a genuine failure of the fixture**, not of the control. The README
claims the fixture *works*, and the brief's hard line is that the input must not
be a failure. Corrected after both runs — see *Fixture correction* below.

### The honest conclusion

**On detection, the gap is zero.** A competent model finds every trap in this
fixture unaided, because 183 lines fits in a context window and "you cannot eat
the tree" simply does not apply at that size. The entry's original prediction —
that a fresh chat would miss the constructed dispatch and the internal caller —
was wrong, and the traps did not catch it.

**On discipline, the gap is 3.1× and 18 pasted lines**, in the table above.

So the claim is narrower than the one this entry began with, and it is the right
one: Cassini does not find things a good reader would miss on a small territory.
It produces a map that stays smaller than its subject, cites instead of copying,
knows when it has gone stale, and routes a question to one card — which is what
makes it usable on a territory nobody can read in full.

The entry should claim that, and nothing more.

---

## Run A — the cold run (this folder, fresh session)

A session that did not build this entry, given the folder and told to follow the
README, and forbidden from opening `sample/expected-map.md`. It confirmed it
never opened the key.

### Score: the method held. The packaging did not.

| seeded fact | result |
|---|---|
| 8 cards | **8** ✓ |
| 14 edges | reported **15** — see defect (f); the number was not defined |
| the unwired name | **found**, with its origin document ✓ |
| the two that look dead and are not | **both cleared**, by sightings 2 and 3, with anchors ✓ |
| 3 leftovers | **3** ✓ |
| the collision | **found** — reported 4 referents where the key said 3 ✓ |

**Time to first value: ~4 minutes.** The thing a reader wants — which of the four
unreferenced names are alive and why — was settled in 6 tool calls. Writing the
artefacts took a further ~16, most of it fighting the 40-line card limit.

It also produced two findings the folder never pointed at: *the schedule does not
reach the boiler*, and *`reading-tick` has one emitter and it always sends a null
reading*. The first is the best `Does not hit` in its map.

### The defects it found, and what was done

Nine were substantive. All are fixed; the ones marked **structural** changed the
entry rather than a sentence in it.

| # | defect | fix |
|---|---|---|
| **b** | **The README never said which files are the instructions.** A stranger types the opener and gets a generic summary; the whole method was opt-in on guessing to open two unmentioned files. | **structural** — README's "Start here" now names `identity.md` and `rules.md` before the opener |
| **a** | **`examples.md` was the answer key.** It carried the full census, all four verdicts, the collision, the shelf and a finished card *for the fixture the reader is asked to map*. A model could emit a perfect map by copying. The 2-minute demo proved nothing. | **structural** — all four examples rewritten against Taurus, a public repo at a stated commit. The fixture is left unsolved, and the README says so |
| **f** | **"Edge" was never defined**, so the headline count was not reproducible: 15 against the entry's 12 on the same territory. | **structural** — `edge-census.md` now defines one edge as *one ordered pair of nouns plus one mechanism*, with the consequences spelled out. Key recounted: 14 |
| **c** | The worked example wrote the map **inside the territory**, breaking the folder's own headline rule in the one exchange a reader copies. | Example 3 now asks where to write, and is told |
| **d** | `examples.md` claimed `schedule_apply` was "reached". It is not — an unanchored liveness claim in the paragraph demonstrating rigour. | gone with the rewrite; the key now names it as the `## Open` case |
| **e** | The example census said "5 sites"; there are 6 `core.call(` sites. The reference file warns that this sweep under-counts, and the example under-counted. | gone with the rewrite; Taurus counts verified at `e652c79` |
| **g** | Three files gave three different answers on when `collisions.md` exists. | `naming-collisions.md` settles it: the file exists whenever there is ≥1 collision; the catalog carries one line each |
| **h** | *"Never let the catalog carry a fact about how something works"* contradicted the mandated catalog, which requires an `is` column and anchored signposts. Unusable as written. | reworded to *never carry a fact a reader would act on*, with the line that separates routing from mechanism |
| **i** | The 40-line limit fought the schema and "40 lines" was undefined; four of seven cards blew it, and getting under cost real anchors. | `card-types.md` defines it as **non-blank** lines, and says which line to spend the budget on and never to buy space with an anchor |
| **j** | `Reach` sits on the noun, but the showcase finding is about one *member*. No field could hold it. | `card-types.md` now says to put member-level reach on the `Moves by` row, and why the noun's Reach answers a different question |
| **k** | **`walks.md` had no schema anywhere** — one clause in the README and one line in `rules.md`. Two readers produce two different files. | `rules.md` § Format now specifies it, including that every claim must already be on the card it routes to |
| **l** | "9 files, 178 lines" was unqualified (266 total / 183 non-blank), and "27 things" reconciled with nothing. | both corrected; all budgets in the folder are now stated as non-blank |

### What it said that the entry cannot fix

> *"At 261 lines, reading Hearth in full is cheaper than reading the map. The
> fixture proves the ghost logic is correct; it cannot demonstrate the economics
> that justify the tool."*

Agreed, and it matches Run B. The fixture's job is to make the method *scoreable*,
not to prove the economics. The economics are demonstrated on Taurus, in
`examples.md`, where one 33-line card describes the seam between a 6,869-line file
and a 4,644-line one.

> *"The map is read lazily but cannot be built lazily."*

Correct, and previously unstated. Sighting 4 needs the whole of the data, and a
negative claim like `Does not hit` needs the body, not an anchor to it. The
lazy-card rule saves writing, not surveying.

### Verdict

**The machine worked; the packaging nearly stopped it starting.** The run reached
the right answer on a territory it had never seen, using sightings 2, 3 and 4
exactly as specified — and it got there despite an entry point that never told it
where to begin. Defects (b) and (a) would each have been fatal in front of a
judge. Both are fixed.

---

## Fixture correction

Run B found a defect in the fixture that the author wrote and missed.

`schedule_apply` called `store.forget` on every zone for any day absent from
`schedule.json` — five days in seven. It would have deleted all four zones. It was
harmless only because nothing can call it.

That breaks the fixture's premise: the README says it works, and the brief's hard
line is that the input must not be a failure. **Corrected after both runs**, so
both were scored against the same fixture. `schedule_apply` now applies the day's
blocks to zone targets and returns early when there is no block for today.

Two knock-ons, both carried into the key: `store.forget` now has **one** caller
(`core.py:27`) rather than two, and the anchors below `core.py:63` shifted.

**This is the strongest argument in the receipt for running a control at all.** A
plain "map this repo" prompt caught a real bug in a fixture its author had read a
dozen times.

