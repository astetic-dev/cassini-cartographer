# Wren

The ringing station's week. One raw log in, two artifacts out: the return that
goes to the scheme, and the post that goes on the station site.

Running since week 12. One run per week, Monday morning, after the last net round
of the week before.

## Folder map

```
wren/
  CLAUDE.md
  CONTEXT.md
  input/
    week-28.md
  notes/
    handover.md
  references/
    house-voice.md
    scheme-columns.md
    species-names.md
  stages/
    01-tally/
    02-return/
    03-post/
    04-recoveries/
```

The map says what is on disk. It does not route anything. A stage runs when
`CONTEXT.md` routes to it or a trigger below fires it. A reference file is loaded
when a stage's `Inputs` names it, or when a standing rule in `CONTEXT.md` binds
it. Nothing else reaches anything, and a folder nobody routes to is a folder that
never runs.

## Routing

| You want to | Go to |
|---|---|
| Run the week | `CONTEXT.md` |
| Know how the post reads | `references/house-voice.md` |

## Triggers

| Keyword | Action |
|---|---|
| `tally` | Run `stages/01-tally/CONTEXT.md` on its own |
| `return` | Run `stages/02-return/CONTEXT.md` on its own |
| `handover` | Append this session to `notes/handover.md` |

## The week number

Every artifact name carries the week. `<nn>` in an `Inputs` or `Outputs` row is
the week the run covers, two digits, and it comes from the log's filename.
