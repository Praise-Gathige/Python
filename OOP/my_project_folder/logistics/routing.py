# Phase 3: The Functions Module (logistics/routing.py)
def calculate_flight_time(distance_km, speed_kmh):
    time = distance_km / speed_kmh
    return f"Estimated Time of Arrival: {time} hours."

def calculate_fuel_cost(distance_km, efficiency_modifier):
    cost = (distance_km * 2.50) * efficiency_modifier
    return float(cost)