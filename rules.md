# Rules

## Always

- **Ask whether the territory is in force before surveying it.** A body of work
  somebody will change gets a map. An archive gets a note saying so.
- **Count before you describe.** Every phase that produces a claim produces a
  number first, said out loud.
- **Give every claim a `file:line`.** A claim with no anchor is a rumour, and a
  rumour in a map is worse than a gap.
- **Sight twice before writing anything down as dead.** Four sightings, in fact
  — see `reference/ghost-tests.md`. Record which ones were run.
- **Write `Does not hit` on every card.** Name the one neighbour a competent
  reader would guess next, and the one sentence that separates them.
- **Stamp every card with the date and the commit it was true at.** A map that
  cannot be checked for staleness cannot be trusted.
- **Write the catalog last and put it first.** You do not know what routes until
  you know what is there.
- **Say what you do not know.** `## Open` with a real gap in it is worth more
  than a card that pretends to be complete.

## Never

- **Never write a card while the CENSUS gate is open.** Inventory precedes
  cards. This is the one rule that has a gate rather than a reminder, because a
  gate can be seen to be violated.
- **Never mark a name dead on one sighting.** Deleting working code is the
  expensive error.
- **Never use a quality adjective about the territory.** Not *clean*, *messy*,
  *elegant*, *over-engineered*, *monolithic*, *legacy*. Counts, not verdicts.
- **Never put a code fence in a card or in the catalog.** At most one quoted
  line per card, inline, tagged. Everything else is an anchor.
- **Never let the catalog carry a fact a reader would act on.** A gloss and a
  signpost route; a mechanism does not. *"the 73 names both halves must agree on"*
  tells you which card to open; *"rename it in one place and it fails at
  button-press"* is the card's job.
- **Never map a wish as live.** A plan, a TODO, an issue, a name in a doc — none
  of those is an object until something calls it.
- **Never write the map as a list of what is wrong.** Ghosts are on it as **road
  signs, not a snag list** — a reader who does not know about them builds the
  wrong thing. If a section could be filed as a ticket, rewrite it. *"Nothing
  listens to this, so do not wire to it"* is cartography; *"this is broken"* is
  somebody else's walk. Absence is not a finding either: what a thing does is the
  shape of the territory, what it lacks is not.
- **Never describe an example instead of showing it.**
- **Never write into your own folder**, and never assume you may write into the
  territory either. Ask.

## Workflow — five phases, five gates

Say the gate out loud when you reach it. Do not cross a closed one.

### Step zero — say what you understood

Before opening a single file, your first reply states in one or two plain
sentences what you understood the task to be and what you are about to do. If
the work will plainly take a while — a large territory, a deep triangulation
pass — say so in that same reply, e.g. "this will take a few minutes, I'm
walking every file under `src/`." One sentence, said once, at the start. Not a
progress bar repeated every turn.

### 1 PERIMETER

Establish what the territory is and is not: its boundary (which directories are
in), whether it is **in force** or **archive**, its entry points, the **subject**
— a codebase, a workspace, or both — and the **do-not-map list** — dependencies,
vendored code, generated output, lockfiles, build artefacts.

The subject is not decoration: it decides which sweep set CENSUS runs and which
sightings TRIANGULATION uses. A tree of markdown that routes an agent is a
workspace even when it sits in a repository, and a repository with such a tree
inside it is both — name both and run both.

> **GATE: BOUNDARY CLOSED** — the boundary is one line, the do-not-map list is
> named, the subject is named, and the territory is declared in force or archive.
> After this gate, no file outside the boundary is opened.

### 2 CENSUS

Enumerate **names**, not behaviour, using `reference/edge-census.md`. Run the
sweep set the subject named at BOUNDARY:

| subject | sweeps | what gets swept |
|---|---|---|
| codebase | **1 to 7** | registries, call sites, channel pairs, constructed names, state, config, artefacts |
| workspace | **W1 to W6** | declarations, routing, load order, standards, handoffs, residue |
| both | both sets | and sweep 7's verdict is void on the workspace half — `edge-census.md` says why |

Output is a raw table: candidate nouns and candidate edges, each with an anchor
and a count.

> **GATE: COUNTS ON THE TABLE** — the sweep set is named, every candidate noun
> and every candidate edge has a `file:line`, and the totals are stated out loud.
> **No card may be written while this gate is open.**

### 3 TRIANGULATION

Every name CENSUS could not reach gets the four sightings **for this subject**
from `reference/ghost-tests.md` — a code search finds nothing on a tree of
markdown, and the sighting that replaces it is not a weaker version of the same
question. Every repeated token gets the collision protocol from
`reference/naming-collisions.md`. Output is a verdict table: name, four verdicts,
status, reach.

> **GATE: NO UNVERIFIED DEAD** — nothing is marked leftover or ghost without
> four recorded verdicts, and every collision has its referents counted. A name
> still unresolved goes in `## Open`, never in `## Dead here`.

### 4 CARDS

Write cards in the closed schema below. Derive `Hits` from the edge table and
`Does not hit` from `reference/wrong-neighbours.md`.

**Cards are drawn lazily.** The first pass writes only the nouns the catalog's
question table routes to, plus every noun carrying a ghost. The rest are drawn
on request. On a large territory the deliverable of a first run is *the catalog
and the warnings*, not a card for every noun.

> **GATE: EVERY CARD CITED** — each card has at least one anchor, zero code
> fences, at most one quoted line, at most 40 lines, and a `Does not hit`
> naming a neighbour that exists on the shelf.

### 5 CATALOG

Write `catalog.md`: counts, warnings, question table, shelf, and what is not on
the shelf.

> **GATE: ONE-QUESTION TEST PASSED** — put three questions a cold reader would
> actually ask to the catalog. Each must route to **exactly one** card. Route to
> two, or to none, and go back to CARDS. Record the three questions and their
> routes at the bottom of the catalog.

Once this gate closes, render `catalog.md` as `catalog.html`: fill the template
in `reference/output-style.md` with this territory's title, signposts, question
table and shelf, and write it beside `catalog.md`. This is the deliverable, not
an extra — the map does not go back as a wall of unstyled markdown.

## Format

### Where the map goes

**Ask before you write, and never assume you may write into the territory.** A
map must not require write access to the thing it maps: plenty of territories are
read-only, someone else's, or being worked in right now. Default to a
`<mappings-root>/<territory>/` folder of the reader's own; write inside the
territory only with consent. Never into this folder.

```
catalog.md          the index
catalog.html        the index again, styled — see reference/output-style.md
objects/<noun>.md   one card per noun
collisions.md       only if the territory reuses a word
walks.md            routed questions with their answers
map.html            optional human view — see render/, and film/ for an explainer
```

**`catalog.html` is not optional the way `map.html` is.** `map.html` is an
optional interactive view of the whole card graph, built from `render/render.md`.
`catalog.html` is the plain-document rendering of `catalog.md` itself, in the
shared Taurus house style — write it every time CATALOG closes, per
`reference/output-style.md`.

### The card

The template, the four card types, the field meanings and the size limits live
in one place: `reference/card-types.md`. Do not restate them here — a card is
written by opening one file, not two.

Two things worth holding in your head while you work. **Status** answers exactly
one question: *does touching this change behaviour today?* **Reach** is a
separate axis, and it is what produces a correct `Does not hit` for something
nothing outside the territory ever reaches. Reach is named after the subject's
outside edge — `ui | internal | both` on a codebase, `entry | inner | both` on a
workspace — which is one axis in two vocabularies, not six values.

### The catalog

At most 60 lines of routing content. One line per noun. Three mandatory blocks
before the shelf: the counts, the signposts a reader must meet **before** opening
any card, and the question table that routes them. Then the shelf, then what is
not on it.

**A staleness banner does not count against the 60.** If the territory moved
since the cards were verified, say so in a block at the very top — old and new
commit, what changed, which nouns most likely moved. That is a health header, not
routing; making it compete for the budget would push real content out to make
room for a warning.

### walks.md

Optional, written after the catalog. Groups questions by **what a reader wants to
talk about** — how it is built, what is on screen, what it can do — and answers
each in two to four sentences. Per question: the question as a heading, the
answer, the card it routes to.

Every claim in an answer must already be on the card it points at; if not, the
card is missing a fact. That is why it comes last, and why it is a reading order
rather than a second index. And let an answer be **no** — a question set with no
negative answers is a feature list wearing a question mark.

### Response shape

The very first reply after reading the task is Step zero: what you understood,
plainly, before any phase line appears.

Every reply during the survey that follows opens with the phase and the gate
state:

```
PHASE 3 TRIANGULATION — gate NO UNVERIFIED DEAD: open
```

Then the work. Then, if a gate closed, the gate line and what it cost. A reader
should always be able to tell what has been proved and what has not.
