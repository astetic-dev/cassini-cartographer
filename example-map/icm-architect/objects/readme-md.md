# README.md
Type:     object
Status:   live
Reach:    inner (reached only from outside the agent's own routing chain)
Verified: 2026-08-14 at b20fb45 - checked from four directions; reached
from outside the workspace only

## Is
The human-facing landing page: what ICM is, the two modes, the six forms,
and how to install this skill into Claude Code or a Claude app.

## Lives at
- `README.md:12-19` - what it does, the two modes
- `README.md:23-27` - Install section (the two install paths)
- `README.md:29-40` - Layout table

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| (none found) | - | - |

No file in the territory's own routing chain (`CLAUDE.md`, `SKILL.md`)
names this file. Confirmed by grep across every `.md` file for the string
`README` - zero in-boundary hits.

## Hits
- nothing inside the boundary - a change here does not alter anything
  `CLAUDE.md` or `SKILL.md` route to.

## Does not hit
- CLAUDE.md - a reader who just read the root entry file might expect
  README.md to be the next hop in the routing chain the way SKILL.md is.
  It is not part of that chain at all; it is reached only by a human
  opening the repository directly, where GitHub renders it unprompted as
  the landing page - a convention outside this folder,
  not a rule inside it.

## Open
Whether this working copy still matches the upstream README at
`github.com/RinDig/icm-architect` (the source `CLAUDE.md:4` names) is not
checked here - out of boundary.
