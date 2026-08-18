# ssh-audit
Type:     channel
Status:   live
Reach:    internal
Verified: 2026-08-16 at e652c79

## Is
The trail of an SSH connection: who knocked, what was decided, what happened.
Every event is written to a log file in the config folder, and announced at the
same moment on a channel of this name.

## Lives at
- `src-tauri/src/sshhost.rs:169` - the line appended to the log
- `src-tauri/src/sshhost.rs:173` - the same event, announced

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| one line appended per event | ssh-audit → Config store | `src-tauri/src/sshhost.rs:169` |
| the same event, sent to the window | ssh-audit → window | nothing listens |

## Hits
- The log file under the config folder, which is the thing that survives. It is
  appended to, never rewritten, so it is the one file here that grows without
  limit.

## Does not hit
- Session history. Both are records kept in the same folder and both are read
  after the fact, but this one is appended to and never rewritten, and nothing
  in it refers to a session at all - it is about machines, not work.

## Dead here
- The announcement itself - never received - `src-tauri/src/sshhost.rs:173` -
  checked from four directions: the window listens for twelve channels and this
  is not one of them. **Read the log, not the channel.** Anything built to
  listen for this receives nothing while the events keep arriving on disk.

## Open
Whether the announcement was written for a screen that was never built, or for
one that was removed, is a question about the past and is not answered here.
