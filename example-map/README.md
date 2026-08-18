# A finished map

This is not a fixture and not an answer key. It is one real deliverable, copied
here whole, so you can see what comes back before you run anything.

**The territory.** `icm-architect` — a Claude skill that designs a body of work
into an ICM workspace, by Jake Van Clief, MIT licensed,
[RinDig/icm-architect](https://github.com/RinDig/icm-architect). It was surveyed
as a **workspace**: 15 files, 792 lines of markdown, at commit `b20fb45`, on
2026-08-18, in the local deployment where it sits — which is why the map records
the root `CLAUDE.md` as a working copy that was never committed.

**Start with one of these two.**

| open | what it is |
|---|---|
| [`catalog.html`](catalog.html) &nbsp;·&nbsp; [**open in a browser**](https://htmlpreview.github.io/?https://github.com/astetic-dev/cassini-cartographer/blob/main/example-map/catalog.html) | the map as a document: the name, the maker, four paragraphs saying what the thing is, two signposts, what is here, the questions, and the counts at the foot |
| [`map/map.html`](map/map.html) &nbsp;·&nbsp; [**open in a browser**](https://htmlpreview.github.io/?https://github.com/astetic-dev/cassini-cartographer/blob/main/example-map/map/map.html) | the same map as a graph you can walk — click a part, watch what moves with it, and read the answer to the question that brought you there |

**Both are HTML, and GitHub shows HTML as source rather than rendering it.** The
second link in each row hands the file to a preview service so it opens as a
page; downloading the repo and double-clicking either file does the same thing
offline. Neither file loads anything from the network — the map is one
self-contained page, which is the whole point of it.

`catalog.md` is what `catalog.html` renders. `objects/` holds the eight cards —
one per thing on the shelf, each with where it lives, what a change to it
touches, and the neighbour that looks connected and is not. `collisions.md` is
there because one word in that territory names two different files.

**Read it for the shape, not for the answers.** A third territory is used here
on purpose, the same reason `examples.md` is worked against Taurus: the two
fixtures in `sample/` have to stay unsolved, or a reader could produce a perfect
map by copying instead of surveying, and the demonstration would prove nothing.

**Never load this folder during a survey.** It is evidence about Cassini, like
`sample/`, `receipts/` and `docs/` — see the table in `CLAUDE.md`. A survey that
reads a finished map has read somebody else's territory.
