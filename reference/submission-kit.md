# The submission kit — how the entry's two public documents were built

Not survey doctrine. A running survey never loads this file. It documents how
`docs/writeup.md` and `docs/submission-comment.md` — the two documents a judge
is most likely to read — were assembled, so both can be checked against a real
shape instead of citing one that was never written down.

## Two documents, two shapes

| document | budget | shape |
|---|---|---|
| `docs/writeup.md` | ≤100 words, checked by `checks/count-writeup.py` | who it is for / what it does / one design choice and why |
| `docs/submission-comment.md` | none — ready to paste whole | hook → recording + repo → money-shot → receipt → writeup |

Each is built once, from what the rest of the repo already has on disk.
Neither invents a claim the entry cannot back with an anchor.

## The writeup's shape

`docs/writeup.md` is one paragraph, three unlabelled parts, in this order:

1. **Who it is for.** One sentence naming the reader and the trigger — point it
   at anything someone will change.
2. **What it does.** What comes back, and what a reader does with it: one card
   per thing that matters, opened one at a time, stop.
3. **One design choice and why.** Not a feature list — one choice, argued, with
   a number attached. The choice named is "a card may never contain a code
   fence", measured against what the same prompt produces without the rule
   (`receipts/cold-run.md`, Run B: 9 fenced blocks, 18 lines of source pasted
   in).

It closes on one sentence that restates the whole entry in six words: "A map
bigger than its subject is not a map."

The word count sits directly under the paragraph, in the same file, checked by
`checks/count-writeup.py` rather than by eye. Recount whenever the paragraph
changes.

Below the count, `docs/writeup.md` keeps two things that are not part of the
100 words and are not pasted anywhere else: the case for the design choice
against the two runners-up it beat, and the hook line handed to the comment.
Both stay in `docs/writeup.md` alone — neither is quoted a second time
anywhere in the entry.

## The comment's shape

`docs/submission-comment.md` is a fixed chain, in this order, nothing added:

1. **Hook.** One line, the same line named in `docs/writeup.md`'s "hook line
   for the comment" section — the refusal in `examples.md`: "It does not
   answer the question. It shortens it."
2. **Recording + repo.** The 90-second explainer (`film/film.md`) and the repo
   link, in that order — a judge who wants proof watches or clones before
   reading the rest.
3. **Money-shot.** Two `📸` call-outs, each one concrete result a judge can
   check without cloning anything: the four-sightings result on Taurus
   (`examples.md`, exchange 2 — the triangulation) and the control-run
   comparison (`receipts/cold-run.md`, Run B).
4. **Receipt.** A pointer to `receipts/cold-run.md` by name, not a restatement
   of it. The receipt is long because it is honest about where the entry lost;
   repeating that here would give the same facts a second home.
5. **Writeup.** The 100-word paragraph from `docs/writeup.md`, quoted verbatim,
   because the platform's comment field cannot transclude another file at
   posting time. This is a marked copy, not a second original — see the note in
   `docs/writeup.md` and in this file's own ship checklist.

Then the ship checklist: what has to be true before a human posts it, closing
on "a human posts it" — Cassini does not.

## Keeping the two in sync

The writeup's closing paragraph is the one piece of text both documents need
word for word. `docs/writeup.md` is its one home; `docs/submission-comment.md`
holds a marked verbatim copy near its ship checklist. Edit the paragraph in
`docs/writeup.md`, recount with `checks/count-writeup.py`, then copy the new
text into `docs/submission-comment.md` before ticking that line off.
