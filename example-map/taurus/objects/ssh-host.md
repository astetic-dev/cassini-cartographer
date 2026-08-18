# SSH host
Type:     object
Status:   live
Reach:    both
Verified: 2026-08-16 at e652c79

## Is
The half of Taurus that lets a tab run on another machine. It listens for
machines that knock, asks a person whether to let them in, and carries the
output of a remote agent back into a tab in this window.

## Lives at
- `src-tauri/src/sshhost.rs:1` - the connection itself
- `src-tauri/src/sshhost.rs:292` - a machine knocking, waiting for an answer
- `src-tauri/src/sshhost.rs:917` - the output of a mirrored session, sent back
- `src-tauri/src/sshhost/netgate.rs:1` - what is allowed onto the network
- `src-tauri/src/sshhost/sftp.rs:1` - files moved over the same connection

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| every ssh_ command | Command surface → SSH host | `src-tauri/src/lib.rs:5334` |
| the fingerprint and the answer given | SSH host → Peer register | `src-tauri/src/sshhost.rs:292` |
| one line per event | SSH host → ssh-audit | `src-tauri/src/sshhost.rs:173` |
| mirrored output of a remote tab | SSH host → window | `src-tauri/src/sshhost.rs:917` |

## Hits
- The peers file. A decision made once is remembered, and the next connection
  from that machine does not ask again.
- The mirrored output channel is built across several lines, so its name never
  appears next to the call that sends it. A search for the name finds the
  listener and, at a glance, no sender.

## Does not hit
- Session. A tab running on another machine is mirrored into a tab here, so it
  looks as though this opens one - it does not. Tabs are started and closed
  through the command surface like any other, whatever machine they run on.

## Open
Two commands here are reached through one call that chooses between them while
running, on where the agent came from (`src/main.js:1661`). What the far side
does differently for each is not answerable from this file.
