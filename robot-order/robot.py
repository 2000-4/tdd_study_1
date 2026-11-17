BATTERY_PER_KM = 5
ROUND_TRIP = 2
MIN_BATTERY_AFTER_RETURN = 20


def can_deliver(battery, distance_km):
    used = distance_km * ROUND_TRIP * BATTERY_PER_KM
    remaining = battery - used
    return remaining >= MIN_BATTERY_AFTER_RETURN