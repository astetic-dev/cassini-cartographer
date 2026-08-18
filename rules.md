# Rules

## Always

- **Ask whether the territory is in force before surveying it.** A body of work
  somebody will change gets a map. An archive gets a note saying so.
- **Open the map with what the thing is, in prose.** Two to four paragraphs
  before any number, any table and any filename that the sentence can do
  without: what it is, what it does when it runs, what it is built for, and how
  the parts sit together. Write it for someone who has never opened the folder.
  This is the part of the map that gets read.
- **Say what it is for.** The intent is readable off the territory — what the
  entry file declares, what the structure makes easy, what the parts are shaped
  to receive. Say it plainly. Where an intent is declared and does not happen,
  say both in that order, once: what it is meant to do, then what happens
  instead. See `identity.md`, "Reading the intent".
- **Keep the method out of the deliverable.** Sweeps, sightings, gates, phases,
  triangulation, W-numbers, and the words *ghost* and *leftover* are said during
  the walk and never written on the sheet. Plain equivalents go on the map:
  *nothing here calls this*, *checked from four directions*, *no longer used*.
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
- **Never report your own search.** A sweep that found nothing has found nothing
  to point at. *"No handoffs found — a real zero, not a gap"* is the instrument
  talking about itself; the reader never asked what was looked for. If the
  absence genuinely shapes the territory, describe the shape instead: *"this is
  the method that other work is built from, not a pipeline that runs."*
- **Never describe a working thing by what does not reach it.** *"README is
  live, but outside the routing chain"* leads with a `but` and ends with a
  negative. It is live: say what it does and who reads it, and let where it is
  reached from sit on its card in one clause.
- **Never remark on a naming or layout choice.** A word with two referents gets
  counted and routed, not commented on. The reader wants to know which one they
  are holding, not that reusing the word was a decision.
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

Write `catalog.md` in the order set out under **The catalog** below: the name,
the maker, what this is in prose, the signposts if any survive, the shelf, the
question table, what is not on the shelf, and the survey record last.

> **GATE: ONE-QUESTION TEST PASSED** — put three questions a cold reader would
> actually ask to the catalog. Each must route to **exactly one** card. Route to
> two, or to none, and go back to CARDS. Record the three questions and their
> routes at the bottom of the catalog.

Once this gate closes, render `catalog.md` as `catalog.html`: fill the template
in `reference/output-style.md` with this territory's name, its maker, the
description, the signposts, the shelf, the question table and the survey record
— the catalog's own order, unchanged — and write it beside `catalog.md`. This is the deliverable, not
an extra — the map does not go back as a wall of unstyled markdown.

Then build `map.html`: follow `render/render.md`'s steps — one JSON object from
the finished `catalog.md` and every card, filled into `render/map-template.html`.
This is mechanical, not generative: the JSON is assembled from cards already
written, nothing new is claimed — the description in `meta.is` and
`meta.explainer` is the catalog's opening prose, word for word, not a second
attempt at it. A reader who only gets `catalog.md` and
`catalog.html` back has the index; `map.html` is where the graph itself — the
edges, the `hits`/`doesNotHit` paths, the collisions — is something to walk
through rather than read as a table. Skipping it is how a survey ends with the
index and loses the reason `render/` exists.

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
map.html            the card graph, interactive — see render/render.md
```

**Neither `catalog.html` nor `map.html` is optional.** Both are written every
time CATALOG closes: `catalog.html` is the plain-document rendering of
`catalog.md` itself, in the shared Taurus house style, per
`reference/output-style.md`; `map.html` is the interactive view of the whole
card graph, built from `render/render.md`, needing nothing beyond a browser to
open. The only genuinely optional deliverable is `film/`'s explainer video —
that one reaches outside this folder, against a real external tool, and skipping
it costs nothing the map needs.

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

A reader meets this document first and reads it top to bottom knowing nothing.
The order is fixed:

1. **The name.** The territory's own name, alone, as the first line — `# hearth`.
   Not `Map — hearth`, not the path it happened to be found at, not the word
   *map* at all. The masthead above it already says it is a map and who drew it.
2. **The maker**, if the territory says who that is — one line under the name,
   taken from a LICENSE, a package manifest, a README byline or the commit
   history. If nothing says, leave it out rather than guess.
3. **What this is** — two to four paragraphs of plain prose. No counts, no
   method words, no filenames the sentence can do without. What it is, what it
   does when it runs, what it is built for, how the parts sit together, and —
   where it is readable off the territory — what it is plainly meant to do. This
   is the map for most of the people who open it, and on some days the only part
   of it they read.
4. **Signposts**, only those that survive the test below, at most three. None at
   all is a legal answer, and a common one. **The collision pointer does not
   count against the three**: *"session names four things here and forget names
   three → `collisions.md`"* routes a reader to the right card rather than
   warning them off a wrong one, and it has a file of its own behind it. Three
   road signs and a pointer is a map. Four road signs is a snag list with a
   ceiling.
5. **The shelf**, headed `## What is here` — one row per noun: its name, a few
   words saying what it is, where it is reached from in plain words, and the
   link to its card. The status triad appears only when a noun is **not** in use
   — then say so in that row, in words (*no longer used*, *never wired*). The
   field values stay on the card, where a machine reads them.
6. **If your question is…** — the question table, *under* the shelf. A reader
   sees what is in the territory, then how to ask about it.
7. **What is not on the shelf** — one short paragraph.
8. **The survey record** — last, and the only block on the page that carries
   counts, dates and a commit sha. Files and lines walked, what was checked, the
   date and sha the cards were verified at, and the three questions of the
   one-question test with their routes. Plain sentences, still no method words.

**Budgets.** At most 60 lines of routing content — the shelf, the question table
and what is not on the shelf. The description, the survey record and a staleness
banner do not count against it; the budget exists to keep routing short, not to
make the description compete with a warning for room.

**A staleness banner sits above everything, including the name's own block.** If
the territory moved since the cards were verified, say so — old and new commit,
what changed, which nouns most likely moved.

**The signpost test.** A signpost earns its place only if a reader who does not
know it **builds the wrong thing.** Not *is surprised*, not *would like to
know* — builds the wrong thing. Write it as what is there, with the consequence
in the same breath: *"the queue is written by the collector and read by nothing
else; if you want the totals, read them from the store."*

Three shapes that are never signposts:

- **A null result of your own search.** Nothing was found, so there is nothing
  to point at.
- **A live thing described by what does not reach it.** It is in force: describe
  what it does.
- **A choice you would have made differently.** Not yours to make.

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
