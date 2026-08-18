---
title: "icm-architect, mapped"
slug: map-icm-architect
lang: en
intent: "The standard nine-scene explainer from Cassini's film/film.md, on a workspace: three stations (a way of working you describe -> icm-architect -> a folder an agent can run), one step per rail scene, every spoken line already a claim on a card in example-map/icm-architect/. The companion to map-taurus: same shape, other subject."
audience: "Somebody deciding whether to point this at their own folder. Technical, plain register."
style: technical-diagram
brand: taurus-house
preset: diagram-dark
duration_target_s: 90
fps: 30
autonomy: A
budget_eur: 0
budget_video_seconds: 0
deadline_minutes: 45
source_refs: ["example-map/icm-architect/catalog.md", "example-map/icm-architect/objects/root-claude-md.md", "example-map/icm-architect/objects/skill-md.md", "example-map/icm-architect/objects/references-forms-md.md", "example-map/icm-architect/objects/references-core-md.md", "example-map/icm-architect/objects/templates.md", "example-map/icm-architect/collisions.md"]
created: "2026-08-19"
board_version: 1
---

# Scenes

## s01-title - What it is
template: title-card / dur_s: 7 / data: data/s01-title.json
transition_in: none / transition_out: fade / motion: med / text_critical: true
qc_focus: [legibility] / vo_target_s: 6.3
#### NOTE
catalog.md's opening: a skill, written down, that nothing executes.
#### VO
icm-architect turns a way of working into a folder an agent can run.
#### ON SCREEN
- A method, written down

## s02-what - Two directions
template: takeaway-split / dur_s: 10 / data: data/s02-what.json
transition_in: fade / transition_out: cut / motion: med / text_critical: true
qc_focus: [legibility, accuracy] / vo_target_s: 9
#### NOTE
catalog.md description: build from what you describe, or restructure what exists.
#### VO
It goes in two directions: it builds a workspace from what you describe, or restructures one you already have.
#### ON SCREEN
- Build
- Restructure
- Four documents

## s03-door - The door
template: flow-rails / dur_s: 12 / data: data/s03-door.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
Root entry card: 18 lines, names SKILL.md at CLAUDE.md:8 and references/ at :9.
#### VO
A cold agent opens the root file. Eighteen lines: what this is, and where the method lives.
#### ON SCREEN
- 18 lines, then you are in the method

## s04-form - Pick the form
template: flow-rails / dur_s: 12 / data: data/s04-form.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
forms.md card: the Selection table matches the repeating unit of work to one of six forms, references/forms.md:7-18.
#### VO
The method asks one question first: what is the repeating unit of work? The answer picks one of six forms.
#### ON SCREEN
- 6 forms, one skeleton

## s05-contract - Write the contracts
template: flow-rails / dur_s: 12 / data: data/s05-contract.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
core.md card: five principles, the five-layer hierarchy, the stage contract format, token discipline.
#### VO
Every working folder gets a contract: what it reads, what it does, what it writes, and what a person checks.
#### ON SCREEN
- 5 principles behind every contract

## s06-copy - Copy, never start blank
template: flow-rails / dur_s: 12 / data: data/s06-copy.json
transition_in: cut / transition_out: cut / motion: high / text_critical: true
qc_focus: [legibility, accuracy, layout-occlusion] / vo_target_s: 10.8
#### NOTE
Templates card: eight blank starters, copied out rather than edited, per invariant 10 at SKILL.md:27.
#### VO
New work begins by copying one of eight blank starters. That is the method's own tenth rule.
#### ON SCREEN
- 8 starters, copied out

## s07-walk - The test everything has to pass
template: takeaway-split / dur_s: 10 / data: data/s07-walk.json
transition_in: fade / transition_out: cut / motion: med / text_critical: true
qc_focus: [legibility, accuracy] / vo_target_s: 9
#### NOTE
SKILL.md card: the walk test, SKILL.md:85-97 - orient, act and report status from the files alone.
#### VO
One test decides any of it: an agent with no memory must orient, act and report status from the files alone.
#### ON SCREEN
- Orient
- Act
- Report status

## s08-signs - Two road signs
template: takeaway-split / dur_s: 10 / data: data/s08-signs.json
transition_in: cut / transition_out: fade / motion: med / text_critical: true
qc_focus: [legibility, accuracy] / vo_target_s: 9
#### NOTE
collisions.md: two files named CLAUDE.md. Root entry card: finished work goes to blueprints/, CLAUDE.md:11.
#### VO
Two road signs. Two files here are called CLAUDE.md, only one is the door. And finished work is kept elsewhere.
#### ON SCREEN
- Two files, one name
- Work goes to blueprints/

## s09-outro - How to read it
template: outro-refs / dur_s: 6 / data: data/s09-outro.json
transition_in: fade / transition_out: none / motion: low / text_critical: true
qc_focus: [legibility] / vo_target_s: 5.4
#### NOTE
rules.md: the catalog routes, one card answers.
#### VO
Open the catalog, then one card. That is the whole rule.
#### ON SCREEN
- catalog.md, then one card
