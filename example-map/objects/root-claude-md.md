# Root entry (CLAUDE.md)
Type:     object
Status:   live
Reach:    entry
Verified: 2026-08-18, working tree, uncommitted (git status: untracked)

## Is
The workspace's root routing file: names SKILL.md as the method and
`references/` as the reference material, and names `blueprints/` as where
work produced here should be saved.

## Lives at
- `CLAUDE.md:8` - names SKILL.md
- `CLAUDE.md:9` - names references/
- `CLAUDE.md:11` - names blueprints/ (outside this boundary)
- `CLAUDE.md:17-18` - self-describes as Taurus-generated, not shipped upstream

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| routes | CLAUDE.md → SKILL.md | `CLAUDE.md:8` |
| routes | CLAUDE.md → references/ | `CLAUDE.md:9` |

## Hits
- SKILL.md - the only in-boundary file this entry names besides the
  references/ folder itself; a reader following this file reaches SKILL.md
  next.

## Does not hit
- README.md - a cold reader used to repos that route through their README
  might expect it here; this file's 18 lines never mention README.md at all.
  README is reached only from outside the agent's routing chain (see its
  own card).

## Open
Whether "Taurus" (the tool this file says generated it) ever diffs or
regenerates this file against a canonical version is not stated anywhere in
the territory.
