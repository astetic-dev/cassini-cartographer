# The film — taurus

Ninety seconds on a 15,897-line codebase, in the nine scenes `film/film.md`
prescribes: a title, what it does, four steps along three stations, two things
to hold on to, and where to read on.

The three stations are the ones that file names for an application:

    the window  ->  73 names  ->  what survives a restart

What is here is the whole input, so the render is reproducible from the map:

| file | what it is |
|---|---|
| `taurus.mp4` | the film itself, 91 seconds, 6.0 MB — download it and play it locally |
| `taurus.srt` | the narration as subtitles, timed |
| `brief.md` | what the film is for, who is watching, and every claim it may make |
| `board.md` | the nine scenes: template, duration, narration, and the card each line came from |
| `data/` | one payload per scene — the stations, the step, the badge |

Rebuild it with [Odr](https://github.com/astetic-dev/odr), from this folder
copied into a project of your own:

    odr plan --project <dir>
    odr voice --project <dir>
    odr build --final --project <dir>
    odr assemble --final --project <dir>

`odr voice` is the gate worth watching: it speaks each line and measures it
against its scene. A line still being spoken when the picture cuts is the most
visible mistake a film can make.

**Every number spoken is on a card.** 73 registered names and 97 call sites come
from `objects/command-surface.md`; the two halves of a tab from
`objects/session.md`; the seven files from `objects/config-store.md`; the
command that is wired to nothing from `objects/session-history.md`; the trail
nobody listens for from `objects/ch-ssh-audit.md`; the word that names four
things from `collisions.md`. Re-survey the territory and those counts change,
which is why a film that quotes them has to be re-rendered.
