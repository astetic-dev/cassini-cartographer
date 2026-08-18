# Card types and the card schema

Four types, closed. A noun that fits none of them is a sign the noun is wrong,
not that the set is short.

---

## The four types

| type | what makes it its own type | how you know |
|---|---|---|
| **object** | has identity and state; a thing you can point at and name | you can say "*the* X" |
| **channel** | a named pipe with two ends that must be renamed together | one end can be changed without the compiler noticing |
| **surface** | a boundary where names must match across two languages, processes or machines, and a mismatch fails **silently** | there is a registration table on one side and call sites on the other |
| **store** | persisted state outside the code | its contents outlive the code that wrote them |

They are types rather than tags because each has a different **shape** of two
fields:

- `Lives at` — an object has anchors; a channel has a **pair** of anchors, one
  per end; a store has a path plus whatever fixes its schema.
- `Hits` — a surface's hits are *both sides or neither*; a store's hits are
  *every file already written in the old shape*; a channel's hits are *the other
  end, always*.

Getting the type right is most of getting `Hits` right.

---

## Status and Reach

**Status** answers exactly one question: *does touching this change behaviour
today?*

| status | meaning | how it is said in prose |
|---|---|---|
| `live` | yes | *in use* |
| `leftover` | no, but it did a real job once, and it is honest about being over | *no longer used* |
| `ghost` | no, it never did the job its name claims, and it still looks live | *never wired — it looks finished and nothing calls it* |

The three words are field values, and the field is the machine-readable part of
a card. **They stay in the field and out of the sentences.** A reader meets
*never wired*, not *ghost*; a survey run says *ghost* out loud all day and
writes it down nowhere. Same rule as every other word the instrument uses.

**Reach** is a separate axis, present only when status is `live`. It answers one
question — *can anything outside the territory get here at all?* — so its values
are named after the **outside edge of the subject** being mapped:

| subject | reached from the outside surface | reached only from inside | both |
|---|---|---|---|
| codebase | `ui` — from the interface | `internal` — only from its own side | `both` |
| workspace | `entry` — from the **routing surface** | `inner` — only from below it | `both` |

**One triad per subject, and the same axis under two vocabularies** — `entry` is
to a workspace what `ui` is to a codebase. This is not six values.

A workspace's outside surface is its **routing surface**: the entry file and the
pipeline file, by any means — a routing row, a trigger row, a standing rule — and
the harness, which is the outermost case of it and not the only one. `inner` is
what is reached only from below that line: a stage contract, a `Process` step,
another reference file, a previous run's output.

**`entry` does not mean "the entry file".** A file *reached from* the entry file is
`entry` too; the entry file is `entry` because the harness opens it. The value is
named after the surface, not the file — and it has to be, because a workspace in
which exactly one file is `entry` has an axis that separates nothing.

On a territory that is both, use the triad of the sweep that reached the noun and
say which sweep that was in `Moves by`. Workspace reach is decided at sweep W3 in
`reference/edge-census.md`.

Reach is not a fourth status. It exists because it is what makes `Does not hit`
correct: for a `live · internal` noun the card must say *changing this does not
touch the interface — there is no caller there*, and for a `live · inner` one
*nothing routes here from the entry file*. Neither warning can be stated without
the field.

**Reach describes the noun, not every name inside it.** A noun can be `both`
while one member of it is reachable only internally — that is common and it is
often the most useful thing on the card. Put it in `Moves by` as its own row with
the reach in the direction column (`core → core`), and if it changes what a
reader should expect, say so in `Does not hit` as well. Do not weaken the noun's
own Reach to describe one member; the noun's Reach answers *can anything outside
the territory get here at all*.

Keep the status triad closed. A fourth value invites a fifth, and then the set
is no longer closed and the reader can no longer predict it.

---

## The template

```markdown
# <Noun name>
Type:     object | channel | surface | store
Status:   live | leftover | ghost
Reach:    ui | internal | both          <!-- live only; workspace: entry | inner | both -->
Verified: <YYYY-MM-DD> at <short-sha>   <!-- or "working tree, uncommitted" -->

## Is
One to three plain sentences: what this is in the work as it runs today, what it
does, and what it is there for. Written for someone who has never seen it.
No history. No praise. No quality judgement. None of the method's vocabulary.

## Lives at
- <path:line> - <role, at most 5 words>
2 to 5 anchors. Anchors only.

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
Only edges crossing between two nouns or two sides.
A call inside one noun is not an edge. Sharing a file is not an edge.

## Hits
- <noun / file / stored data> - <why a change here reaches it>

## Does not hit
- <the obvious next noun, which is wrong> - <one sentence: why it is a different thing>

## Dead here
Omit if nothing. Named members of this noun that are leftover or ghost:
- `<name>` - <status> - <anchor> - verified by <sightings>. Tripwire: <what a reader would wrongly build>.

## Open
What this card does not know. "Nothing" is a legal answer and is not a weakness.
```

---

## Hard limits

Every one of these is checkable by a script, which is the point.

- **40 lines**, counted as **non-blank lines** — `(Get-Content card | ? {$_.Trim()}).Count`,
  or `grep -c .` — so section spacing is free and the limit bites on content. A
  card that still needs more is two nouns. On a noun with many edges, `Moves by`
  is the row to spend the budget on and `Is` is the line to shorten; never buy
  space by dropping an anchor.
- **Zero code fences.** `grep -c '```' <card>` must return `0`.
- **One quoted line, at most, per card.** Inline, in backticks, tagged
  `(quoted: the string is the fact)`. Permitted only when an anchor genuinely
  cannot carry the fact — a name assembled at runtime is the standard case,
  because the fact *is* the expression. Everything else is a `file:line`.
- **`Does not hit` names a real neighbour** that appears on the shelf. Not a
  strawman, and not three of them. Naming three is hedging; the card promises
  *the* one a competent reader would guess next.
- **`Verified:` is mandatory.** A card with no stamp cannot be checked for
  staleness, and an uncheckable map gets trusted long after it stops being true.

The reason for the quote budget, printed here so it can be cited during review:
**if a reader can rebuild the implementation from the card, the card has become
the territory.**

---

## The decay rule

`Verified: <date> at <sha>` makes staleness computable rather than felt. If the
last commit touching a card's anchor files is newer than the card's sha, the
card is **stale**, and it says so before it says anything else.

Two consequences worth stating:

- A stale card is not a wrong card. It is a card whose claims have not been
  re-sighted. Say that, do not delete it.
- Re-verifying is cheap precisely because the anchors are already there. That is
  a second reason anchors are mandatory.
