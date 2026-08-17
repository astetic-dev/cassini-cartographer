# 1.3 — zones keep their own sensor

Until now a sensor belonged to the boiler and every zone read the same number,
which is fine in a flat and wrong in a house. From 1.3 a zone owns its sensor.

**State shape changed.** `zones.json` went from a list to a map keyed by zone
name, and `probe` became `sensor`. The file version went from 2 to 3. The old
file is left beside the new one as `zones.old.json` so a bad upgrade can be read
by hand; nothing reads it.

**Pairing moved into the panel.** The Pair sensor button is new. Unpairing is the
Forget button next to it.

Shipped 11 March. Superseded by 1.4, which added the weekly schedule.
