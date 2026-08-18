# Brief -- map taurus

## What is this for

A viewer who has never opened Taurus should be able to say, in ninety seconds,
what it is, what happens when a tab is started, where the state lives, and which
one thing to be careful of -- from the map alone, without opening the code.

## Who is watching

Somebody about to change something in a 15,897-line codebase they do not hold in
their head: the next maintainer, or a model opening the tree cold. They know
what a terminal and an SSH connection are. Afterwards they should open
`catalog.md`, then exactly one card.

## What it must say

Every line is already a claim on a card in `example-map/taurus/`:

- 73 command names registered in `src-tauri/src/lib.rs:5503`, 69 of them called
  across 97 sites from `src/main.js`. Nothing checks that the two sides agree.
- A tab is a real console process on the Rust side (`lib.rs:1923`) and a screen
  buffer in the page; output comes back on `pty-output` / `pty-exit`
  (`main.js:3466`).
- Seven files and two folders outside the program hold the state (`lib.rs:61`).
  They outlive the code that wrote them.
- `history_forget` is registered at `lib.rs:5513`, defined at `:1447`, called by
  nothing. `ssh-audit` is written to a log at `sshhost.rs:169` and announced at
  `:173` with nothing listening. "session" names four things, "forget" three.

## What it must not do

No adjectives about how good the code is. No causes -- why a thing is not wired
is not answered. No number that is not on a card.
