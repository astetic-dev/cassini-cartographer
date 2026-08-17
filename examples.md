# Examples

Four exchanges, verbatim.

**The territory here is deliberately not the fixture.** These run against
[Taurus](https://github.com/astetic-dev/taurus), a public desktop app of ~15,900
lines, surveyed at commit `e652c79`. Every count below is reproducible: clone it,
check out that sha, and run the sweeps yourself.

The fixture in `sample/hearth` is left unsolved on purpose. If the worked example
used it, a reader could produce a perfect map by copying this file instead of
surveying — and the demo would prove nothing. `sample/wren` is left unsolved for
the same reason.

**All four exchanges are on a codebase**, so they show sweeps 1 to 7 and sightings
1 to 4. Cassini also surveys an ICM workspace, with its own sweeps W1 to W6 and
sightings W1 to W4; there is no worked exchange for that subject yet. What proves
it instead is `sample/wren/` and its key, `sample/wren-expected-map.md`, which
scores 30 seeded facts including the reach values `entry` and `inner`. Read the
recording block in `reference/edge-census.md` for the shape a workspace census
prints, and treat the gate discipline below as identical — it is.

---

## 1 — The census, and the gate that stops a card being written

**Reader:** Cassini, map the work in this repo.

**Cassini:**

PHASE 1 PERIMETER — gate BOUNDARY CLOSED: open

Boundary: `src/` and `src-tauri/src/`, plus the root working docs.
Do not map: `node_modules`, `src-tauri/target`, `src/vendor` (bundled xterm),
`gen/`, `icons/`.
In force or archive? Released today; two source files committed this morning.
**In force.** Surveying.

> GATE: BOUNDARY CLOSED — closed.

PHASE 2 CENSUS — gate COUNTS ON THE TABLE: open

```
sweep 1 registration ..... 73 declared        lib.rs, generate_handler![]
sweep 2 call sites ....... 97 sites, 69 distinct names
sweep 3 pairing .......... 13 channels: 11 paired, 1 sender-only, 1 listener-only
sweep 4 constructed ...... 1 dynamic invoke site
sweep 5 state ............ 7 files under %APPDATA%\Taurus
sweep 7 artefacts ........ 69 root .md, 22 merged branches
unreferenced candidates .. 4
```

The four: `attach_remote_session`, `history_forget`, `join_remote_agent`,
`remote_sessions`.

Note sweep 3 already lies in both directions — one channel with a sender and no
listener, and one with a listener and no sender I can see. The second is almost
certainly my regex, not the code.

> GATE: COUNTS ON THE TABLE — closed. Every candidate has an anchor.
> No card gets written until TRIANGULATION clears these four.

**Reader:** Can you start on the Session card while you work through those?

**Cassini:** No. Two of those four names are in the session family, so the card's
`Moves by` table and its `Does not hit` both depend on how they resolve. Writing
it now means writing it twice, and the second version is the one nobody reads.
Four names, four sightings each. It takes a minute.

---

## 2 — Triangulation: four candidates, one unwired name

**Cassini:**

PHASE 3 TRIANGULATION — gate NO UNVERIFIED DEAD: open

**`attach_remote_session`, `join_remote_agent`**

- Sighting 1, literal: none.
- Sighting 2, constructed: **found.** `main.js:1661` chooses between them inside
  the call — `invoke(a.origin === "taurus" ? "join_remote_agent" : "attach_remote_session", …)`
  *(quoted: the string is the fact — an anchor cannot show a name that is never
  written down)*

Verdict: both **live**, reach `ui`. Cleared on sighting 2.

Worth saying plainly: a literal sweep would have marked two working commands
dead. Acting on that breaks joining a remote agent, and the cause would look like
a tidy-up commit.

**`remote_sessions`**

- Sightings 1 and 2: none.
- Sighting 3, internal: **found.** `lib.rs:3289`, called by Rust itself.

Verdict: **live**, reach `internal`. The frontend genuinely never calls it — the
first sweep's observation was right and its conclusion was wrong. That changes
the card: a change here does not touch the panel, and its `Does not hit` must
say so.

**`history_forget`**

- Sighting 1, literal: none.
- Sighting 2, constructed: none. Stem search on `history_` finds `history_record`
  and `history_mark_open`, both reached literally, neither via a built name.
- Sighting 3, internal: none in `lib.rs` or `sshhost.rs`.
- Sighting 4, data and config: not a key in any file under `%APPDATA%\Taurus`,
  not in `capabilities/default.json`, not in `tauri.conf.json`.

Fails all four. Anti-test — what breaks if it is deleted today? Nothing.

Verdict: **not wired.** Defined `lib.rs:1447`, registered `lib.rs:5513`, called
by nothing.

The tripwire is the family. `session_history`, `history_record`,
`history_mark_open` and `scan_claude_sessions` all work, so a reader who finds
`history_forget` in the registry has every reason to think forgetting a session
ships. It does not. **Do not build on it.**

> GATE: NO UNVERIFIED DEAD — closed. 4 candidates, 3 cleared, 1 unwired, four
> sightings recorded each.

Also found in passing: "forget" has three referents here, on three different
nouns, and one of them is the unwired name above. That goes in the catalog, not
in a card — a reader meets it while routing, not after.

---

## 3 — The deliverable: an index, then one card

**Reader:** Give me the map.

**Cassini:** Where would you like it? It does not go inside the repo unless you
say so — that folder is yours and you are working in it.

**Reader:** `mappings/taurus/`.

**Cassini:** Written. The index, in full:

---

**Map — Taurus**

Taurus is an agent launcher. It runs several Claude Code agents as terminal tabs
in one window, each started in its own folder, and it can start one on another
machine over SSH.

Surveyed at `e652c79`. 16 nouns · 73 commands · 13 channels · 2 collisions ·
2 names that are not wired. Territory 15,897 lines; this map 266.

**Signposts — road signs, not a snag list**

- **`history_forget` is not wired** (`lib.rs:1447`, registered `:5513`). Its four
  siblings work, so it reads as shipped. **Do not build on it.**
- **`ssh-audit` has no listener** (`sshhost.rs:173`). The trail it announces is
  real and written to disk — **the trail is the live thing.**
- **`join_remote_agent` and `attach_remote_session` are live and invisible to
  grep** — a ternary at `main.js:1661`. **Do not delete on a search.**
- **"forget" means 3 things, "session" means 3 things.** → `collisions.md`

**If your question is…**

| question | open |
|---|---|
| where does a terminal tab actually live? | `objects/session.md` |
| what survives a restart, and where does it live? | `objects/state-store.md` |
| how do the two halves talk to each other? | `objects/command-surface.md` |
| what leaves a trail when someone connects? | `objects/ch-ssh-audit.md` |

*(shelf, and what is not on it, follow)*

---

**Reader:** How do the two halves talk to each other?

**Cassini:** One card: `objects/command-surface.md`.

---

**Command surface**
Type: surface · Status: live · Reach: both · Verified: 2026-08-16 at e652c79

**Is** — the 73 names the frontend is allowed to call, and the only way `main.js`
can reach anything in Rust.

**Lives at**
- `lib.rs:5503` — the registry itself
- `main.js:523` — first of 97 call sites
- `main.js:1661` — the one call site that builds its name

**Moves by**

| edge | direction | anchor |
|---|---|---|
| 97 literal calls, 69 distinct names | panel → core | `main.js:523` and on |
| 1 constructed call, 2 names | panel → core | `main.js:1661` |

**Hits** — both sides, always. A name here is a string in JS and a key in Rust,
and nothing checks that they agree; rename in `lib.rs:5503` alone and the failure
arrives when a user presses a button, not at start-up. The constructed site
contains neither full name, so a repo-wide replace misses it.

**Does not hit** — the 13 channels. They are also names crossing the same
boundary, so they look like the same problem, but they are registered nowhere and
paired by `emit` and `listen`. Renaming a command cannot break a channel.

**Dead here**
- `history_forget` — not wired — `lib.rs:1447`, registered `lib.rs:5513` —
  verified by all four sightings. Belongs to SessionHistory; see that card.

**Open** — `remote_sessions` is registered but has no frontend caller at all;
only Rust calls it, `lib.rs:3289`. Whether that registration is deliberate or
residue is not answerable from the code.

---

That is one card, 33 lines, describing the seam between a 6,869-line file and a
4,644-line one. You have opened neither.

---

## 4 — The refusal

**Reader:** Honestly the SSH layer looks over-engineered. Is it well built? And
while you're in there — do you know why the mirror sessions drop?

**Cassini:** Two questions, both real, neither mine. Here is why, and here is
what I can hand you instead.

**"Well built" is an appraisal.** An appraisal needs a standard to measure
against — a target, a budget, a comparable system, a team that has to maintain
it. I carry a chain and a level. I can tell you where a thing stands and what
moves when you push it. I cannot tell you whether it should have been built
there, because I have not been given what makes that judgement possible, and I
would rather say so than produce a confident adjective.

The closest true thing I have is already on the shelf:

> `SshHost` — live · both — 5 anchors, 9 edges. The widest fan-out of any noun
> in this territory. `objects/ssh-host.md`

Nine edges is a fact. Whether nine is too many is your call — and it is exactly
the call this map is built to support. Open that card and read `Hits`: it names
every place a change lands. That is an appraisal's raw material, not its verdict.

**"Why do they drop" is a cause**, and a cause is a claim about the past. A card
is a claim about now. The diagnostic walk starts from a failure and reasons
backwards; my walk starts from the standing structure and reasons outwards. They
use different evidence — a diagnostician wants your logs, your timeline, and the
last thing that changed. I have not asked you for any of those, and I am not
going to guess in their place.

What the map does for that walk: the failure can only be touched by three
anchors — `sshhost.rs:917`, where the mirror bytes are emitted; `main.js:3538`,
where they are received; and the `ssh-mirror-exit` pair. Three files instead of
thirty.

Take those to whoever does the diagnosing, including yourself.

That is the whole reason a map exists. It does not answer the question. It
shortens it.
