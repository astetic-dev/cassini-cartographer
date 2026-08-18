# Collisions

Two words in this territory name more than one thing. Both are used in the
window, in the machine half, and in the files on disk, so the word alone never
tells you which one you are holding.

## "session" - 4 referents

| referent | what it is | anchor | how to tell it apart |
|---|---|---|---|
| a running tab | a console process with a screen buffer, alive right now | `src-tauri/src/lib.rs:1923` | it has a process behind it; close it and something stops |
| a saved tab | the same tab written down so the next start can reopen it | `src-tauri/src/lib.rs:1272` | it is a line in `sessions.json`; nothing is running |
| a session on another machine | work happening on a remote host, mirrored into a tab here | `src-tauri/src/lib.rs:2936` | it carries a host, and its output arrives over a connection |
| the agent's own session id | a UUID Taurus chooses and hands to the agent, which the agent uses to name its own transcript file | `src-tauri/src/lib.rs:1680` | it is a UUID, not a tab id, and it appears in a file path |

**Reader rule:** *the tab* and *the saved tab* are the pair that catches people.
A tab id is chosen in the window and lives as long as the window does; the UUID
is what survives, and it is the one thing that ties a tab, its history entry and
the agent's own transcript together.

## "forget" - 3 referents

| referent | what it is | anchor | how to tell it apart |
|---|---|---|---|
| forget a history entry | removes a session from the list of work ever started | `src-tauri/src/lib.rs:1447` | it is the one that is never called - see the Session history card |
| forget an id | drops an id from a short-lived list held in memory | `src-tauri/src/lib.rs:1997` | it takes an id, returns nothing, and touches no file |
| forget a peer | removes a machine's fingerprint, so it must ask again | `src-tauri/src/lib.rs:5368` | it takes a fingerprint and rewrites `peers.json` |

**Reader rule:** two of the three are reachable from the window and the third
is not reachable at all. If somebody says "the forget command", ask which of
the three files they mean before you touch anything.
