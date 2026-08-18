# Turning a map into a film

Optional, and third in line. The cards are the map; `map.html` is one way to look
at them; a film is another. **The film is about the territory, never about the
cartographer.** Map Porter and you get a film that explains Porter.

## What you need — read this before starting

**Nothing in this section is required to use Cassini.** The map is markdown and
needs no tools at all; `render/map-template.html` needs a text editor and a
browser. Only this step reaches outside the folder.

A film needs an animation studio. This folder is written against **Odr** — a
multi-engine studio, MIT-licensed, free to run locally:

> **https://github.com/astetic-dev/odr**

Install it, then check the machine before you plan anything:

```
odr doctor
```

You need `node`, `ffmpeg`, and the **hyperframes** engine reported `ok`. Piper
supplies the narration and is optional — without it you get a silent picture and
subtitles, which is still a usable film. On Windows, hyperframes is marked beta
and Odr passes `--experimental-fast-capture=false` for you; if a render dies at
frame 0 with *"drawElement canvas not initialized"*, that flag is why.

First run also wants a projects root **outside** the Odr repo:

```
odr setup --non-interactive --projects-root <a folder of your own> \
          --brand _example-blueprint --style technical-diagram
```

**Using a different studio?** The shape below is what matters, not the tool.
Nine scenes, three stations, one step per phase, and narration sized to the
scene. Any studio that takes a scene list and a data payload per scene can
render it; only the command names change.

Everything spoken must already be a claim on a card. If a line of narration says
something no card says, the card is missing a fact — fix the card, not the script.

## Two worked examples

Both films in `example-map/` are this shape, rendered from the maps beside them:

| film | subject | three stations |
|---|---|---|
| `example-map/taurus/film/` | a codebase | the window → 73 names → what survives a restart |
| `example-map/icm-architect/film/` | a workspace | how you describe it → the method → a folder that runs |

Each folder carries `brief.md`, `board.md` and one payload per scene — the whole
input, so the render is reproducible from the map and this file alone. Read
`board.md` first: the `#### NOTE` under every scene names the card the line came
from, which is what "everything spoken is already on a card" looks like when it
is being obeyed. One line in the second film had no card behind it; the card
gained the anchor, per the rule above.

## The shape that works

Three stations carry an entire explainer, and they are the same three every time:

```
<what goes in>  ->  <the thing being mapped>  ->  <what comes out>
```

For an intake operator that is *the inbox → Porter → the workspace*. For an app
it is *the panel → the core → what survives a restart*. Two rails above and
below carry the two directions. Each step along the rails is one noun or one
phase from the catalog.

Nine scenes, about 88 seconds:

| scene | template | drawn from |
|---|---|---|
| 1 | `title-card` | the catalog's opening sentence |
| 2 | `takeaway-split` | the "what it does" paragraphs |
| 3–6 | `flow-rails` | one step each, from the shelf and the walks |
| 7–8 | `takeaway-split` | what holds it together; the collisions |
| 9 | `outro-refs` | the one rule: catalog, then one card |

## What the payloads want

`flow-rails` was written for HTTP calls, so it offers `request.method`,
`request.path`, `response.status` and `response.text`. Do not fight it, and do
not leave `status` as an HTTP code — it renders as a bold value directly before
the text, so use it as **a short count that reads into the sentence**:

```
status "8"  text "of 9 schemas point here"    ->  8 of 9 schemas point here
status "1"  text "appended line per email"    ->  1 appended line per email
```

A `status` of 200 with unrelated text produces `200 appended line per email`,
which is how the first draft of this went wrong.

Put badge annotations at `at_pct: 0.28`. Two things are already on that rail and
a badge has to miss both: the packet travels and lands around 0.4–0.7, and the
rail's own label — `REQUEST`, `COMES BACK` — sits hard left. A badge is centred
on its `at_pct`, so 0.16 reaches back across the label and prints a badge over
the word; 0.28 clears the label and still lands well before the packet. Add
`layout-occlusion` to `qc_focus` on every `flow-rails` scene, and look at the
frames the render drops in `qc/` — this one was found there, in a finished cut,
with the gate passed and the label reading *COMES B*.

## Sizing the narration

Roughly **12.5 spoken characters per second**, and the estimator runs 3–8%
optimistic. Budget `dur_s × 12.5 × 0.9` characters per scene and the voice gate
will pass first time.

Two gates will stop you, and both are worth the friction:

- **`odr plan`** rejects a board whose narration does not fit its scenes.
- **`odr voice`** synthesises the audio and measures it. A line still being
  spoken when the picture cuts is the most visible mistake a film can make.

## The run

```
odr init map-<territory>
odr plan --project <dir>
odr voice --project <dir>
odr build --final --project <dir>
odr assemble --final --project <dir>
```

The finished file is the one in `out/` — the one under `renders/` has no audio.

## What a film must not do

- **Never sell.** No adjectives about how good the work is; the same rule as a
  card, and it is easier to break out loud than in writing.
- **Never diagnose.** Where a name reads as live and is not, give a direction —
  *do not build on this one* — and move on. The film is not a defect report
  either.
- **Never say a number the map does not carry.** Re-survey the territory and the
  counts change; a film that quotes them has to be re-rendered.
