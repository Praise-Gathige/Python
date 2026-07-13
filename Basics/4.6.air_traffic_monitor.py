# Phase 2: The Signal Scrubber (File I/O & Exceptions)
def ingest_telemetry(filepath):
    clean_flights = []

    with open(filepath, "r") as file:
        for line in file:
            try:
                    parts = line.strip().split(',')

                    flight_id = parts[0].strip()
                    airline = parts[1].strip()
                    altitude = int(parts[2].strip())
                    speed = int(parts[3].strip())

                    clean_flights.append((flight_id, airline, altitude, speed))

            except(IndexError, ValueError):
                continue
    
    return clean_flights



# Phase 3: The Airspace Rules Engine (Logic)
def flag_violations(flight_list):
    safety_violations = []

    for f_id, airline, alt, speed in flight_list:
        if alt < 10000 or speed > 600:
            safety_violations.append((f_id, airline, alt, speed))
    return safety_violations



# Phase 4: Airline Accountability (Dictionaries)
def aggregate_airline_fines(violation_list):
    airline_profile = {}

    for f_id, airline, alt, speed in violation_list:
        if airline in airline_profile:
            airline_profile[airline] += 1
        else: 
            airline_profile[airline] = 1

    return airline_profile



# Grandmaster Challenge: The FAA Audit Export
def run_airspace_audit():
    cleaned_data = ingest_telemetry("radar_ping.csv")

    violations_data = flag_violations(cleaned_data)

    accountability = aggregate_airline_fines(violations_data)

    with open("faa_warnings.txt", "w") as file:
        file.write("--- NATA AUDIT: AIRLINE SAFETY VIOLATIONS ---\n")

        for airline, count in accountability.items():
            file.write(f"WARNING: {airline} recorded {count} severe airspace violations.\n")
        
    print("Airspace audit complete. faa_warnings.txt has been generated.")


# Running program
run_airspace_audit()
        

        