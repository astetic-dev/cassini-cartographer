"""Hearth state - json under state/, next to this module. v1.4"""

import json
import pathlib

_DIR = pathlib.Path(__file__).parent / "state"


def read(name):
    return json.loads((_DIR / f"{name}.json").read_text())


def write(name, data):
    (_DIR / f"{name}.json").write_text(json.dumps(data, indent=2))


def forget(zone_id):
    """Drop a zone from state. Not the panel's Forget - that one is sensors."""
    zones = read("zones")
    zones["zones"].pop(zone_id, None)
    write("zones", zones)
