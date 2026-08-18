# Rendering a map to HTML

The cards are the map; this is the way most people will look at it. Built every
run, once the CATALOG gate closes — `rules.md` requires it and it is assembled
mechanically from cards already written, so it claims nothing new.

## Steps

1. Read the finished `catalog.md` and every card in `objects/`.
2. Build one JSON object matching the schema below.
3. Take `map-template.html`, replace `{{MAP_JSON}}` with that JSON, and write the
   result to `<territory>/map/map.html`.
4. **Write `map.html` before the markdown files** if you are generating both in
   one pass. Some viewers list workspace files newest-first, and the map should
   sort above its own view.

## The one escaping rule

After serialising, replace every `<` in the JSON with `\u003c` — a legal JSON
escape that `JSON.parse` turns back into `<`.

A card that cites a closing script tag or an HTML comment would otherwise
terminate the JSON block and silently truncate the map. Silently is the problem:
the page still renders, just with fewer nouns.

## Schema

```json
{
  "meta": {
    "title": "Hearth",
    "surveyed": "2026-08-16",
    "at": "working tree",
    "territoryFiles": 9,
    "territoryLines": 178,
    "cardsDir": "objects",
    "catalog": "catalog.md",
    "beatMs": 600,
    "staggerMs": 267,
    "collisions": [{ "word": "forget", "count": 3, "file": "collisions.md" }],
    "questions": [
      { "q": "What breaks if I rename a command?", "id": "command-surface" },
      { "q": "Where do the temperatures actually live?", "id": "hearth-state" }
    ]
  },
  "nouns": [
    {
      "id": "command-surface",
      "name": "Command surface",
      "type": "surface",
      "status": "live",
      "reach": "both",
      "summary": "9 names the panel may call",
      "source": "core.py:91",
      "card": "objects/command-surface.md",
      "hits": [ { "id": "hearth-state", "why": "...", "via": ["e:command-surface>hearth-state"] } ],
      "doesNotHit": { "id": "ch-reading-tick", "why": "..." },
      "dead": [ { "name": "schedule_forget", "status": "ghost", "at": "core.py:72" } ]
    }
  ],
  "edges": [
    { "id": "e:command-surface>hearth-state", "from": "command-surface",
      "to": "hearth-state", "kind": "calls", "label": "store.write",
      "status": "live", "source": "core.py:30" }
  ],
  "lint": [
    { "level": "warn", "code": "unbacked-hit", "noun": "zone",
      "message": "card claims a hit with no edge path", "at": "objects/zone.md:22" }
  ]
}
```

### Fields that carry weight

- **`meta.title` is the territory's own name and nothing else** — `hearth`, not
  `Map — hearth`, not `hearth system map`. The page does not need to announce
  that it is a page.
- **`meta.maker`** — who made the territory, if the territory says so. One line
  under the title. Omit rather than guess.
- **`meta.is` and `meta.explainer` — the description, and they are not
  optional.** The same prose that opens `catalog.md`: `is` is the first
  paragraph, `explainer` is the two or three that follow. On this page only the
  first paragraph is open; the rest sits behind a fold, because a page whose
  diagram starts below the fold has buried the thing it was opened for. The full
  description belongs to `catalog.md`, which is a document and can afford it. Without them the page
  opens on a graph of parts belonging to nothing, and a reader who does not know
  what they are looking at cannot use an accurate diagram of its insides. Plain
  language throughout — the banned method words in `rules.md` are banned here
  too.
- **`meta.topics` — lenses, and where the reader goes after the map.** They sit
  **below the diagram**, not above it: the map is the thing that was asked for
  and it goes first; the questions are how you interrogate it once you have seen
  it. They stay on screen inside a card as well — this list is how a reader
  moves around the page, and navigation that disappears the moment you use it is
  not navigation. The question that was followed is marked in place. A reader arrives wanting to talk about *one aspect* — how it is built,
  what it can do — so group the questions that way. Each question carries three things:

  ```json
  { "q": "Where does a terminal tab actually live?",
    "id": "session",
    "answer": "In two places at once. The process is a ConPTY owned by Rust (`lib.rs:3460`) ..." }
  ```

  The **`answer` is the point**. A highlight on a graph is not an answer to
  anything — the reader asked a question in words and wants words back. Two to
  four sentences, every claim anchored, and every claim already on the card it
  routes to. If an answer says something no card says, the card is missing a
  fact, not the answer.

  Answers are escaped and then backticks are re-admitted as `<code>`. Do not put
  markup in them.

  A flat `meta.questions` array still works and renders as one unnamed lens.

- **Questions must be about the territory, not about its maintenance.** "What
  breaks if I rename a command?" is a chore. "Where does a terminal tab actually
  live?" is the territory. The second is what a reader came for; the first is
  what a linter would ask.

- **Let an answer be "no".** The most valuable question in the Taurus map is
  "Can I forget a session from the history?" and the answer is no, because the
  command exists and nothing calls it. A question set with no negative answers in
  it is a feature list wearing a question mark.
- **`edges[].label` is the content, not decoration.** It is drawn on the line.
  Without it the graph says only that two things touch, never how. `zone_list`,
  `store.forget`, `boiler_on / boiler_off (constructed)` — those labels are what
  turn a shape into a map.

- **`status`** is `live` / `leftover` / `ghost`, on nouns **and independently on
  edges**. A live noun can have a dead output edge — a function that does real
  work and also announces itself on a channel nobody listens to. If edge status
  were derived from its endpoints, that finding would be invisible.
- **`hits[].via`** is the ordered list of edge ids from the origin to the thing
  it hits. Compute it once, here. The page replays that path; it never re-derives
  the graph. Two consequences: the animation cannot disagree with the edge table,
  and any claim on screen can be traced back to a card.
- **`doesNotHit`** is one object, not a list. The card promises *the* wrong
  neighbour. Three is hedging.
- **`lint`** is what the generator disagreed with. Render it; do not swallow it.
  The most useful code is `does-not-hit-is-reachable` — the edge table saying a
  card's own `Does not hit` is wrong.

## Prose ceilings — fail, do not truncate

- `summary` — 200 characters
- `hits[].why` — 120
- `doesNotHit.why` — 160

Over the ceiling, stop and fix the card. Truncating makes the view fatter and
the card wronger. These limits are the reason the HTML physically cannot become
a substitute for reading the map.

## What the page must not do

It runs inside a sandboxed frame with an opaque origin in at least one of its
three targets. So: no `localStorage`, no `sessionStorage`, no cookies, no
`fetch`, no `history.pushState` — these throw rather than fail quietly. No
external stylesheet, script, font or image. Read `location.hash` once at boot
inside a `try`, and treat it as write-only afterwards.

An embedded webfont is blocked outright by a `font-src 'self'` policy the page
inherits and cannot see. Use the system stack in the template.

## Size

A 13-noun map lands around 70 KB. If it passes **250 KB**, something is wrong —
almost always an embedded image, or prose that belongs on a card.
