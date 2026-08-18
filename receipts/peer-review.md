# Peer review — three siblings pointed at this folder

`cold-run.md` scores Cassini against a fixture. This is a different kind of receipt: three
sibling specialists from the same family — Forseti (editor), Mimir (diagnostician), Kvasir
(researcher) — each pointed at *this folder itself*, on 2026-08-18, independently and without
reading each other's output first. All three sessions were read-only against this repository;
the fixes below were applied afterward, in a fourth pass.

Each ran its own real method: Forseti mined this folder with `checks/mine.py` (borrowed from
the family, this folder still has none of its own — see *What Kvasir found*) and gated its
review through `checks/verify.py` before delivering it. Mimir marked every claim in its finding
`[seen]` / `[inferred]` / `[general]` and passed its own gate. Kvasir ran its five-phase method
inside-first across all six sibling repos before going outside.

## What Forseti found

Bar: **public** — a stranger clones this and uses it without asking anyone, which is what a
competition judge is. ICM layer only; no output was supplied, so height 3 (does a Cassini map
meet Cassini's own standard) did not run.

**2 BREAKS, 2 COSTS, 0 SUGGESTION** — full findings, gated, in commit history at the fix commit
below.

- **F-01 BREAKS.** `docs/writeup.md` and `docs/submission-comment.md` both opened by citing
  `reference/submission-kit.md` — a file that did not exist anywhere in the tree, confirmed by a
  full-tree search, not a single grep.
- **F-02 BREAKS.** `docs/writeup.md` claimed its own word count was "checked with a script, not
  by eye." No script existed anywhere outside the `sample/hearth` fixture code. The number
  itself was correct (97, hand-recounted) — only the tooling claim was false, and
  `reference/card-types.md` makes the identical kind of promise about its own 40-line limit, so
  this was read as a pattern, not a one-off.
- **F-03 COSTS.** `reference/edge-census.md` (278 lines) and `reference/ghost-tests.md` (246)
  both broke the canon's 200-line reference-file guardrail with no reasoning recorded anywhere
  for it.
- **F-04 COSTS.** The closing paragraph of `docs/writeup.md` was duplicated verbatim in
  `docs/submission-comment.md`, caught independently by `mine.py`'s own duplication scan, with
  nothing keeping the two copies in sync.

Explicitly **not** raised as a finding, after checking rather than assuming: the absence of
`DEFECTS.md`, `CREDITS.md`, `checks/`, `eval/` — the shape every sibling in this family carries.
Forseti's own rule is that a preference is not a finding where both the work's own word and the
canon are silent, and neither promises those specific files. `receipts/cold-run.md` already
carries the substance a `DEFECTS.md` would, under a different name.

## What Mimir diagnosed

One structural cause, evidence tier B (the mined tree plus this repository's own git history,
called out as outside the normally-mined tree): **`docs/` is excluded from every check this
workspace runs on itself.** `CLAUDE.md`'s own routing doctrine classifies `docs/` — alongside
`receipts/` and `sample/` — as "evidence about Cassini, never loaded." The one self-audit this
workspace ran (`cold-run.md`, above) never opened `docs/` — its own defect table touches
`README.md`, `examples.md`, `reference/*.md`, `rules.md`, never `docs/`. A later commit that
hand-edited `docs/submission-comment.md` itself — changing its repo link and shipping checklist
— still passed over the broken citation two lines above, on the same file, in the same edit.

Ruled out and stated as ruled out: a stale reference to a file that once existed and was cut —
`git log --all -p` shows `submission-kit.md` appears only inside the two citations, in every
commit including the first. The file was never written, so nothing was cut.

This survives the obvious repair. Deleting the two dangling lines, or stubbing the file, leaves
`docs/` exactly as unrouted as before — which is why the fix below wrote the file for real
rather than just removing the two lines.

## What Kvasir found

Inside sweep across all six sibling repos, no outside sweep needed — the question resolved
inside. **Cassini is the only one of the six family repos with zero of
`DEFECTS.md`/`CREDITS.md`/`checks/`/`eval/`** (Forseti is the nearest, missing only
`CREDITS.md`). Nothing in any of the six repos' own prose, in this repo's git history, or in any
sibling's `DEFECTS.md`, addresses the absence — it was original to the first commit, not a
regression.

The sharper finding: this repo's own reference files repeatedly assert that its properties are
**"checkable by a script, which is the point"** (`reference/card-types.md`, the 40-line card
limit; `reference/wrong-neighbours.md`) — the same vocabulary the rest of the family uses to
justify the `checks/` scripts it actually built — while shipping no script of its own before this
pass (three `.py` files existed, all fixture code). An earlier quick pass over this repo had
guessed the absence "might be intentional" for a mapping tool; that guess does not survive the
grounded sweep and points the other way.

Left open, not filled in: whether the remaining gap (no `DEFECTS.md`/`CREDITS.md`/`checks/`
beyond the one script this pass added, still no `eval/`) is a considered choice or unfinished
work. That is the owner's call, not a fact a researcher gets to invent.

## The fix

All four of Forseti's findings were actioned, at the owner's direction, in the same pass:

- **F-01** — wrote `reference/submission-kit.md` for real, extracting the structure both
  `docs/` files already followed rather than inventing one from nothing.
- **F-02** — added `checks/count-writeup.py`, scoped to the one job of checking the writeup's
  word count against its own claim. `docs/writeup.md`'s sentence now names it.
- **F-03** — checked whether the codebase/workspace split Forseti suggested was actually clean
  before doing it. It was not: `ghost-tests.md` says of its own verdicts section that it
  "governs both sets" and is "not repeated for the workspace" — splitting would have forced
  duplicating load-bearing content this repo's own canon rules against. Added a short
  guardrail-exception note to both files instead, in the shape `reference/output-style.md`
  already carried. Nothing was cut.
- **F-04** — `docs/writeup.md` is now the one stated home for the shared closing paragraph;
  `docs/submission-comment.md` keeps its own copy (it has to stay a standalone paste for a
  competition platform) but now says so and says which file to edit first.

`checks/mine.py`'s duplication scan still flags the F-04 text as a match after the fix, by
design — the paragraph is still, deliberately, identical text in both files. What the scan is a
proxy for (no canonical source) is closed by the note; the raw text match it can also still see
is not, and cannot be while `docs/submission-comment.md` has to remain paste-ready.

Fix commit: `3800fd7`. Canonical-source header on the shared house-style file, from the same
day's earlier pass: `a84cd8d`.
