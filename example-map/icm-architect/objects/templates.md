# Templates (assets/templates/)
Type:     object (cluster, 8 members)
Status:   live
Reach:    inner
Verified: 2026-08-14 at b20fb45

## Is
Eight copyable starters - CLAUDE.md, CONTEXT.md, stage-CONTEXT.md, node.md,
object.md, process.md, schema.md, questionnaire.md - blank shapes a *new*
workspace is instantiated from. Nothing here is edited in place; the job is
to be copied out, per invariant 10 (`SKILL.md:27`).

## Lives at
- `assets/templates/CLAUDE.md:1-27`
- `assets/templates/CONTEXT.md:1-14`
- `assets/templates/stage-CONTEXT.md:1-21`
- `assets/templates/node.md:1-29`, `object.md:1-43`, `process.md:1-38`
- `assets/templates/schema.md:1-24`, `questionnaire.md:1-9`

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| routes | SKILL.md → assets/templates/* (bare-name list) | `SKILL.md:110` |
| routes | SKILL.md → assets/templates/stage-CONTEXT.md | `SKILL.md:21` |
| cites | references/core.md → assets/templates/stage-CONTEXT.md | `references/core.md:36` |
| cites | references/system-map.md → object.md, process.md | `references/system-map.md:40` |

## Hits
- nothing inside this territory reads a template's *content* - copying
  happens outside the boundary, into a new workspace this territory does
  not contain.

## Does not hit
- the root `CLAUDE.md` at the territory's own root (see its card) -
  `assets/templates/CLAUDE.md` shares the exact filename with the real
  entry file one level up. They are unrelated files with different jobs.
  See `collisions.md`.

## Dead here
None. All eight are named by `SKILL.md:110`'s bare-name list or a more
specific pointer; every one of them is named or reached from the method.

## Open
Nothing.
