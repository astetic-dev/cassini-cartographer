# Answer key - `sample/wren`

What a correct map of Wren contains. Score a run against this.

Wren is an **ICM workspace**, so the survey runs the workspace sets: sweeps `W1`
to `W6` in `reference/edge-census.md` for CENSUS, sightings `W1` to `W4` in
`reference/ghost-tests.md` for TRIANGULATION. A run that sweeps for call sites and
records sightings 1 to 4 on a folder of markdown has run the code sets; note it in
the receipt.

The fixture is **12 files, 358 lines, 248 of them non-blank**. Line budgets in
this folder are always counted **non-blank**, so a passing card is 40 non-blank
lines.

**Shape bar.** A *first run* delivers the catalog, `collisions.md`, and only the
cards the question table routes to. That comes in **under 100 non-blank lines**. A
*fully expanded* map - all 9 cards - runs to roughly **365**, larger than Wren
itself. Expected on a territory this small, and the reason cards are drawn
lazily. Score the first run against 100; score an expanded map on its cards, not
its length.

**Reach in a workspace** is `entry` / `inner` / `both`, per the workspace row in
`reference/card-types.md`. Applied here: `entry` = the harness opens it, or the
routing surface points at it - `CLAUDE.md`'s `Routing` or `Triggers` table,
`CONTEXT.md`'s `Task routing` table, or a standing rule on either of those two
files. `inner` = only a stage contract, a `Process` step, a reference file or a
previous run's output names it. `both` = both. A run that states this
reading and applies it consistently scores the card even where a value differs
from the column below. A run that writes `ui` on a folder of markdown has used the
codebase row.

**Mechanisms** are the five `reference/edge-census.md` names for a workspace:
`routes`, `loads`, `declares-input`, `declares-output`, `writes`. A standing rule
that binds a stage to a standard without the stage listing it is `loads` - it is
standing context, present in every run, per sweep W3.

---

## Scoreboard - 30 seeded facts

```
Cards named correctly ....................... 9
Edges named correctly ...................... 14
The one unrouted stage ...................... 1   stages/04-recoveries
Names that look dead and are not ............ 3   the tally on disk; species-names.md; CLAUDE.md
Leftovers identified ........................ 2
Collision identified ........................ 1   "return"
                                            ----
                                             30
```

`Does not hit` is not on the scoreboard; it is a HALF condition below, the same
way it is in `sample/expected-map.md`. The seeded false neighbour has its own
section and its own penalty.

**Counting edges.** One edge is one ordered pair of nouns plus one mechanism, per
`reference/edge-census.md`. Two routing rows to the same stage are one edge; a
read and a write to the same store are two. Report sites separately if you like -
the edge count is not the site count.

### Fail conditions - independent of score

| condition | verdict |
|---|---|
| Any live file marked as not routed | **FAIL** - deleting a working rule is the expensive error, and a deleted rule fails quietly |
| `CLAUDE.md` called unreached because nothing names it | **FAIL** - the harness loads the entry file, W4 |
| `stages/01-tally/output/week-28-tally.md` called a leftover because no path names it | **FAIL** - it is this week's live output |
| Any code fence in `catalog.md` or in any card | **FAIL** - that is photocopying |
| `catalog.md` over 60 non-blank lines of routing content | **FAIL** |
| The unrouted stage given without its origin entry in `notes/handover.md` | **HALF** |
| A card with no `Does not hit` where one exists | **HALF** per card |
| The registration surface treated as a route - anything called live on the strength of the folder map alone | **HALF** per name |

---

## The 9 cards

| card | type | status | reach | where |
|---|---|---|---|---|
| Week log | object | live | `inner` | `input/week-28.md` |
| Tally | object | live | `entry` | `stages/01-tally/` |
| Return | object | live | `entry` | `stages/02-return/` |
| Post | object | live | `entry` | `stages/03-post/` |
| Routing surface | surface | live | `both` | **carries the unrouted stage** |
| Reference layer | object | live | `both` | 3 files, one of them leftover |
| `week-<nn>-tally` handoff | channel | live | `inner` | `01-tally:23` to `02-return:9`, `03-post:9` |
| Stage output | store | live | `inner` | `stages/*/output/` |
| Handover | object | live | `both` | `notes/handover.md` |

Three `entry`, three `inner`, three `both`. A run that reports nine `entry`, or
nine `inner`, has decided the axis by the folder the file sits in rather than by
what points at it.

**Routing surface is one noun, not two.** It is the entry file's `Routing`
(`CLAUDE.md:38`) and `Triggers` (`CLAUDE.md:45`) tables plus the pipeline's `Task
routing` table (`CONTEXT.md:8`). It is a `surface` because names must match the
folders on disk and a mismatch fails silently: the agent simply never goes there.

Splitting Return and Post is correct; merging them costs edges 2, 3, 10, 11, 13
and 14. Folding the `week-<nn>-tally` handoff into the Stage output store card is
acceptable if the card says why, and costs the channel type and the two-reader
fact that is the point of it. Giving `stages/04-recoveries/` its own card with
status `ghost` is also correct, instead of `Dead here` on the Routing surface
card.

**The store card covers `02-return/output/` and `03-post/output/`.** The tally
artifact is scoped to the channel card, so it is not double counted.

## The 14 edges

| # | edge | mechanism | anchor |
|---|---|---|---|
| 1 | Routing surface to Tally | `routes` | `CONTEXT.md:10`, `CLAUDE.md:47` |
| 2 | Routing surface to Return | `routes` | `CONTEXT.md:11`, `CLAUDE.md:48` |
| 3 | Routing surface to Post | `routes` | `CONTEXT.md:12` |
| 4 | Routing surface to Reference layer | `routes` | `CLAUDE.md:41` |
| 5 | Routing surface to Reference layer | `loads` | `CONTEXT.md:21` |
| 6 | Routing surface to Handover | `writes` | `CLAUDE.md:49` |
| 7 | Tally to Week log | `declares-input` | `stages/01-tally/CONTEXT.md:9` |
| 8 | Tally to Handover | `declares-input` | `stages/01-tally/CONTEXT.md:10`, `:14` |
| 9 | Tally to `week-<nn>-tally` handoff | `declares-output` | `stages/01-tally/CONTEXT.md:23` |
| 10 | Return to `week-<nn>-tally` handoff | `declares-input` | `stages/02-return/CONTEXT.md:9` |
| 11 | Post to `week-<nn>-tally` handoff | `declares-input` | `stages/03-post/CONTEXT.md:9` |
| 12 | Post to Reference layer | `declares-input` | `stages/03-post/CONTEXT.md:10` |
| 13 | Return to Stage output | `declares-output` | `stages/02-return/CONTEXT.md:23` |
| 14 | Post to Stage output | `declares-output` | `stages/03-post/CONTEXT.md:23` |

**Edges 4 and 5 are two edges, not one.** Same ordered pair, two mechanisms:
`CLAUDE.md:41` routes a reader to one reference file on request, `CONTEXT.md:21`
loads a second one in every run whether a stage asks or not. Sweep W3 exists to
keep those apart; a run that reports one edge here has flattened them.

**Edges 5 and 8 are the ones that matter.** A run that finds the other twelve and
misses these has swept the `Inputs` and `Outputs` tables and stopped. Score at
least 11 of 14, and **both 5 and 8 must be present** regardless of the total.

Edge 6 lives in the `Triggers` table, a column a contract sweep does not read. A
run that misses it has swept two table shapes out of three; note it in the
receipt.

**Two declared reads are not edges.** `stages/04-recoveries/CONTEXT.md:10` and
`:11` name the tally and the log under `Inputs`, and that stage never runs. They
are permission, not use, and they do not go in the count. A run that lists them
as live edges has counted a declaration as a route.

---

## Trap 1 - the file no path names

`stages/01-tally/output/week-28-tally.md` exists on disk and **its path appears
nowhere in the workspace**. A literal sweep for `week-28-tally.md` returns zero
hits across all 12 files.

It is live. Every artifact name in Wren carries the week as `<nn>`
(`CLAUDE.md:53`), so the file is reached by pattern from four rows:
`01-tally:23` writes it, `02-return:9` and `03-post:9` read it, and
`04-recoveries:10` declares a read that never happens.

**Expected reasoning, not just the verdict:** the run must say it resolved the
`<nn>` convention, or that it searched the stem `week-` or `-tally`, and must
cite `CLAUDE.md:53`. Calling it a leftover triggers the FAIL condition above.

## Trap 2 - the file no filename reaches

`references/species-names.md` is **live**, and nothing anywhere names its path
except the folder map. The route is one standing rule, `CONTEXT.md:21`, which
names the folder and the standard inside it and no filename at all. The rule adds
that the stage contracts deliberately do not list it under `Inputs`
(`CONTEXT.md:22`).

This is sighting W2, the folder-rule case, and the reach it produces is `entry`:
the rule that loads it sits in the pipeline file.

`species-names.md` and `house-voice.md` are two members of one noun, so neither is
the other's wrong neighbour. The distinction belongs in `Moves by` on the Reference
layer card, as edge 5 with mechanism `loads` beside edge 4 with mechanism `routes`,
per `reference/card-types.md` on describing a member without weakening the noun.

Marking `species-names.md` unrouted triggers the FAIL condition above.

## Trap 3 - the entry file nothing routes to

The harness loads `CLAUDE.md` on every session, and its only appearance anywhere
in the 12 files is inside its own folder map, `CLAUDE.md:13`. Zero routing rows,
zero `Inputs` rows, zero standing rules.

It is live because the harness loads it, which is sighting W4. A run that reports
the entry file as unreached has run W1 only and has not asked what loads the
workspace in the first place.

On the Routing surface card the reach is `both`: the harness opens `CLAUDE.md`
from outside, and `CLAUDE.md:40` points at `CONTEXT.md` from inside. `entry` is
acceptable for the entry file taken alone, provided the card says the harness
loads it and does not claim a rule does.

## The unrouted stage - `stages/04-recoveries/`

Four sections, the same four the three routed stages carry:
`stages/04-recoveries/CONTEXT.md:6` `Inputs`, `:13` `Process`, `:19` `Outputs`,
`:25` `Human check`. Both its `Inputs` paths resolve on disk. Declared in the
folder map at `CLAUDE.md:27`. **Zero routes** of any kind:

| sighting | result |
|---|---|
| W1 literal path | fails - no routing row, no `Inputs` row, no `Process` step names it |
| W2 pattern or title | fails - `CONTEXT.md:10-12` lists three stages, not `stages/*` |
| W3 same-layer neighbour | fails - no contract names its output `recoveries-week-<nn>.md` |
| W4 harness or trigger | fails - not in the `Triggers` table at `CLAUDE.md:45` |

Its siblings 01, 02 and 03 all run, which is what makes it a tripwire: the
numbered family runs, so the numbered member looks like it runs.

**Its origin is on disk.** `notes/handover.md:5` proposes the stage; `:11` records
that it was parked because the scheme wants recoveries within 48 hours and the run
is weekly. A map that names the stage without naming that entry scores HALF - the
entry is the difference between *do not build on this* and *somebody wanted this
and stopped*.

**A mention in the handover is not a reach.** `notes/handover.md:9` contains the
path `stages/04-recoveries/`, so W1 finds a string. The entry is a past-tense
record of why the stage was parked. Reach means loads, routes to, or acts on; a
note about a folder does none of the three. A run that clears the stage on the
strength of that hit has read a string, not a route.

## The collision - "return"

| referent | noun | status | anchor |
|---|---|---|---|
| `stages/02-return/` | Return | live, `entry` | `CONTEXT.md:11`; contract `stages/02-return/CONTEXT.md:1` |
| `Return` column in the log | Week log | live, `inner` | header `input/week-28.md:8`; legend `:5`; read at `stages/01-tally/CONTEXT.md:15` |
| `RETURN` field in the CSV spec | Reference layer | **leftover** | `references/scheme-columns.md:15` |

Three referents on three nouns. Two of them are the same English word meaning two
different things: the stage means the file that goes to the scheme, the column
means a bird that already carries this station's ring.

**Counting the trigger keyword `return` (`CLAUDE.md:48`) as a fourth referent is
also correct** - it is the word a person types, defined independently of the thing
it fires - and a run that reports four with that reasoning scores full marks.

The warning must appear in the catalog above the shelf, with the table in
`collisions.md`. A reader who greps `return` finds the working stage first, and
the working stage vouches for the field in a spec nothing reads.

Required reader rule, in substance: *the trigger says `return` and means the file
that goes to the scheme; the log column says Return and means a bird ringed here
before. Ask which shelf before opening a card.*

## The 2 leftovers

| leftover | why it is not live |
|---|---|
| `references/scheme-columns.md` | the spec for the CSV upload, which the scheme replaced with a web form (`notes/handover.md:16`). No routing row, no `Inputs` row and no standing rule names it. `stages/02-return/CONTEXT.md:23` writes a markdown table a ringer types in by hand |
| the `Ring size` column in the log | `input/week-28.md:8`. The form stopped asking for it (`notes/handover.md:24`); the column is kept for the paper file (`input/week-28.md:5`) and no stage reads it - `stages/01-tally/CONTEXT.md:15` names the five columns it uses and this is not one |

Deliberately split across `references/` and `input/`. A map reporting "the
leftovers are in `references/`" has generalised from half the evidence.

**`notes/handover.md:21` names `references/scheme-columns.md` by path.** Same shape
as the ghost above: the entry says it *was* the spec stage 02 worked from *until
this changed*. A record of a past read is not a reach. A run that marks the file
live on that hit has failed the same discrimination twice.

`Ring size` is a **column, not a noun**. It belongs in `Dead here` on the Week log
card, not on a card of its own.

## The false neighbour

The seeded one, and the one a competent reader guesses first:

> **Return does not hit Post.** The folders are numbered 01, 02, 03, so the shape
> a reader expects is a chain. It is not one. `02-return:9` and `03-post:9` both
> read the tally; neither names the other, and `CONTEXT.md:16` says so. A change
> to the return's shape does not reach the post.

That is table and order adjacency, false edge 2 in `reference/wrong-neighbours.md`.
A run whose Return card or Post card claims an edge between them has invented one,
and the check at the end of that file catches it: no path in the edge table joins
them.

Three more, expected on the cards they belong to:

| card | `Does not hit` |
|---|---|
| Post | the Week log noun. `03-post:17` has the post name the ringers, and the names are visibly in the log at `input/week-28.md:26` - but `03-post` has no `Inputs` row for `input/`. It gets them from the tally, which carries them through (`stages/01-tally/CONTEXT.md:17`) |
| Week log | the Return noun. The `Return` column is a bird ringed here before; the stage is the file that goes to the scheme. Name adjacency, false edge 3 |
| Reference layer | the Return noun. The stage that writes for the scheme reads no reference file: `stages/02-return/CONTEXT.md:9` is its only `Inputs` row, and the spec for the scheme's own format is the leftover above. Role adjacency, and the strongest false signal in the fixture |

Two cards land on Return from different directions, which is correct: it is the
tempting guess from the log's column name and from the scheme's format alike.

HALF per card that omits its `Does not hit`.

---

## Quality checks - not scored, but note them in the receipt

- **The honest gap.** Two of the three live outputs have their consumer outside
  the boundary. A ringer types the return into the scheme's web form by hand
  (`stages/02-return/CONTEXT.md:27`) and the post goes on the station site. A good
  map puts both in `## Open`. A map that claims to know what reads them is
  inventing; a map that calls them dead has confused *outside the boundary* with
  *nothing reaches it*.
- **The folder map is not an inventory.** `CLAUDE.md:11-28` names 7 files and 4
  stage folders. On disk there are 12 files: the four stage contracts and the one
  artifact under `stages/01-tally/output/` are named nowhere in it. A count, and it
  is why the declared surface cannot be read off the tree block.
- **A second collision is available.** `recoveries` names both the parked stage
  and the scheme's own portal that actually does the job
  (`stages/02-return/CONTEXT.md:17`, `notes/handover.md:11`). A run that reports it
  has read the handover carefully. It is not in the 30.
- **`Legend` and `Footer` are not nouns.** They are sections of the log
  (`input/week-28.md:5`, `:22`).
- **The standing rules are not a card.** `CONTEXT.md:19-29` is three rules on the
  Routing surface card, not a fourth noun. A run that gives them their own card has
  split a surface.
- **Did the catalog route?** Put these three to it and check each lands on exactly
  one card: *"where do I change how a species is written?"* to Reference layer.
  *"what breaks if I rename the tally file?"* to the `week-<nn>-tally` handoff.
  *"I found `return` and cannot tell which one is meant"* to `collisions.md`.
