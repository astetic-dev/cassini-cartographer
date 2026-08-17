# Edge census — seven sweeps, and the lie each one tells

How to enumerate what moves without reading the bodies. Run the sweeps that
apply, state the count from each, and carry the known false result forward.

**Both directions of error matter.** A first sighting invents edges that are not
there and hides edges that are. Neither is rarer than the other.

## What counts as one edge

State this before you count anything, because two readers will otherwise report
different totals for the same territory.

> **One edge is one ordered pair of nouns plus one mechanism.**
> `A → B by calling` is one edge whether there are two call sites or forty.
> `A → B by calling` and `A → B by writing` are **two** edges: different
> mechanism. `A → B` and `B → A` are **two** edges: different direction.

Consequences worth holding:

- **Sites are not edges.** Report both — *"97 sites, 69 distinct names"* — but the
  edge count is neither of those; it is the number of noun-pairs-plus-mechanism.
- **A read and a write to the same store are two edges.** They fail differently
  and a change touches them differently.
- **An edge inside one noun is not an edge.** A helper calling another helper in
  the same noun is internal structure.
- Mechanisms in practice: `calls`, `reads`, `writes`, `emits`, `imports`,
  `spawns`, `config`. If you need an eighth, name it on the card.

The `Moves by` table on a card has one row per edge, so the two numbers must
agree: rows in all tables = the edge count in the catalog. If they disagree, the
catalog is wrong.

---

## 1 The registration sweep

Find the table where names are declared to an interface: a handler list, a route
table, an export block, a command registry, a plugin manifest.

Yields: the **declared surface** — everything the other side is permitted to
call.

Lies by: **over-counting.** Registration is permission, not use. A name in the
table with no caller is a candidate, not an edge.

## 2 The call-site sweep

Find every place the other side calls in. Count **distinct names** and **total
sites** separately — they answer different questions.

Yields: the **used surface**.

Lies by: **under-counting**, twice. Once when the name is constructed at runtime
(sighting 2 in `ghost-tests.md`). Once when the call **wraps across lines** and
a single-line pattern cannot see it.

> **Worked case.** A one-line regex over emit calls returned 12 of 13 channels.
> The missing one had its name alone on its own line because the call was
> formatted across several. The channel was entirely live and had a listener.
> Nothing was wrong with the code; the sweep was wrong.

**Mitigation:** run the sweep multiline, or sweep for the name rather than the
call, then confirm the call.

## 3 The pairing sweep

For any named pipe — events, topics, queues, signals — sweep **both ends
separately** and diff them.

Yields: three sets that each mean something different.

| set | meaning |
|---|---|
| both ends present | a live channel |
| sender only | **the sender's output edge is dead** — nothing receives |
| receiver only | a listener for something never sent |

Lies by: making a **half-wired channel look live** if you only sweep one end.

> **Worked case.** A function with many callers, doing real work, writing real
> output to disk — and also announcing itself on a channel that nothing listens
> to. The node is live; that one edge is dead. This is why **edge status is
> independent of node status**.

## 4 The constructed-name sweep

Search for the *shape* of dynamic dispatch rather than for names: string
concatenation into a call, interpolation, lookup tables, reflection.

Yields: the edges sweeps 1–2 structurally cannot see.

Lies by: **silence**. It finds nothing when there is nothing, and nothing when
you searched the wrong shape. Prefer a stem search over the family.

## 5 The state sweep

Find every path the work writes to and reads from: files, databases, caches,
directories outside the boundary.

Yields: edges to a `store` card — and the **only** edges that survive a
rewrite, because data already written outlives the code that wrote it.

Lies by: **invisibility**. State written at runtime does not appear in the
source tree at all. Look for the path-building code, not for the files.

## 6 The config sweep

Sweep manifests, capability lists, permission tables, feature flags, build
files, CI definitions.

Yields: edges that are **declared** rather than called, and constraints that
change what a reader is allowed to do.

Lies by: looking inert. A permission list is not a call, but changing it breaks
things that never mention it.

## 7 The artefact sweep

Sweep the non-code residue: docs, branches, planning files, release notes,
migrations, test fixtures.

Yields: almost entirely **leftovers**, plus the **origins of ghosts**.

Lies by: **looking live**. This is the richest source of false liveness in any
territory. A document is not an object. Two specific traps:

- A named intention — a plan, a TODO, an issue — is not an object until
  something calls it.
- **Version-control reachability is not liveness.** A branch reported as "not
  merged" may be fully shipped if the merge was squashed. A branch reported as
  merged is a leftover. Check what shipped, not what the tool says is reachable.

---

## Recording the census

State every count out loud before writing a single card:

```
sweep 1 registration ... 73 declared
sweep 2 call sites ...... 69 distinct names, 98 sites
sweep 3 pairing ......... 13 channels: 12 paired, 1 sender-only
sweep 4 constructed ..... 1 dispatch site, 2 names
sweep 5 state ........... 6 files, all outside the boundary
sweep 7 artefacts ....... 69 docs: 62 for shipped work
unreferenced candidates . 4  -> TRIANGULATION
```

The gap between sweep 1 and sweep 2 is the candidate list. It is a **question**,
not a finding. Everything in it goes to TRIANGULATION before it goes on a card.
