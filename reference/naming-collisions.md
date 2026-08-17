# Naming collisions

A collision is one word with more than one referent in the same territory. It is
the highest-value finding a map can carry, because it misroutes a reader
**before** they open a card — and a warning inside a card arrives too late.

---

## Why this outranks most findings

A reader who does not know a territory navigates by **word**. They search the
word they were given, find a match that works, and stop. If the word has three
referents and they landed on the wrong one, everything downstream is confidently
wrong.

The dangerous shape is specific: **one referent is visible and working, and
another is dead.** The working one is what a search finds first. It vouches for
the dead one.

---

## How to find them

**Same token, different nouns.** Take the verbs and the distinctive nouns from
your census and check whether each appears in more than one family. Most
collisions are a shared verb: `forget`, `close`, `reset`, `sync`, `open`, `clear`.

**Interface labels versus internal names.** A button that says one word and
calls something with a different name is half a collision already. The user's
word and the code's word have drifted.

**String and translation tables.** These are where an interface word is defined
independently of the thing it triggers. A word with an entry there and no
matching object is worth checking in both directions.

**Private helpers sharing a public verb.** A small internal function with the
same verb as a public one, on a different noun. Invisible to an interface sweep,
found by a stem search.

**Types that share a name with an instance.** A word that is both a category and
a specific thing.

---

## Where the warning lives

**One line in the catalog, above the shelf; the table in `collisions.md`.**

A collision is a **routing** failure, so the warning has to reach the reader at
the routing point — a note inside one referent's card helps only the reader who
already guessed right. But the table itself is too wide for a catalog that has a
line budget, so:

- **`collisions.md` exists whenever the territory has at least one collision**,
  and holds the full table for each. One collision is still a file; that keeps
  the rule the same at every size and stops the catalog growing a table.
- **The catalog names every collision in one line each**, with a pointer. The
  compression is in the pointer, never in the omission.

No collisions at all? Then there is no `collisions.md`, and the catalog says
nothing about it.

---

## The recording format

```markdown
## "<word>" - <n> referents

| referent | noun | status | anchor | how to tell it apart |
|---|---|---|---|---|
| <name> | <noun> | ghost | <path:line> | nothing calls it |
| <name> | <noun> | live · ui | <path:line> | the visible button |
| <name> | <noun> | live · internal | <path:line> | private, <n> callers |

**Reader rule:** <one sentence saying which one a person almost certainly means,
and what to ask before opening a card.>
```

The **how to tell it apart** column is the working part of the table. A reader
who can only see a list of three identical words is no better off than before.
Each row must give them something they can check from where they are standing.

---

## The reader rule

Every collision ends with one sentence in the imperative, aimed at somebody who
has just been handed a task containing the ambiguous word.

> **Reader rule:** the button says Forget and means the peer. If somebody asks
> you to "fix Forget", ask which shelf before you open a card.

That sentence is the deliverable. The table is evidence for it.

---

## What is not a collision

- **Two things with similar names that are genuinely the same concept.** Not a
  collision, just verbosity.
- **A generic word used generically** — `get`, `list`, `id`, `name`. Only worth
  recording if a reader could plausibly land on the wrong one while doing real
  work.
- **A word that means different things in different *territories*.** Out of
  scope. The map covers one boundary.

The test: could a competent reader, given a task containing this word, open the
wrong card and not notice? If not, leave it out. A collisions file that lists
every repeated string is noise, and noise at the routing point is worse than
nothing.
