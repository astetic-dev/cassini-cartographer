# Peer register
Type:     store
Status:   live
Reach:    both
Verified: 2026-08-16 at e652c79

## Is
The list of machines that are allowed to knock, each remembered by its
fingerprint together with the answer a person once gave it. It is what makes
the consent question happen once instead of every time.

## Lives at
- `src-tauri/src/sshhost.rs:48` - what the list is for
- `src-tauri/src/sshhost.rs:75` - the file it lives in
- `src-tauri/src/sshhost.rs:122` - the list, rewritten whole
- `src-tauri/src/lib.rs:5339` - read, set and forgotten from the window

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| read, set, forget | Command surface → Peer register | `src-tauri/src/lib.rs:5339` |
| the fingerprint and the answer given | SSH host → Peer register | `src-tauri/src/sshhost.rs:292` |
| the list, rewritten whole | Peer register → Config store | `src-tauri/src/sshhost.rs:122` |

## Hits
- Every machine that has connected before. Forgetting one here does not close
  a connection that is already open; it decides what happens the next time.
- `peers.json`, which is rewritten in full on every change.

## Does not hit
- Session history. Both remember something after the fact, and both are lists
  in the same folder, but a peer is a machine and a history entry is a piece of
  work; forgetting one has nothing to do with the other. See `collisions.md`.

## Open
Whether a fingerprint that changes on the far machine appears as a new peer or
as the same one is not answerable from this file alone.
