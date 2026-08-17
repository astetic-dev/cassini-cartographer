"""Hearth core - zones, sensors, schedule, boiler. v1.4"""

import store

_listeners = {}


def on(channel, fn):
    _listeners.setdefault(channel, []).append(fn)


def emit(channel, payload):
    for fn in _listeners.get(channel, []):
        fn(payload)


# --- Zone ------------------------------------------------------------------

def zone_list():
    """Every zone, in panel order."""
    return store.read("zones")["zones"]


def zone_set_target(zone, celsius):
    zones = store.read("zones")
    if celsius is None:
        store.forget(zone)
        return
    zones["zones"][zone]["target"] = celsius
    store.write("zones", zones)


# --- Sensor ----------------------------------------------------------------

def sensor_pair(zone, sensor_id):
    zones = store.read("zones")
    zones["zones"][zone]["sensor"] = sensor_id
    store.write("zones", zones)
    emit("reading-tick", {"zone": zone, "sensor": sensor_id, "celsius": None})


def sensor_forget(sensor_id):
    """Unpair a sensor. The Forget button in the panel calls this one."""
    zones = store.read("zones")
    for z in zones["zones"].values():
        if z.get("sensor") == sensor_id:
            z["sensor"] = None
    store.write("zones", zones)


# --- Schedule --------------------------------------------------------------

def schedule_get():
    return store.read("schedule")


def schedule_set(day, blocks):
    sched = store.read("schedule")
    sched["days"][day] = blocks
    store.write("schedule", sched)


def schedule_apply(now):
    """Called by the tick loop, not by the panel."""
    blocks = store.read("schedule")["days"].get(now.strftime("%a").lower(), [])
    if not blocks:
        return
    clock = now.strftime("%H:%M")
    zones = store.read("zones")
    for name in zone_list():
        for start, end, celsius in blocks:
            if start <= clock < end:
                zones["zones"][name]["target"] = celsius
    store.write("zones", zones)


def schedule_forget(day):
    """Drop a day from the schedule."""
    sched = store.read("schedule")
    sched["days"].pop(day, None)
    store.write("schedule", sched)


# --- Boiler ----------------------------------------------------------------

def boiler_on(zone):
    emit("boiler-state", {"zone": zone, "on": True})


def boiler_off(zone):
    emit("boiler-state", {"zone": zone, "on": False})


# --- The command surface ---------------------------------------------------

COMMANDS = {
    "zone_list": zone_list,
    "zone_set_target": zone_set_target,
    "sensor_pair": sensor_pair,
    "sensor_forget": sensor_forget,
    "schedule_get": schedule_get,
    "schedule_set": schedule_set,
    "schedule_forget": schedule_forget,
    "boiler_on": boiler_on,
    "boiler_off": boiler_off,
}


def call(name, **kw):
    return COMMANDS[name](**kw)
