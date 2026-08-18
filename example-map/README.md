# Two finished maps

Neither of these is a fixture and neither is an answer key. They are real
deliverables, copied in whole, so you can see what comes back before you run
anything. One of each subject: a workspace, and a codebase.

**GitHub shows HTML as source rather than rendering it**, so every row below has
a second link that hands the file to a preview service. Clone the repo and
double-click any of them and you get the same page offline — the maps load
nothing from the network, which is the whole point of them.

## taurus — a codebase

A desktop application that runs several Claude Code agents as terminal tabs in
one window, 15,897 lines of JavaScript and Rust, surveyed at commit `e652c79`.
By Arjen Stet, MIT, [astetic-dev/taurus](https://github.com/astetic-dev/taurus).

| open | what it is |
|---|---|
| [`taurus/catalog.html`](taurus/catalog.html) · [**in a browser**](https://htmlpreview.github.io/?https://github.com/astetic-dev/cassini-cartographer/blob/main/example-map/taurus/catalog.html) | the map as a document |
| [`taurus/map/map.html`](taurus/map/map.html) · [**in a browser**](https://htmlpreview.github.io/?https://github.com/astetic-dev/cassini-cartographer/blob/main/example-map/taurus/map/map.html) | the same map as a graph you can walk |

Sixteen things are on its shelf and eight have cards — on a territory this size
the first walk delivers the index, the warnings and a card for everything the
questions route to. It is the better of the two to read for the warnings: a
command that is registered next to four working siblings and called by nothing,
two commands called by a name assembled while the program runs, a trail written
to disk and announced on a channel nobody listens to, and two words that name
seven different things between them.

## icm-architect — a workspace

A Claude skill that designs a body of work into an ICM workspace: 15 files, 792
lines of markdown, surveyed at commit `b20fb45`. By Jake Van Clief, MIT,
[RinDig/icm-architect](https://github.com/RinDig/icm-architect).

| open | what it is |
|---|---|
| [`icm-architect/catalog.html`](icm-architect/catalog.html) · [**in a browser**](https://htmlpreview.github.io/?https://github.com/astetic-dev/cassini-cartographer/blob/main/example-map/icm-architect/catalog.html) | the map as a document |
| [`icm-architect/map/map.html`](icm-architect/map/map.html) · [**in a browser**](https://htmlpreview.github.io/?https://github.com/astetic-dev/cassini-cartographer/blob/main/example-map/icm-architect/map/map.html) | the same map as a graph you can walk |

Every noun on that shelf has a card, because the territory is small enough for
the first walk to draw them all. It is the one to read for what a workspace map
looks like when the documents *are* the objects.

## In both

`catalog.md` is what `catalog.html` renders. `objects/` holds the cards — one
per thing on the shelf, each with where it lives, what a change to it touches,
and the neighbour that looks connected and is not. `collisions.md` is there
because both territories reuse a word for more than one thing.

**Read them for the shape, not for the answers.** Both are third territories on
purpose, the same reason `examples.md` is worked against Taurus: the two
fixtures in `sample/` have to stay unsolved, or a reader could produce a perfect
map by copying instead of surveying, and the demonstration would prove nothing.

**Never load this folder during a survey.** It is evidence about Cassini, like
`sample/`, `receipts/` and `docs/` — see the table in `CLAUDE.md`. A survey that
reads a finished map has read somebody else's territory.
