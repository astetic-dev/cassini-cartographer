---
title: "Taurus, mapped"
slug: map-taurus
lang: en
intent: "The standard nine-scene explainer from Cassini's film/film.md, on a codebase: three stations (the window -> the command surface -> what survives a restart), one step per rail scene, every spoken line already a claim on a card in example-map/taurus/. Shipped as one of two worked examples beside the maps themselves."
audience: "Somebody about to change something in a codebase they do not hold in their head. Technical, plain register."
style: technical-diagram
brand: taurus-house
preset: diagram-dark
duration_target_s: 90
fps: 30
autonomy: A
budget_eur: 0
budget_video_seconds: 0
deadline_minutes: 45
source_refs: ["example-map/taurus/catalog.md", "example-map/taurus/objects/command-surface.md", "example-map/taurus/objects/session.md", "example-map/taurus/objects/config-store.md", "example-map/taurus/objects/session-history.md", "example-map/taurus/objects/ch-ssh-audit.md", "example-map/taurus/collisions.md"]
created: "2026-08-19"
board_version: 1
---

# Scenes

## s01-title - What it is
template: title-card / dur_s: 7 / data: data/s01-title.json
transition_in: none / transition_out: fade / motion: med / text_critical: true
qc_focus: [legibility] / vo_target_s: 6.3
#### NOTE
catalog.md's opening sentence, unchanged.
#### VO
Taurus runs several Claude Code agents as terminal tabs in one window.
#### ON SCREEN
- One window, several agents

## s02-what - What it does
template: takeaway-split / dur_s: 10 / data: data/s02-what.json
transition_in: fade / transition_out: cut / motion: med / text_critical: true
qc_focus: [legibility, accuracy] / vo_target_s: 9
#### NOTE
From the description paragraphs in catalog.md and the Session card.
#### VO
Every tab is a real console process, started in a folder you pick, and it keeps running while you look away.
#### ON SCREEN
- A tab is a process
- Two halves
- State is files

## s03-names - The window asks by name
template: flow-rails / dur_s: 12 / data: data/s03-names.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
Command surface card: 73 registered at lib.rs:5503, 97 sites and 69 distinct names from main.js:523.
#### VO
The window holds nothing that matters. It asks the machine half for work by name, and there are seventy-three of those names.
#### ON SCREEN
- 73 names, the only way across

## s04-tab - A tab is two things at once
template: flow-rails / dur_s: 12 / data: data/s04-tab.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
Session card: the process at lib.rs:1923, started at :3460 under an id the window chose, main.js:2899.
#### VO
Starting a tab makes a real console process on the machine, and a screen buffer in the page. One tab, two halves.
#### ON SCREEN
- 2 places one tab lives

## s05-back - What comes back
template: flow-rails / dur_s: 12 / data: data/s05-back.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
Session card: output and exit arrive on two channels the page listens for, main.js:3466.
#### VO
What the agent prints comes back on its own channel, and the page draws it. Thirteen channels carry the two halves.
#### ON SCREEN
- 13 channels between the halves

## s06-disk - What survives a restart
template: flow-rails / dur_s: 12 / data: data/s06-disk.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
Config store card: lib.rs:61, seven files and two folders; sessions.json written whole at :1303.
#### VO
The open tabs and the history are written to seven plain files outside the program. They outlive any rewrite of the code.
#### ON SCREEN
- 7 files, written whole

## s07-seam - What holds it together
template: takeaway-split / dur_s: 10 / data: data/s07-seam.json
transition_in: fade / transition_out: cut / motion: med / text_critical: true
qc_focus: [legibility, accuracy] / vo_target_s: 9
#### NOTE
Command surface card, Hits: a name is a string on one side and a key on the other, and nothing checks that they agree.
#### VO
Nothing checks that the two sides agree on a name. Rename one alone and it fails at a button press.
#### ON SCREEN
- One list, 73 names
- Nothing checks them
- 97 call sites

## s08-signs - Three road signs
template: takeaway-split / dur_s: 10 / data: data/s08-signs.json
transition_in: cut / transition_out: fade / motion: med / text_critical: true
qc_focus: [legibility, accuracy] / vo_target_s: 9
#### NOTE
history_forget lib.rs:1447 registered :5513; ssh-audit sshhost.rs:169-173; collisions.md counts session at four and forget at three.
#### VO
Three road signs: a command wired to nothing, a trail nobody listens for, and one word that names four things.
#### ON SCREEN
- history_forget
- ssh-audit
- "session"

## s09-outro - How to read it
template: outro-refs / dur_s: 6 / data: data/s09-outro.json
transition_in: fade / transition_out: none / motion: low / text_critical: true
qc_focus: [legibility] / vo_target_s: 5.4
#### NOTE
rules.md: the catalog routes, one card answers. Cards are opened one at a time.
#### VO
Open the catalog, then one card. That is the whole rule.
#### ON SCREEN
- catalog.md, then one card
