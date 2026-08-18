# Session
Type:     object
Status:   live
Reach:    both
Verified: 2026-08-16 at e652c79

## Is
One terminal tab, and it exists in two places at once: a real console process
owned by Rust, and a tab with a screen buffer in the window. What you type goes
down one way, what the program prints comes back the other.

## Lives at
- `src-tauri/src/lib.rs:1923` - the process, its reader and its writer
- `src-tauri/src/lib.rs:3460` - started here, under an id the window chose
- `src/main.js:2899` - the window asking for one, with its folder and agent
- `src/main.js:3466` - the window drawing what comes back

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| output and exit | Session → window | `src/main.js:3466` |
| keystrokes and pasted text | window → Session | `src/main.js:2734` |
| the open tabs, saved for the next start | Session → Config store | `src-tauri/src/lib.rs:1303` |

## Hits
- The window's tab strip. The id is chosen in the window and handed down, so
  the two halves agree only for as long as that id is passed unchanged.
- `sessions.json` in the config folder - what is written there is what comes
  back after a restart, and it outlives any rewrite of this code.

## Does not hit
- Session history. A tab and a history entry are different things that both
  call themselves a session: closing a tab does not remove its history entry,
  and an entry has no process behind it. See `collisions.md`.

## Open
Whether a tab whose process has already exited can be told apart from one that
was never started, from the saved file alone, is not answerable here.
