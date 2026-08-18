# SKILL.md (the method)
Type:     object
Status:   live
Reach:    entry
Verified: 2026-08-14 at b20fb45

## Is
The method file: ten invariants, Build mode, Restructure mode, the walk
test, and the routing table into `references/` and `assets/templates/`.
The walk test is what every result is checked against - an agent with no
memory must orient, act and report status from the files alone.
Its YAML frontmatter (`name`, `description`) is also what the Claude Code
harness scans to decide when to trigger this skill at all.

## Lives at
- `SKILL.md:1-4` - frontmatter, harness-facing trigger description
- `SKILL.md:14-27` - the ten invariants
- `SKILL.md:85-97` - the walk test, the check on any result
- `SKILL.md:105-110` - the References list, the routing table proper

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| routes | SKILL.md → references/core.md | `SKILL.md:107` |
| routes | SKILL.md → references/forms.md | `SKILL.md:47`, `SKILL.md:108` |
| routes | SKILL.md → references/system-map.md | `SKILL.md:33`, `56`, `95`, `109` |
| routes | SKILL.md → assets/templates/ (8 files, bare-name list) | `SKILL.md:110` |
| routes | SKILL.md → assets/templates/stage-CONTEXT.md | `SKILL.md:21` |
| declares | SKILL.md → Claude Code harness (skill discovery) | `SKILL.md:1-4` |

## Hits
- every reference file and every template - this is the only file in the
  territory that names all three references files and all eight templates
  in one place.

## Does not hit
- README.md - never named here either; a reader assuming the method file
  also covers installation will not find it, that is README's job and it
  is reached only via GitHub, not via this file.

## Open
Nothing.
