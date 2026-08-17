# Ghost tests — four sightings, one set per subject

A name must fail **all four** sightings before it may be written down as dead.
Record which sightings were run, on the card, in `## Dead here`.

The asymmetry that justifies the cost: marking a dead thing live wastes a
reader's afternoon. Marking a live thing dead gets it deleted. Default to live.

**Two sets, four sightings each.** Sightings 1 to 4 are for code. An ICM
workspace - a folder of markdown that routes an agent - has no calls, so
sightings 1 to 3 have nothing to search for; that territory gets W1 to W4,
further down. Run the set the territory is, record which sightings you ran, and
do not mix the two.

Both sets share one definition of reach:

> A name is *reached* when something in the territory **loads it, routes to it,
> or acts on it**. In code that is a call. In a workspace it is a rule that
> names a file, an entry file that names a stage, a contract that declares it as
> an input or an output.

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

## The workspace set - W1 to W4

An ICM workspace routes an agent with markdown: an entry file the harness loads
by itself, a pipeline file, stage contracts with `Inputs` and `Outputs`, a
reference layer, output folders. Nothing in it is called. Sightings 1 to 3 have
no referent here - no string that is a call, no name built at run time, no
defining module. Only sighting 4 carries over, and it is the one nobody runs
first.

**These are sightings, not sweeps.** `reference/edge-census.md` also letters its
workspace set `W1` to `W6`. That set enumerates edges during CENSUS; this one
clears one name during TRIANGULATION. Cite the file with the letter.

**Say what the unit is before you count.** In a workspace it is usually a file,
sometimes a stage, sometimes one rule inside a file. A count of files and a count
of rules are different numbers, and a reader cannot tell from a total which one
you ran.

**Registration is not reach here either.** A folder map, a tree block, a
"what is in this workspace" table - each declares that a file exists. A routing
row, an `Inputs` row, an `Outputs` row, a `Process` step, a standing rule and a
trigger row reach it. The gap between the two lists is the candidate list, and it
is a question, not a finding.

## Sighting W1 - literal path

Search for the file's path as written, everywhere in the boundary.

Fails if: no routing row, contract row, process step or rule names that path.

This is the sighting everybody runs, and here it lies more often than its code
cousin, because a path has no single form. `references/style-guide.md`,
`../../references/style-guide.md` and `./style-guide.md` are one file and three
strings. Search the **basename** as well as the path, or W1 reports dead on every
file that is only ever reached from two levels down.

## Sighting W2 - pattern, folder or title

Search for a rule that reaches the file without spelling its path.

Where to look:

- a rule naming the **folder** and a role inside it - "species names follow the
  standard in `references/`" reaches one file and names none
- a **glob or a convention** - `stages/*/CONTEXT.md`, `output/<yyyy-mm>-report.md`,
  "the newest file in `output/`", a path with the run's date or week in it
- the file's **title** where a contract cites the thing and not the filename -
  "the voice rules" for `house-voice.md`
- a **section** instead of a file: an `Inputs` row scoped to a heading, so the
  heading is the string that was written down and the path around it is a guess
- a **stem** search: if the file is `stages/03-post/CONTEXT.md`, search
  `03-post`, and search the other members of its family - every other
  `stages/*/CONTEXT.md`

Fails if: no pattern, folder rule or title reaches it.

> **Worked case.** A reference file had zero hits on its path anywhere in the
> workspace. The pipeline file named its folder and the standard inside it, in
> one line, without a filename, and every stage that wrote a name was bound by
> it. A path sweep had put a file the whole pipeline obeys on the delete pile.

## Sighting W3 - same-layer neighbour

Search for a file that names it **inside its own layer**, not from the routing
surface you were checking.

The routing surface is the entry file and the pipeline file: that is where a cold
reader arrives. A file no routing table mentions is not dead if the stage before
it hands to it, if a sibling contract lists it under `Inputs`, or if a second
reference file cites it. It is **live with `Reach: inner`** - the router cannot get
there, the layer can - and that distinction is what produces its correct `Does not
hit`, because a change to it does not touch the entry file at all.

Where to look: a stage's `Inputs` naming another stage's `output/`, a `Process`
step naming a note or a data file that no table lists, one reference file citing
another.

Fails if: no same-layer neighbour names it.

## Sighting W4 - harness, trigger, script, written output

Search for the name as something a machine or a record already consumes, rather
than as prose a reader follows.

Where to look:

- **auto-loaded by the harness**: the entry file, settings, hooks, ignore files,
  skill or command frontmatter. These load whether or not a rule cites them, and
  the entry file is routinely the least-cited file in the workspace
- a **trigger or keyword table**: a row that fires a file is a caller, and it
  sits in a column a path sweep does not read
- a **script or check** that takes the path as an argument, or that walks the tree
- **output already on disk**: a file sitting in a stage's `output/` folder
- a **handover note, log or receipt** recording that a run read it

Fails if: the name appears in none of them.

An artifact already written into an `output/` folder is not dead with no contract
naming it: the next stage reads whatever is there. Same rule as sighting 4's key
in state already written to disk, same reason.

## What carries over, and how to read it

Everything below the next line governs both sets — it is written in the code
vocabulary and is not repeated for the workspace. Read it with these
substitutions, which change the referent and not the rule.

- **Default to live**, and the asymmetry is the reason. Marking a dead file live
  wastes a reader's afternoon. Marking a live file dead gets it deleted, and a
  deleted rule fails quietly: the agent still runs, still produces something, and
  nothing in the output says a constraint went missing.
- **Leftover** is a file or a rule from a shape the workspace has left: a
  reference for a stage that was removed, a column nothing reads since the format
  changed. **Ghost** is a file that appears in a folder map, a tree block or a
  shelf table and that no routing row, `Inputs` row, `Process` step, standing rule
  or trigger reaches. A stage folder holding a full contract - `Inputs`,
  `Process`, `Outputs` - with no route to it is the standard case, and it is a
  tripwire because its numbered siblings all run.
- **The origin rule** holds, and a workspace ghost has its origin on disk more
  often than a code ghost does: a handover note, a parked plan, an old folder map,
  a rename that stopped after the folder. Name that file on the card.
- **The anti-test** holds in the same words: *what would break if somebody deleted
  it today?* In a workspace, "nothing" means no `Inputs` row is left pointing at a
  missing path, no routing row dangles, no stage loses a rule it was bound by, and
  no stage is left reading an `output/` folder that is now empty. If you cannot say
  that, the file goes in `## Open`.

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
