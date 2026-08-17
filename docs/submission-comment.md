# Submission comment — ready to paste

Assembled per `reference/submission-kit.md`: hook → recording + repo → money-shot
→ receipt → writeup.

**Before posting, fill the two placeholders marked `<<>>`.** A human ships this;
Cassini does not post.

---

**It does not answer the question. It shortens it.**

Cassini is a cartographer. Point it at a body of work someone will change — a
repo, a vault, a client delivery — and it leaves a map: a short index, and one
card per thing that matters. The next reader, human or model, opens one card and
stops. Nobody has to eat the tree.

🎬 90-second explainer: `<<video link>>`
📁 Repo: `<<repo link>>`

📸 **The money shot.** A name must fail four sightings before it is written down
as dead. On a real 15,000-line desktop app, four commands looked unused after a
literal search. Two were reached by a name the program builds while running, so
neither appears anywhere as a string. One was called only from inside Rust. Only
one was genuinely unwired — and a planning document on disk explained how it got
that way. Four candidates, one ghost, and deleting working code is the expensive
error.

📸 **The receipt, including where it lost.** The folder ships a working fixture
and a 29-fact answer key, and `receipts/cold-run.md` carries two runs: a cold
session that did not build the entry, and a control with a plain "map this repo"
prompt and no folder at all.

**The control found every trap.** On a 183-line fixture there is no detection gap
— it fits in a context window. What it did instead was produce **561 lines of map
for a 183-line territory**, with **18 lines of source pasted in**. Cassini's first
run is 87 lines, zero code fences, every claim anchored.

The receipt says that plainly, along with the twelve defects the cold reader found
in the folder and what was done about each — including the two that would have
been fatal.

---

Cassini maps a body of work you did not write. Point it at anything someone will
change and it leaves one card per thing that matters. A cold reader opens one
card and stops.

The design choice: a card may never contain a code fence. Run a plain "map this
repo" prompt on our fixture and the map comes back three times the size of the
thing it maps, with source pasted in. Cassini's is half the size, every claim
anchored, every card stamped with its commit.

A map bigger than its subject is not a map.

---

## Ship checklist

- [ ] `<<video link>>` replaced — `odr-projects/cassini-cartographer/out/*.mp4`
      uploaded somewhere playable
- [ ] `<<repo link>>` replaced — entry folder pushed public
- [ ] `docs/cover.png` attached as the leading image
- [ ] `receipts/cold-run.md` present and honest, including the failures
- [ ] writeup is ≤100 words (currently 97 — recount if edited)
- [ ] no internal paths anywhere in the entry (`X:\`, customer names)
- [ ] a human posts it
