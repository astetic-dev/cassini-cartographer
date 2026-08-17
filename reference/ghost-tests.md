# Ghost tests — the four sightings

A name must fail **all four** sightings before it may be written down as dead.
Record which sightings were run, on the card, in `## Dead here`.

The asymmetry that justifies the cost: marking a dead thing live wastes a
reader's afternoon. Marking a live thing dead gets it deleted. Default to live.

---

## Sighting 1 — literal

Search for the exact name as a string, everywhere in the boundary.

Fails if: no caller by exact name.

This is the sighting everybody runs, and on its own it is wrong often enough to
be dangerous. The three below exist because of how often sighting 1 lies.

## Sighting 2 — constructed

Search for a caller that **builds** the name at runtime.

Where to look:

- ternaries and conditionals inside the call itself
- template strings, f-strings, string concatenation, `+` on a prefix
- lookup tables, dicts, maps keyed by name
- `getattr`, `getMethod`, reflection, dynamic import
- a **stem** search: if the name is `boiler_on`, search `boiler_`, and search
  the other members of its family

Fails if: no constructed caller.

> **Worked case.** Two commands showed zero literal callers and were both live.
> The call site chose between them with a ternary inside the invocation, so
> neither full name appeared anywhere as a string. A stem search on the family
> found it immediately. Two live commands were one grep away from the delete
> pile.

## Sighting 3 — same-side internal

Search for a caller **inside the defining language or module**, not across the
boundary you were checking.

A name registered on a public interface and never called from the other side is
not dead if its own side calls it. It is **live with `Reach: internal`** — and
that distinction is what produces its correct `Does not hit`, because a change
to it does not touch the interface at all.

Fails if: no internal caller.

## Sighting 4 — data and config

Search for the name as **data** rather than as code.

Where to look:

- persisted state: saved documents, databases, migration files
- config: routing tables, feature flags, manifests, build files
- translation and string tables
- generated code, schemas, API specifications
- docs that are executed — task runners, CI definitions, scripts

Fails if: the name appears in none of them.

A name that is a key in state already written to disk is not dead even with no
code caller: something will read that state.

---

## Verdicts

| outcome | status | what the card says |
|---|---|---|
| passes any sighting | **live** | note which sighting found it, if it was not sighting 1 |
| fails all four, and something once used it | **leftover** | say what it was for and when it stopped |
| fails all four, and nothing ever used it | **ghost** | say what a reader would wrongly assume, and where the wish came from |

**Leftover and ghost are not interchangeable.** A leftover is honest — it did a
job and the job ended. A ghost never did the job its name claims. A ghost is a
tripwire; a leftover is only clutter.

## The origin rule

A ghost without its origin is a lint result, not a map entry. Find where the
wish came from — a plan that was never built, a feature that was cut, a rename
that stopped halfway — and put it on the card. That is what tells the next
reader whether to delete it or finish it.

> **Worked case.** A registered command with zero callers of any kind. Its four
> siblings were all live, so a reader would reasonably assume the whole family
> shipped. On disk, a planning document proposed the feature; only the function
> survived the plan. That document is the difference between "delete this" and
> "somebody wanted this and stopped".

## The anti-test

Before you write `ghost`, answer this in one sentence: **what would break if
somebody deleted it today?**

"Nothing" is the only answer that permits the verdict. If you cannot answer,
the name goes in `## Open`, not in `## Dead here`. An honest gap costs a reader
a search. A wrong verdict costs them a rollback.
