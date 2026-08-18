# taurus

*Arjen Stet · MIT*

Taurus is a desktop application for running several Claude Code agents at the
same time. Each agent gets a terminal tab in one window, and every tab is
started in a folder you pick, so two agents working on two projects never see
each other's files.

Opening it gives you a window with a tab strip. Starting a tab launches a real
console process on the machine and hands it to an agent; you type into the tab
and what the agent prints comes back into it. Tabs keep running while you look
at another one, and the window comes back after a restart with the same folders
open, because the open tabs and the history of everything ever started are
written to a folder of plain files. A tab can also be started on a different
machine over SSH — then the process is there and the tab is here, the output is
mirrored across, and the machine that knocked has to be let in by a person
before anything happens. There is voice input, a dropzone for files, and a
history you can pick work up from.

Underneath it is two halves speaking a fixed vocabulary. The window is a web
page; everything with a process behind it — terminals, files, SSH — is a Rust
program under it. The page asks for work by name and draws what comes back, and
those 73 names are the only way across. That seam is what this map is arranged
around: it is the one place where a change on one side cannot be seen by the
other, and where the failure arrives when somebody presses a button rather than
when the program starts.

The state is the other half of the shape. Nothing important is kept in the
window: seven files and two folders under `%APPDATA%\Taurus` hold the projects,
the open tabs, the history, the machines allowed to connect and the trail of
what they did. Those files outlive any rewrite of the code that wrote them,
which makes them the part of this territory a change has to be most careful
with.

<div class="callout">
<span class="label">Removing a session from the history is a command that goes nowhere.</span>
`history_forget` sits in the command list next to four siblings that all work
(`src-tauri/src/lib.rs:1447`) and nothing calls it. It reads as shipped, so
anything built on top of it will look wired and do nothing.

</div>

<div class="callout">
<span class="label">Two commands carry a name that is put together while the program runs.</span>
`join_remote_agent` and `attach_remote_session` are chosen between inside the
call itself (`src/main.js:1661`), so neither name appears next to a caller
anywhere. Both run every time somebody joins a remote agent, and a rename that
goes through the tree by name will pass them by.
</div>

<div class="callout">
<span class="label">The trail of an SSH connection is on disk, not on the channel that announces it.</span>
Every event is appended to a log in the config folder and announced at the same
moment on a channel called `ssh-audit` (`src-tauri/src/sshhost.rs:169-173`).
Nothing in the window listens for it. Read the log — anything wired to that
channel receives nothing while the events keep arriving on disk.
</div>

<div class="callout">
<span class="label">"session" names four different things here, and "forget" names three.</span>
A running tab, a saved tab, work on a remote machine and the agent's own id are
all called a session; three unrelated functions are all called forget. Which one
you are holding decides what a change touches → `collisions.md`.
</div>

## What is here

| what | it is | reached from | card |
|---|---|---|---|
| Command surface | the 73 names the window may call | both sides | [objects/command-surface.md](objects/command-surface.md) |
| Session | one terminal tab, in two halves at once | both sides | [objects/session.md](objects/session.md) |
| Session history | every session ever started, kept in a file | both sides | [objects/session-history.md](objects/session-history.md) |
| Config store | the folder that survives a restart | inside only | [objects/config-store.md](objects/config-store.md) |
| SSH host | tabs that run on another machine | both sides | [objects/ssh-host.md](objects/ssh-host.md) |
| ssh-audit | the trail of a connection | inside only | [objects/ch-ssh-audit.md](objects/ch-ssh-audit.md) |
| Peer register | machines allowed to knock, and the answer given | both sides | [objects/peer-register.md](objects/peer-register.md) |
| The window | everything on screen | the interface | [objects/window.md](objects/window.md) |
| Projects | the folders you work in | both sides | not drawn yet |
| Hosts | the machines you can reach out to | both sides | not drawn yet |
| Branding | name, colours and logo, resolved from three places | both sides | not drawn yet |
| Discovery | finding agents on the local network | both sides | not drawn yet |
| Netgate | what is allowed onto the network | inside only | not drawn yet |
| File transfer | files moved over an open connection | both sides | not drawn yet |
| Speech to text | hold a key, speak, get text in the tab | both sides | not drawn yet |
| Capability manifest | what the window is permitted to do at all | fixed before start | not drawn yet |

## If your question is…

| question | open |
|---|---|
| Where does a terminal tab actually live? | [objects/session.md](objects/session.md) |
| How do the two halves talk to each other? | [objects/command-surface.md](objects/command-surface.md) |
| What is on disk after I close the window? | [objects/config-store.md](objects/config-store.md) |
| Can I remove a session from the history? | [objects/session-history.md](objects/session-history.md) |
| What happens when another machine connects? | [objects/ssh-host.md](objects/ssh-host.md) |
| Who decides whether that machine is let in? | [objects/peer-register.md](objects/peer-register.md) |
| What is written down when someone connects? | [objects/ch-ssh-audit.md](objects/ch-ssh-audit.md) |
| What do I actually see on screen? | [objects/window.md](objects/window.md) |

## Not on the shelf

`src/vendor/` and `src/fonts/` — the terminal component and the typefaces, both
brought in whole from elsewhere. `src-tauri/icons/` — 40 image files. The
release notes, issues and status documents at the root: 19 documents that record
what was decided, not things a change can reach. And everything under
`src-tauri/target/` and `node_modules/`, which is built rather than written.

<div class="record">

**How this was walked.** 15,897 lines across ten files — the window
(`src/`) and the machine half (`src-tauri/src/`) — on 2026-08-16, at commit
`e652c79`. The command list holds 73 names; the window calls 69 distinct ones
across 97 places. Thirteen named channels carry events between the halves:
eleven have both ends, one is sent and nothing receives it, and one has its
sending line written across two lines, so the name does not sit beside the call
that sends it. Four names that nothing appeared to call were each checked from
four directions: three are in use — two of them called by a name built while the
program runs, one called only from inside Rust — and one, `history_forget`, is
not wired. Two words that name more
than one thing were counted, in `collisions.md`.

**Sixteen things are on the shelf and eight have cards.** On a territory this
size the first walk delivers the index, the warnings, and a card for everything
the questions route to; the other eight are drawn on request. Nothing about them
is unknown — they are on the shelf with what they are and where they are reached
from.

**Three questions, three cards.** *"Where does a tab live?"* → the Session card,
and no other. *"What is left on my disk?"* → the Config store card, and no
other. *"Can I clear something out of the history?"* → the Session history card,
and no other — where the answer is no.

</div>
