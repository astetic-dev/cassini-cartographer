# The film — icm-architect

Ninety seconds on a 792-line markdown workspace, in the same nine scenes as the
film beside it. Same shape, other subject — which is the point of shipping both.

The three stations, for a workspace:

    how you describe the work  ->  the method  ->  a folder that runs

| file | what it is |
|---|---|
| `icm-architect.mp4` | the film itself, 91 seconds, 5.9 MB — download it and play it locally |
| `icm-architect.srt` | the narration as subtitles, timed |
| `brief.md` | what the film is for, who is watching, and every claim it may make |
| `board.md` | the nine scenes: template, duration, narration, and the card each line came from |
| `data/` | one payload per scene — the stations, the step, the badge |

Rebuild it with [Odr](https://github.com/astetic-dev/odr), from this folder
copied into a project of your own:

    odr plan --project <dir>
    odr voice --project <dir>
    odr build --final --project <dir>
    odr assemble --final --project <dir>

**One line here had no card behind it.** The walk test — *an agent with no
memory must orient, act and report status from the files alone* — was named on
`objects/skill-md.md` without an anchor, so the film could not say it. The rule
in `film/film.md` says which way that gets resolved: the card was missing a
fact, so the card gained `SKILL.md:85-97`, and the line stayed. Fix the card,
not the script.
