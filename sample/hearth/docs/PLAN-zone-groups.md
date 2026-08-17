# Plan — zone groups

**Status: not built.** Written before 1.4, parked when the schedule turned out
to cover most of what this was for.

## The idea

Zones would join a named group — "upstairs", "day rooms" — and the schedule
would address a group instead of repeating a block per zone.

## What it needed

- A `groups` map in `zones.json`, version 4.
- `group_set` and `group_list` on the command surface.
- A way to drop a group once it is no longer wanted, so the panel does not
  accumulate dead groups. Working name: **forget**.
- The schedule would then apply per group, which is why `schedule_apply` was
  going to need to know about groups at all.

## Why it stopped

The weekly schedule shipped in 1.4 and covered the repetition problem on its
own. Groups would still be nice for the upstairs rooms. Nobody has asked twice.

Nothing from this plan is wired up.
