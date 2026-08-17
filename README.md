# Cassini — the cartographer

Drop this folder into a Claude project, point it at a folder of real work, and it
hands back a map: a short index, and one card per thing that matters. The next
person — or the next model — reads the index, opens **one** card, and knows enough
to change something without reading everything first.

Every card says where it lives, what a change to it touches, and which nearby
thing looks connected but is not — and carries the day it was checked, so you can
tell when it has gone stale.

## Start here

**Read `identity.md` and `rules.md` first and follow them as your operating
instructions.** They define Cassini, the five phases, and the gate between each;
`reference/` holds the procedures they call for. Without them this is a folder of
documents. Then type:

> **"Cassini, map the work in sample/hearth."** — or `sample/wren`, if what you
> actually want mapped is a folder of markdown rather than a folder of code.

## Two kinds of territory

Cassini surveys a **codebase** and an **ICM workspace** — a tree of markdown that
routes an agent, where the documents *are* the objects. Same method, different
instrument: it names which subject it has before it counts anything, then runs
that subject's sweeps and sightings. A territory that is both gets both.

Running the code method on a workspace is the failure that looks like success. It
comes back with a tidy map of leftovers and misses the territory completely,
because there *is anything calling this* has nothing to search for.

## Try it in 2 minutes

Two fixtures, one per subject. Both work; nothing in either is broken.

| fixture | subject | size | answer key | seeded facts |
|---|---|---|---|---|
| `sample/hearth/` | codebase — a heating-control app | 9 files, 183 non-blank | `sample/expected-map.md` | 29 |
| `sample/wren/` | workspace — a ringing station's weekly run | 12 files, 248 non-blank | `sample/wren-expected-map.md` | 30 |

**Open the key after your run, not before** — it gives away every answer, and
`examples.md` is deliberately worked on a third territory so it cannot be copied
from either.

Watch for one trap in each. Hearth registers nine commands and the panel appears
to call five, so four look dead: **three are alive** — two reached by a name built
at run time, one called from inside. Wren has a stage folder holding a complete
contract, both its input paths resolving on disk, listed in the folder map — and
**nothing routes to it**, while its numbered siblings all run. Each gap is the
reason this exists.

## What you need to install

**To make a map: nothing.** No keys, no runtime, no dependency — this folder *is*
the instructions. `render/` needs nothing either: one HTML file with a
placeholder, filled in and opened in a browser. Only `film/`, an optional
90-second explainer, reaches outside; it is written against
[**Odr**](https://github.com/astetic-dev/odr) (MIT, local, free). Skip it and you
still have the map, which is the point.

## What you get

```
catalog.md        the index. Under 60 lines. Read it first.
objects/*.md      one card per thing. Under 40 lines each. Open ONE.
collisions.md     the words this work uses for more than one thing.
walks.md          questions grouped by what you want to talk about, with answers.
map.html          optional. The same map, to look at rather than read.
```

**Cassini asks where to put it before writing anything.** The default is a
`mappings/<name>/` folder of your own, not inside the work being mapped — a
survey should never need write access to its subject.

## The one rule

Read the index, then open one card. Never load the whole `objects/` folder. If
you find yourself reading all of it, the map has failed and you may as well have
read the territory.

## What this will NOT do

- **Say whether the work is any good.** A file is 7,300 lines; whether that is too
  many is a judgement, and Cassini has not been given what a judgement needs.
- **Say why something broke.** A cause needs logs and a timeline; Cassini works
  from what is standing now.
- **Say what to fix, or what to build next.**
- **Map something nobody will change.** An archive gets a note, not a survey.

It still helps with all of those: it turns "somewhere in thirty files" into three
anchors. Take those to whoever does the judging.

## Two things that are not where you would expect

`sample/` holds a **folder**, not one broken file — a body of work is a folder,
and the input to a map is something that works. And `render/` and `film/` are
views: delete them and nothing is lost; delete a card and both are wrong.
