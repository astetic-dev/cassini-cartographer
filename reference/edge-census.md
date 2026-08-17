# Edge census - the sweeps, and the lie each one tells

How to enumerate what moves without reading the bodies. Run the sweeps that
apply, state the count from each, and carry the known false result forward.

**Both directions of error matter.** A first sighting invents edges that are not
there and hides edges that are. Neither is rarer than the other.

## The sweep set is chosen by subject

Two sets. **Sweeps 1 to 7** are for a codebase. **Sweeps W1 to W6** are for a
workspace - a tree of markdown that routes an agent, with an entry file,
contracts, reference material and output folders. Name the set you are running at
the BOUNDARY gate. A territory that is both runs both and says so.

**Sweep 7's verdict is void when the artefacts are the territory.** In a codebase
the non-code residue is almost entirely leftovers, and sweep 7 is right to say
so. In a workspace the documents are the objects: the tree is what gets loaded,
routed to and acted on, so running sweep 7 there returns a map of leftovers and
misses the territory. Read only its last trap - version-control reachability -
which holds on any subject.

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

# W1 to W6 - the workspace sweeps

Same subject as sweeps 1 to 7 - what moves against what - on a tree of markdown
instead of code. One edge is still one ordered pair of nouns plus one mechanism;
the mechanisms here are `routes`, `loads`, `declares-input`, `declares-output`
and `writes`. One pointer repeated in four files is still one edge.

## W1 The declaration sweep

Sweep the entry file and every routing table: the file the harness opens, a
second entry file if one exists, the root contract's task table, a trigger list.
Everywhere the workspace announces that a file, a stage or a keyword exists.

Yields: the **declared surface** - every name the workspace promises an agent it
can get to.

Lies by: **over-counting**, twice. A route is permission to read, not a reading.
And a row whose path is not on disk declares nothing: resolve every path and
report both numbers, declared and resolving. Where two entry files both declare,
sweep them separately and diff - a name in one and not the other is a candidate.

## W2 The routing sweep

Sweep every pointer from one file to another: a path in a routing table, a path
in a contract's Inputs, a relative link, a sentence instructing the agent to read
something. Count **distinct targets** and **total pointers** separately.

Yields: the **reached surface**.

Lies by: **under-counting**, twice. Once when the pointer names a folder or a
pattern (`reference/`, every stage's contract) and a path-literal sweep matches
no file. Once when it is a bare name in prose - *follow the style guide* - which
reaches the file while naming no path.

**Mitigation:** sweep basenames as well as paths, then confirm the pointer.

## W3 The load-order sweep

Sweep what arrives before anybody asks for it: the entry file the harness opens
by itself, anything a rule says to read *always* or *first*, anything every
contract loads. Then sweep separately what is loaded only when a step names it.

Yields: the **standing context** - the edges present in every conversation, and
the ones a reader cannot switch off. Reach is decided here: a noun reached from
the **routing surface** - the entry file or the pipeline file, by a routing row, a
trigger row or a standing rule, or by the harness itself - is `entry`. One reached
only by the stage before it, a `Process` step or another reference file is
`inner`. The harness is the outermost case of `entry`, not the only one.

Lies by: **flattening the two.** An unconditional load and a conditional route
look identical on disk - the difference is in the sentence that names the file,
not in where the file sits. Count them apart, or every reference file in the tree
reads as loaded at all times.

## W4 The standard sweep

Sweep the files that constrain output rather than produce it: style guides,
format contracts, conventions, schemas, templates, checklists, naming rules.

Yields: edges that are **binding** rather than executed, and constraints on what
a later step is permitted to write.

Lies by: **looking inert**, in both directions. A page of rules is not a load, so
a standard nothing names is a candidate and goes to TRIANGULATION. And a standard
that is loaded leaves no mark of its own in the artefact it shaped, so the sweep
can only confirm it from the file that names it, never from the output.

## W5 The handoff sweep

For every stage, sweep **three ends separately** and diff them: its declared
outputs, the declared inputs of every other stage, and what is on disk under each
output folder.

Yields: three sets that each mean something different.

- both ends declared - a live joint
- output declared, no reader - the producing stage's output edge is dead
- input declared, no producer - a stage naming a file nothing writes

Lies by: making a **half-wired chain look live** when you sweep one end only. A
file sitting in an output folder proves a run happened, not that anything reads
it. A contract naming that path proves the joint is declared, not that anything
ever wrote there. Sweep both, and say which end you saw.

## W6 The residue sweep

Sweep what no contract names: notes, plans, a README written for people, drafts,
old runs left in an output folder, files nothing routes to.

Yields: leftovers and the origins of ghosts - **and live objects wearing the same
clothes**, which is what makes this the inverse of sweep 7 rather than a copy.

Lies by: **looking dead.** Here a document can be an object, so absence from the
routing table is one failed sighting and not a verdict. Two cases that recur: a
file reached only from below the routing surface is `inner`, not residue; and a
previous run's output named in a contract's Inputs is reached - record the edge
and its mechanism, and leave the arrangement ungraded.

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

On a workspace, the same discipline with the other set:

```
sweep W1 declared ....... 14 routes: 12 resolve, 2 do not
sweep W2 routing ........ 9 distinct targets, 21 pointers
sweep W3 load order ..... 2 always loaded, 7 loaded on a step
sweep W4 standards ...... 5 files, 4 named by a contract
sweep W5 handoff ........ 3 joints: 2 paired, 1 output-only
sweep W6 residue ........ 11 files no contract names
unreached candidates .... 3  -> TRIANGULATION
```

The gap between sweep 1 and sweep 2 is the candidate list, and so is the gap
between W1 and W2. It is a **question**, not a finding. Everything in it goes to
TRIANGULATION before it goes on a card.
