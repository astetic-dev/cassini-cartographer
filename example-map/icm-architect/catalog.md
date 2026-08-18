# icm-architect

*Jake Van Clief · MIT*

icm-architect is a skill — a set of instructions a Claude agent picks up when
somebody asks it to turn a way of working into a folder structure that an agent
can actually run. Nothing here executes. It is the method itself, written down:
four documents and eight blank starters to copy.

Ask it to structure something and it goes in one of two directions. Given a
description of work — a process you run every week, a body of knowledge, a
problem — it interviews for the shape already present in how you describe it,
picks one of six standard forms, and scaffolds the smallest folder tree that
carries the work. Given a folder, a repo or a vault that already exists, it
inventories everything first, classifies every file, proposes a migration and
waits for approval before moving anything. Both directions end at the same test:
an agent with no memory must be able to open the root, say where it is, and do
the next piece of work from the files alone.

The idea underneath is that folder structure can carry the orchestration that
would otherwise be code. Numbered folders hold the sequence, nesting holds what
is in scope, plain markdown holds the state, and one agent reading the right
file at the right moment does what a multi-agent framework would do. The
workspace it builds is meant to be read like a library: small routing files as
the catalog, the content on the shelves, one librarian walking to one shelf per
question — and never photocopying the building into a backpack.

Four files carry all of it. `CLAUDE.md` is the door, and it is eighteen lines
long: it says what this is and sends you on. `SKILL.md` is the method — ten
rules every workspace must obey, the two modes, the six forms, and the walk
test. Three reference files sit under it, each opened at a named moment:
`core.md` when a contract is being written or a structural call is contested,
`forms.md` when the form is being chosen, `system-map.md` when the form chosen
is the one for a folder that later agents will edit. The templates folder holds
the starters, because the method's own tenth rule is that new work begins by
copying one, never from a blank page.

<div class="callout">
<span class="label">Two files here are called CLAUDE.md.</span>
The one at the root is the door — the file an agent opens first. The one in
`assets/templates/` is a blank starter that opens `# {Workspace name}`, meant
to be copied into a workspace being built. Opening the wrong one gets you a
form with nothing in it. See `collisions.md`.
</div>

<div class="callout">
<span class="label">Work made with this is not kept here.</span>
The root file sends every finished assignment to `blueprints/`, one folder
each, recording which version of this folder produced it. This territory stays
the method; it does not accumulate the work.
</div>

## What is here

| what | it is | reached from | card |
|---|---|---|---|
| CLAUDE.md (root) | the door: what this is, and where to go next | opened first | [objects/root-claude-md.md](objects/root-claude-md.md) |
| SKILL.md | the method: ten rules, two modes, six forms, the walk test | the door | [objects/skill-md.md](objects/skill-md.md) |
| references/core.md | the canon: principles, hierarchy, naming, token budget | the method, when a contract is written | [objects/references-core-md.md](objects/references-core-md.md) |
| references/forms.md | the six forms in depth, and how to pick one | the method, when the form is chosen | [objects/references-forms-md.md](objects/references-forms-md.md) |
| references/system-map.md | how to audit an existing tree into a walkable map | the method, when that form is chosen | [objects/references-system-map-md.md](objects/references-system-map-md.md) |
| assets/templates/ | eight blank starters, copied into new work | the method, while scaffolding | [objects/templates.md](objects/templates.md) |
| README.md | the landing page: what ICM is, and how to install this | a person opening the repository | [objects/readme-md.md](objects/readme-md.md) |
| LICENSE | MIT, 2026, Jake Van Clief | a person, or a license scanner | [objects/license.md](objects/license.md) |

## If your question is…

| question | open |
|---|---|
| Where do I start reading? | [objects/root-claude-md.md](objects/root-claude-md.md) |
| Which of the six forms fits the work in front of me? | [objects/references-forms-md.md](objects/references-forms-md.md) |
| What rules must a stage I write actually follow? | [objects/references-core-md.md](objects/references-core-md.md) |
| How do I turn an existing repo or vault into a walkable map? | [objects/references-system-map-md.md](objects/references-system-map-md.md) |
| Is `assets/templates/CLAUDE.md` the file an agent opens first? | [objects/templates.md](objects/templates.md) |
| Does the root file send me to the README? | [objects/readme-md.md](objects/readme-md.md) |
| What licence is this under? | [objects/license.md](objects/license.md) |

## Not on the shelf

`.git/` — version control internals. And `blueprints/` itself: the root file
names it as where finished work is kept, but today it holds only this folder,
so there is nothing else there to describe.

<div class="record">

**How this was walked.** 15 files and 792 lines of markdown, on 2026-08-18, at
commit `b20fb45` — except the root `CLAUDE.md`, which is a working copy that has
never been committed. Two files that nothing inside names, `README.md` and
`LICENSE`, were each checked from four directions before anything was said about
them; both are in use. One word is used for two different files and is counted
in `collisions.md`. Everything here is in use: nothing was found that is left
over from an older way of working, and nothing looks finished but is unreachable.

**Three questions, three cards.** *"Where do I start?"* → the root `CLAUDE.md`
card, and no other. *"Which form fits a portfolio of pipelines?"* →
`references-forms-md`, and no other; the Umbrella form is named nowhere else.
*"Can an agent following the routing files reach the README?"* → the `readme-md`
card, and no other — where the answer is no.

</div>
