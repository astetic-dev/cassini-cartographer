# Hearth

A home heating panel. Four zones, one boiler, a weekly schedule.

Version 1.4, in service since March. Runs on the wall tablet in the hallway and
on the phone app; both talk to the same `core`.

## Layout

- `ui.py` — the panel. Buttons call into core by name; two channels come back.
- `core.py` — zones, sensors, schedule, boiler. Owns the command registry.
- `store.py` — reads and writes the json under `state/`.
- `state/` — live state. Survives a restart.
- `docs/` — release notes and planning.

## Running it

The panel imports `core`, and `core` imports `store`. There is no build step and
no configuration; the state files are the configuration.

## Adding a command

Write the function in `core.py`, then add it to `COMMANDS`. If it is not in
`COMMANDS`, `call()` cannot reach it and the panel cannot use it.
