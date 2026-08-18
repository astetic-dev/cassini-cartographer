# Collisions

## "CLAUDE.md" - 2 referents

| referent | noun | status | anchor | how to tell it apart |
|---|---|---|---|---|
| the territory's own entry file | Root entry | live · entry | `CLAUDE.md:1` | at the repo root; opens with "# icm-architect", names SKILL.md and references/ |
| a blank starter for workspaces this skill builds | Templates | live · inner | `assets/templates/CLAUDE.md:1` | inside `assets/templates/`; opens with the literal placeholder text "# {Workspace name}" |

**Reader rule:** if you were just told to "open CLAUDE.md" with no path, you
almost certainly mean the root file - it is the one thing the harness
itself loads. The one under `assets/templates/` is never loaded by
anything; it exists only to be copied into a *different* workspace. Check
the first line: a real placeholder (`{Workspace name}`) means you are in
the wrong one.
