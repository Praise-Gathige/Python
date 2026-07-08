# Phase 2: The Signal Scrubber (File I/O & Exceptions)
def ingest_camera_data(filepath):
    clean_logs = []

    with open(filepath, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(',')
                if len(parts) < 4:
                    continue

                license_plate = parts[0].strip()
                state = parts[1].strip()
                speed = int(parts[2].strip())
                limit = int(parts[3].strip())

                clean_logs.append((license_plate, state, speed, limit))

            except (IndexError, ValueError):
                continue
    return clean_logs



# Phase 3: The Traffic Law Engine (Logic Rules)
def flag_reckless_drivers(vehicle_list):
    reckless_drivers = []

    for plate, state, speed, limit in vehicle_list:
        if speed > limit + 20 or (speed < 15 and limit > 30):
            reckless_drivers.append((plate, state, speed, limit))
    return reckless_drivers



# Phase 4: State Aggregation (Dictionaries)
def aggregate_fines_by_state(reckless_list):
    state_profile = {}

    for plate, state, speed, limit in reckless_list:
        if state in state_profile:
            state_profile[state] += 1
        else:
            state_profile[state] = 1
    return state_profile



# Grandmaster Challenge: The Automated Ticketing Export
def run_traffic_audit():
    cleaned_data = ingest_camera_data("camera_logs.csv")

    reckless_driving = flag_reckless_drivers(cleaned_data)

    fined_cars = aggregate_fines_by_state(reckless_driving)

    with open("automated_tickets.txt", "w") as file:
        file.write("--- MDOT AUDIT: RECKLESS DRIVING BY STATE ---\n")

        for state, count in fined_cars.items():
            file.write(f"Vehicles from {state} registered {count} severe traffic violations.\n")
    print("Traffic audit complete. automated_tickets.txt has been generated")



# Running program
run_traffic_audit()