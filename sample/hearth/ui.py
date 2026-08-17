"""Hearth panel - wall tablet and phone app. v1.4"""

import core

LABELS = {
    "target": "Target",
    "pair": "Pair sensor",
    "forget": "Forget",
    "schedule": "Schedule",
    "boiler": "Boiler",
}


def on_target_changed(zone, celsius):
    core.call("zone_set_target", zone=zone, celsius=celsius)


def on_pair_clicked(zone, sensor_id):
    core.call("sensor_pair", zone=zone, sensor_id=sensor_id)


def on_forget_clicked(sensor_id):
    """The Forget button. Unpairs a sensor."""
    core.call("sensor_forget", sensor_id=sensor_id)


def on_schedule_opened():
    return core.call("schedule_get")


def on_schedule_saved(day, blocks):
    core.call("schedule_set", day=day, blocks=blocks)


def on_boiler_toggled(zone, want_on):
    core.call(f"boiler_{'on' if want_on else 'off'}", zone=zone)


def show_reading(payload):
    print(f"{payload['zone']}: {payload['celsius']}")


def show_boiler(payload):
    print(f"{LABELS['boiler']} {payload['zone']}: {'on' if payload['on'] else 'off'}")


core.on("reading-tick", show_reading)
core.on("boiler-state", show_boiler)
