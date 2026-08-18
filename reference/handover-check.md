# The last walk — over your own map

Run this after `catalog.html` and `map.html` are written and before you hand
anything back. It is a walk like any other: over a territory of six or eight
files that somebody has just produced, looking for what is there.

**Read the written files, cold.** Not your memory of them, not your intention —
open `catalog.md`, the cards, `collisions.md`, and the two rendered pages, and
read them as though somebody else wrote them and you have to answer for it. The
map you meant to write cannot be checked.

---

## 1 Whose walk wrote this?

Every sentence on a deliverable belongs to one of three walks, and only one of
them is yours.

| walk | what its sentences do | tells |
|---|---|---|
| **cartographer** | says what is there, what it does, what moves with it, and which neighbour a reader would guess wrong | a fact with an anchor, and a consequence for somebody about to change something |
| **editor** | says what should be different | *but*, *should*, *missing*, *only*, *not wired up properly*, a count of what is absent, a remark on a name or a layout, a null result of your own search |
| **diagnostician** | says why something is as it is | *because*, *caused*, *since*, *was meant to*, any claim about the past |

Go sentence by sentence. An editor's or a diagnostician's sentence is rewritten
into what is there, or cut. Two clarifications, because both come up every time:

- **A ghost is cartography, not a snag.** *"Nothing calls this, so do not build
  on it"* is a road sign. *"This should be removed"* is somebody else's walk.
- **The one thing you may call broken** is an intent the work itself declares
  and does not carry out — what it is meant to do, then what happens instead,
  once. See `identity.md`, "Reading the intent". Everything else that does not
  work is a diagnosis, and you were not asked for one.

## 2 Did the reader get what they came for?

Write one sentence, in your own words: **what did the person who asked want out
of this?** Then open the map and check it is answered before anything else.

A map can be true in every particular and still fail here. If the first thing a
reader meets is the survey — file counts, what was walked, how it was checked —
then the sheet opens on the instrument and the subject arrives late, and the
person who asked what this thing *does* has to hunt for it. The description
comes first, in prose, and the counts go to the back.

Check as well that the questions are the ones a reader would actually ask, and
that at least one answer is **no**. A question set with no negative answers in
it is a feature list wearing a question mark.

## 3 Is the instrument on the sheet?

Mechanical, and the reason this check has a gate rather than a reminder. Over
everything that is prose:

    grep -nEi 'sweep|sighting|triangulat|census|perimeter gate|W[1-6] |ghost|leftover|do-not-map' catalog.md collisions.md objects/*.md catalog.html

Zero hits, or fix them.

`map.html` is checked differently, because it is a program: its data block
carries the three status values by design, and its layout code has a loop
called a sweep. Read the page instead — the node labels, the legend, the counts
strip, the panel headings — and confirm the words appear nowhere a reader sees.
This is where the first run of this check found one: every node on the graph was
printing its own field value onto the picture. The words belong to the walk, not to the map: a reader
who has to learn the instrument before reading the sheet has been handed the
instrument. `reference/card-types.md` carries the plain forms.

Two more that are worth running while you are there:

- **Signposts.** At most three, plus the collision pointer, and each one has to
  survive the test in `rules.md`: a reader who does not know it *builds the
  wrong thing*.
- **Open fields.** Each one names something this card does not know about the
  territory. An `Open` that names a gap in the work is an editor's note with a
  polite heading. `Nothing` is a legal answer and a common one.

---

## Say what it found

Report the pass to the person who asked, not on the map: what it changed, in a
line or two. **A check that never finds anything is not being run** — this walk
turned up six sentences on its first outing, on a map written by someone who had
just finished writing the rule they broke. Expect to find something. If you find
nothing at all, say that too, and say what you looked for.
