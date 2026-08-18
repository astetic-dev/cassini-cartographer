# Session history
Type:     store
Status:   live
Reach:    both
Verified: 2026-08-16 at e652c79

## Is
The list of every agent session that was ever started, kept in a file so it
survives a restart. It is what the window offers when you want to pick up
something you were doing yesterday.

## Lives at
- `src-tauri/src/lib.rs:1337` - what one entry holds
- `src-tauri/src/lib.rs:1366` - the file it lives in
- `src-tauri/src/lib.rs:1427` - an entry written when a session starts
- `src-tauri/src/lib.rs:1436` - entries marked as open again

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| an entry per start | Command surface → Session history | `src-tauri/src/lib.rs:1427` |
| the whole list, rewritten | Session history → Config store | `src-tauri/src/lib.rs:1384` |

## Hits
- `history.json` in the config folder. Every write replaces the whole list, so
  anything that reads it must expect the file to change under it.
- The window's list of earlier sessions, which is drawn from this and nothing
  else.

## Does not hit
- Session. A history entry and a running tab are two different things sharing
  one word: an entry stays after the tab is gone, and nothing about it starts
  a process. See `collisions.md`.

## Dead here
- `history_forget` - never wired - `src-tauri/src/lib.rs:1447`, registered
  `src-tauri/src/lib.rs:5513` - checked from four directions: no caller by
  name, none built at run time, none inside Rust, and the name appears in no
  saved file or manifest. Its four siblings are all called, so it reads as
  shipped. Nothing removes an entry from this list today.

## Open
Every write replaces the whole file, so what a very long list costs on a
machine that has been running Taurus for a year is a real question, and this
card cannot answer it.
