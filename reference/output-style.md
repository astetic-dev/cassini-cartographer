# Output style — the Taurus house style render

`catalog.md` is the deliverable. This file is how it also goes out as a
self-contained HTML page, in the house style shared across the Taurus family of
specialists, so the map is never handed back as a wall of unstyled markdown.

This is separate from `map.html` (`render/render.md`) — that is an optional
interactive view of the whole card graph, built from JSON assembled out of every
card. This file renders `catalog.md` alone: the index, as a document. Both are
views. Neither replaces the cards.

## The template

The tokens `{{NAME}}`, `{{ROLE_NOUN}}` and `{{FIELD_CAPTION}}` are fixed for
Cassini and are already filled in below — nothing to guess at. Two tokens stay
open because they are decided at generation time:

- **`{{DATE}}`** — the date on `catalog.md`'s own staleness stamp: the day the
  cards behind it were last verified, the same date that appears on the cards
  themselves (`Verified: <date> at <sha>`, `reference/card-types.md`).
- **`{{SUBJECT_OR_SESSION_ID}}`** — the territory name and the short commit sha
  it was surveyed at, in the form the catalog already opens with — e.g.
  `Taurus @ e652c79`. On a workspace subject, use the workspace's name in place
  of a repo name; there may be no sha, in which case say `working tree`.
- **`{{DOCUMENT_TITLE}}`** — `Map — <Territory>`, matching the catalog's own
  first line (see `examples.md`, "**Map — Taurus**").

The repeatable blocks (`<h2>`, `.callout`, `.lede`, `table`) are not
one-per-document — use as many of each as `catalog.md` needs. The mapping:

| catalog.md content | template element |
|---|---|
| the one/two sentence "what this is" plus the counts line (nouns · commands · channels · collisions · unwired) | `.lede` |
| the staleness banner, if the territory moved since the cards were verified | one `.callout`, placed **before** the `.lede`, immediately under `<h1>` — matches `reference/card-types.md`'s "does not count against the 60" |
| each signpost — a road sign, not a snag list | one `.callout` per signpost; `.label` is the bolded lead phrase (e.g. `history_forget is not wired`), the callout body is the rest of the sentence |
| "If your question is…" | an `<h2>` heading, then a `table` — question in the left column, the card it routes to in the right, as a relative link (`objects/<noun>.md`) since `catalog.html` sits beside `objects/` |
| the shelf | an `<h2>` heading, then a `table` — noun, type, status, reach, and a relative link to its card |
| what is not on the shelf | an `<h2>` heading with a short `<p>`, or a closing `.callout` if it is one or two lines |

A single card is never expanded into its own Taurus page — a card already has a
closed schema and a 40-line ceiling (`reference/card-types.md`); wrapping it
would only add chrome around a document already built to be opened alone.

## Generating it

Fill the template below, write it to `<territory>/catalog.html`, next to
`catalog.md`. Regenerate it every time `catalog.md` changes — it is a rendering
of the catalog, not a separate source of truth. `<`, if it appears inside a
question or a signpost quoted from source, gets escaped to `&lt;` the same way
the JSON in `render/render.md` does; nothing here is ever injected as raw HTML.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CASSINI — {{DOCUMENT_TITLE}}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:        #f3ead6;
    --paper-edge:   #e6d8b4;
    --ink:          #2b2013;
    --ink-soft:     #5b4c34;
    --wood-dark:    #201609;
    --wood-mid:     #34240f;
    --brass:        #b6893f;
    --brass-bright: #d9b06b;
    --rule:         rgba(43,32,19,0.28);
    --shadow:       rgba(0,0,0,0.35);
  }
  @media (prefers-color-scheme: dark){
    :root{
      --paper:      #241a10;
      --paper-edge: #1a1109;
      --ink:        #ecdfc0;
      --ink-soft:   #b8a37d;
      --wood-dark:  #120c05;
      --wood-mid:   #1c130a;
      --brass:      #c99b4c;
      --brass-bright:#e6bd76;
      --rule:       rgba(236,223,192,0.22);
      --shadow:     rgba(0,0,0,0.6);
    }
  }

  *{ box-sizing:border-box; }
  html,body{ margin:0; padding:0; }
  body{
    background: var(--wood-dark);
    background-image:
      radial-gradient(ellipse at 20% -10%, rgba(217,176,106,0.10), transparent 55%),
      linear-gradient(180deg, var(--wood-dark), var(--wood-mid));
    color: var(--ink);
    font-family: 'EB Garamond', Georgia, 'Times New Roman', serif;
    font-size: 18px;
    line-height: 1.6;
  }

  /* ---------- masthead ---------- */
  .masthead{
    padding: 3.2rem 2rem 2.2rem;
    text-align: left;
    max-width: 860px;
    margin: 0 auto;
  }
  .masthead .name{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 600;
    font-size: clamp(2.4rem, 6vw, 3.6rem);
    letter-spacing: 0.18em;
    color: var(--brass-bright);
    text-shadow: 0 1px 0 rgba(0,0,0,0.4), 0 0 24px rgba(217,176,106,0.15);
    margin: 0;
    text-transform: uppercase;
  }
  .masthead .rule{
    height: 1px;
    background: linear-gradient(90deg, var(--brass) 0%, rgba(182,137,63,0.15) 70%, transparent 100%);
    margin: 0.55em 0 0.7em;
  }
  .masthead .role{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-style: italic;
    font-weight: 500;
    font-size: 1.15rem;
    color: #cabb98;
    margin: 0 0 0.3em;
  }
  .masthead .meta{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #8a7a5c;
  }

  /* ---------- page / content card ---------- */
  .page{
    max-width: 860px;
    margin: 0 auto 3rem;
    background: var(--paper);
    border: 1px solid var(--paper-edge);
    box-shadow: 0 20px 50px var(--shadow);
    border-radius: 2px;
    padding: 3rem 3.2rem 3.4rem;
  }
  @media (max-width: 640px){
    .page{ padding: 2rem 1.3rem 2.4rem; margin-left:0.6rem; margin-right:0.6rem; }
    .masthead{ padding: 2.2rem 1.3rem 1.6rem; }
  }

  .page h1, .page h2, .page h3{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 600;
    color: var(--ink);
  }
  .page h1{
    font-size: 1.9rem;
    letter-spacing: 0.02em;
    margin: 0 0 0.3em;
  }
  .page h2{
    font-size: 1.35rem;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    color: var(--ink-soft);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 0.35em;
    margin: 2.2em 0 0.9em;
  }
  .page h2:first-of-type{ margin-top: 0.4em; }
  .page h3{
    font-size: 1.1rem;
    font-style: italic;
    color: var(--ink);
    margin: 1.6em 0 0.5em;
  }
  .page p{ margin: 0 0 1em; }
  .page ul, .page ol{ margin: 0 0 1.1em; padding-left: 1.3em; }
  .page li{ margin: 0.3em 0; }

  .page .lede{
    font-size: 1.08rem;
    color: var(--ink-soft);
    font-style: italic;
    border-left: 2px solid var(--brass);
    padding-left: 0.9em;
    margin: 0 0 1.8em;
  }

  .callout{
    border-left: 2px solid var(--brass);
    background: rgba(182,137,63,0.08);
    padding: 0.85em 1.1em;
    margin: 1.2em 0;
    font-size: 0.98rem;
  }
  .callout .label{
    display:block;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-style: italic;
    color: var(--brass);
    margin-bottom: 0.25em;
  }

  table{ width:100%; border-collapse: collapse; margin: 1.2em 0; font-size: 0.95rem; }
  th, td{ text-align:left; padding: 0.5em 0.7em; border-bottom: 1px solid var(--rule); }
  th{ font-family:'Cormorant Garamond', Georgia, serif; text-transform:uppercase; letter-spacing:0.06em; font-size:0.82rem; color: var(--ink-soft); }

  .divider{
    border: none;
    border-top: 1px solid var(--rule);
    margin: 2em 0;
  }

  .quote-source{
    display:block;
    font-size: 0.85rem;
    color: var(--ink-soft);
    margin-top: 0.4em;
  }

  footer{
    max-width: 860px;
    margin: 0 auto 3rem;
    padding: 0 3.2rem;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #8a7a5c;
  }
  footer .rule{ flex:1; height:1px; background:var(--rule); margin: 0 1em; }
</style>
</head>
<body>

  <div class="masthead">
    <div class="name">CASSINI</div>
    <div class="rule"></div>
    <div class="role">the cartographer</div>
    <div class="meta">{{DATE}} &middot; {{SUBJECT_OR_SESSION_ID}}</div>
  </div>

  <div class="page">

    <h1>{{DOCUMENT_TITLE}}</h1>
    <p class="lede">{{One or two sentence summary of the territory, plus the counts line.}}</p>

    <div class="callout">
      <span class="label">{{signpost lead phrase}}</span>
      {{the rest of the signpost sentence — one .callout per signpost}}
    </div>

    <hr class="divider">

    <h2>If your question is…</h2>
    <table>
      <tr><th>question</th><th>open</th></tr>
      <tr><td>{{question}}</td><td><a href="{{relative path to objects/&lt;noun&gt;.md}}">{{card}}</a></td></tr>
    </table>

    <hr class="divider">

    <h2>Shelf</h2>
    <table>
      <tr><th>noun</th><th>type</th><th>status</th><th>reach</th><th>card</th></tr>
      <tr><td>{{noun}}</td><td>{{type}}</td><td>{{status}}</td><td>{{reach}}</td>
          <td><a href="{{relative path}}">{{card}}</a></td></tr>
    </table>

    <hr class="divider">

    <h2>Not on the shelf</h2>
    <p>{{what was deliberately left off, and why.}}</p>

  </div>

  <footer>
    <span>TAURUS</span>
    <span class="rule"></span>
    <span>MAPPING</span>
  </footer>

</body>
</html>
```
