# Answer key — `sample/hearth`

What a correct map of Hearth contains. Score a run against this.

The fixture is **9 files, 266 lines, 183 of them non-blank**. Line budgets in this
folder are always counted **non-blank**, so a passing card is 40 non-blank lines.

**Shape bar.** A *first run* delivers the catalog, `collisions.md`, and only the
cards the question table routes to. That comes in **under 100 non-blank lines**.
A *fully expanded* map — all 8 cards — runs to roughly **325**, which is larger
than Hearth itself. That is expected on a territory this small and is exactly why
cards are drawn lazily; the ratio only turns in the map's favour as the territory
grows. Score the first run against 100; score an expanded map on its cards, not
its length.

---

## Scoreboard — 29 seeded facts

```
Cards named correctly ....................... 8
Edges named correctly ...................... 14
The one unwired name ........................ 1   schedule_forget
Names that look dead and are not ............ 2   boiler dispatch; zone_list
Leftovers identified ........................ 3
Collision identified ........................ 1   "forget"
                                            ----
                                             29
```

**Counting edges.** One edge is one ordered pair of nouns plus one mechanism, per
`reference/edge-census.md`. Five call sites to the same noun are one edge; a read
and a write to the same store are two. Report sites separately if you like — the
edge count is not the site count.

### Fail conditions — independent of score

| condition | verdict |
|---|---|
| Any live name marked as not wired | **FAIL** — deleting working code is the expensive error, and preventing it is the whole job |
| Any code fence in `catalog.md` or in any card | **FAIL** — that is photocopying |
| `catalog.md` over 60 non-blank lines of **routing** content — the shelf, the question table, what is not on the shelf | **FAIL** (the description, the survey record and a staleness banner are outside the budget) |
| `catalog.md` opening with counts, a path, or the word *map* instead of the territory's name and a plain description | **FAIL** — the opening is what most readers read |
| Any method word on a deliverable — sweep, sighting, gate, triangulation, a W-number, *ghost*, *leftover* | **FAIL** per occurrence |
| A signpost that is a null result of the survey, a remark on a naming choice, or a live thing described by what does not reach it | **FAIL** per occurrence — that is a review, not a map |
| The unwired name given without its origin document | **HALF** |
| A card with no `Does not hit` where one exists | **HALF** per card |

---

## The 8 cards

| card | type | status |
|---|---|---|
| Zone | object | live · both |
| Sensor | object | live · both |
| Schedule | object | live · both — **carries the unwired name** |
| Boiler | object | live · both |
| Command surface | surface | live · both — 9 names, `core.py:96` |
| Hearth state | store | live · internal — `state/*.json` via `store.py:14` |
| `reading-tick` | channel | live · both — `core.py:39` → `ui.py:47` |
| `boiler-state` | channel | live · both — `core.py:87`, `:91` → `ui.py:48` |

Splitting Zone and Sensor is correct; merging them is acceptable if the card says
why. Folding `state/*.json` into the Zone card instead of giving it its own
`store` card costs the Hearth state card and the four edges that land on it.

## The 14 edges

| # | edge | mechanism | anchor |
|---|---|---|---|
| 1 | Command surface → Zone | calls | `ui.py:15` |
| 2 | Command surface → Sensor | calls | `ui.py:19`, `:24` |
| 3 | Command surface → Schedule | calls | `ui.py:28`, `:32` |
| 4 | Command surface → Boiler | calls **(constructed)** | `ui.py:36` |
| 5 | Schedule → Zone | calls | `core.py:70` |
| 6 | Sensor → Zone | writes | `core.py:37` |
| 7 | Zone → Hearth state | reads | `core.py:21`, `:25` |
| 8 | Zone → Hearth state | writes | `core.py:27`, `:30` |
| 9 | Sensor → Hearth state | reads | `core.py:36`, `:44` |
| 10 | Sensor → Hearth state | writes | `core.py:38`, `:48` |
| 11 | Schedule → Hearth state | reads | `core.py:54`, `:58`, `:65`, `:69` |
| 12 | Schedule → Hearth state | writes | `core.py:60`, `:74` |
| 13 | Sensor → `reading-tick` | emits | `core.py:39` |
| 14 | Boiler → `boiler-state` | emits | `core.py:87`, `:91` |

**Edges 4 and 5 are the ones that matter.** A run that finds the other twelve and
misses these has run one sweep and stopped. Score at least 11 of 14, and **both
4 and 5 must be present** regardless of the total.

---

## Trap 1 — the constructed name

A literal sweep of `call("…")` in `ui.py` finds **5** distinct names against **9**
registered, so the naive candidate list is four: `zone_list`, `schedule_forget`,
`boiler_on`, `boiler_off`.

`boiler_on` and `boiler_off` are **live**. The only call site builds the name at
run time, `ui.py:36`, so neither full name appears anywhere as a string.

**Expected reasoning, not just the verdict:** the run must say it searched the
stem (`boiler_`) or searched for constructed dispatch, and must cite `ui.py:36`.
A run that marks them live without saying how it cleared them scores the fact and
fails the discipline — note that in the receipt.

## Trap 2 — the internal-only caller

`zone_list` is **live**, reached from `core.py:70` inside `schedule_apply`. The
panel never calls it.

Correct status is `live` with the noun's Reach unchanged; the internal-only reach
belongs on the `Moves by` row, per `reference/card-types.md`. The correct
`Does not hit` says a change to it **does not touch the panel**.

Marking `zone_list` unwired triggers the FAIL condition above.

## The unwired name — `schedule_forget`

Defined `core.py:77`, registered `core.py:103`, **zero callers** of any kind: no
literal, no constructed, no internal, no data.

Its siblings — `schedule_get`, `schedule_set`, `schedule_apply` — all work, which
is what makes it a tripwire: the family works, so the member looks like it works.

**Its origin is on disk.** `docs/PLAN-zone-groups.md` proposes zone groups and a
way to drop one, working name **forget**. The plan was parked; only the function
survived. A map that names it without naming that document scores HALF — the
document is the difference between *do not build on this* and *somebody wanted
this and stopped*.

## The collision — "forget"

| referent | noun | status | anchor |
|---|---|---|---|
| `schedule_forget` | Schedule | **not wired** | `core.py:77`, registered `:103` |
| `sensor_forget` | Sensor | live · ui | `core.py:42`; button `ui.py:24`, label `ui.py:8` |
| `forget(zone_id)` | Hearth state | live · internal | `store.py:17`; caller `core.py:27` |

Three referents on three nouns. **Counting the UI label `LABELS["forget"]`
(`ui.py:8`) as a fourth referent is also correct** — it is the caption a reader
meets first — and a run that reports four with that reasoning scores full marks.

The warning must appear in the catalog above the shelf, with the table in
`collisions.md`. A reader who greps `forget` finds the working button first, and
the working button vouches for the unwired command.

Required reader rule, in substance: *the button says Forget and means the sensor;
ask which shelf before opening a card.*

## The 3 leftovers

| leftover | why it is not live |
|---|---|
| `state/zones.old.json` | v2 shape, superseded at 1.3. `store.read` builds `<name>.json` from a caller-supplied name and no caller passes `zones.old` |
| `docs/RELEASE-1.3.md` | notes for a version already shipped and superseded by 1.4 |
| `docs/PLAN-zone-groups.md` | a plan never built. **Also the origin of the unwired name** |

Deliberately split across `state/` and `docs/`. A map reporting "leftovers live in
docs/" has generalised from half the evidence.

---

## Quality checks — not scored, but note them in the receipt

- **The honest gap.** `schedule_apply` (`core.py:63`) is live but its caller is
  the tick loop, which is **outside the fixture**, and it is not on the command
  surface. A good map puts this in `## Open`. A map that claims to know what calls
  it is inventing; a map that calls it dead has confused *outside the boundary*
  with *nothing calls it*.
- **`store.read` / `store.write` are not commands.** They are internal to Hearth
  state. Listing them on the command surface confuses a helper with an interface.
- **`LABELS` (`ui.py:8`) is not a noun.** It is a string table.
- **Did the catalog route?** Put these three to it and check each lands on exactly
  one card: *"what happens if I rename a command?"* → Command surface. *"where do
  the temperatures live?"* → Hearth state. *"I found `forget` and cannot find its
  caller"* → `collisions.md`.
