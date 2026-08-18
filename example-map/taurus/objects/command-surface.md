# Command surface
Type:     surface
Status:   live
Reach:    both
Verified: 2026-08-16 at e652c79

## Is
The 73 names the window is allowed to call, and the only way anything on screen
reaches the machine underneath. A name here is a string in JavaScript and a key
in Rust, and nothing checks that the two agree.

## Lives at
- `src-tauri/src/lib.rs:5503` - the registry, all 73 names
- `src/main.js:523` - the first of 97 call sites
- `src/main.js:1661` - the one call that builds its name while running

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| 97 calls, 69 distinct names | window → machine | `src/main.js:523` and on |
| 1 call, 2 names, chosen at run time | window → machine | `src/main.js:1661` |
| starts, feeds and closes a tab | surface → Session | `src-tauri/src/lib.rs:3460` |
| records and reopens history entries | surface → Session history | `src-tauri/src/lib.rs:1427` |
| every ssh_ command | surface → SSH host | `src-tauri/src/lib.rs:5334` |
| reads, sets and forgets peers | surface → Peer register | `src-tauri/src/lib.rs:5339` |

## Hits
- Both sides, always. Rename a name in the registry alone and the failure
  arrives when somebody presses a button, not when the program starts.
- The call at `src/main.js:1661` contains neither full name as a string, so a
  search-and-replace across the tree misses it.

## Does not hit
- The 13 channels. They also carry names across the same boundary, so they look
  like the same problem, but they are registered nowhere and pair by name at
  both ends. Renaming a command cannot break a channel.

## Dead here
- `history_forget` - never wired - `src-tauri/src/lib.rs:1447`, registered
  `:5513` - checked from four directions. Belongs to Session history; the card
  for that noun says what a reader should do about it.

## Open
`remote_sessions` is registered and called only from Rust
(`src-tauri/src/lib.rs:3289`). Whether the registration is deliberate or
residue cannot be answered from the code.
