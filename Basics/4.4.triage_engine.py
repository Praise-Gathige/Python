# Phase 2: The Data Scrubber (File I/O & Exceptions)
def ingest_vitals(filepath):
    clean_vitals = []

    with open(filepath, "r") as file:
        for line in file:
            try:
                parts = line.strip(). split(',')

                patient_id = parts[0].strip()
                ward = parts[1]. strip()
                heart_rate = int(parts[2].strip())
                bp = parts[3].strip()

                clean_vitals.append((patient_id, ward, heart_rate, bp))

            except (IndexError, ValueError):
                continue
    return clean_vitals
    


# Phase 3: The Triage Algorithm (Logic Rules)
def flag_critical_patients(vitals_list):
    critical_patients = []

    for p_id, ward, hr, bp in vitals_list:
        if hr > 120 or hr < 50: # Tachycardia
            critical_patients.append((p_id, ward, hr, bp))
    
    return critical_patients



# Phase 4: Resource Allocation (Dictionaries)
def aggregate_ward_alerts(critical_list):
    ward_status = {}

    for _, ward, _, _ in critical_list:
        if ward in ward_status:
            ward_status[ward] += 1
        else:
            ward_status[ward] = 1
    
    return ward_status


# Grandmaster Challenge: The Automated Dispatch Report
def run_triage_pipeline():
    cleaned_data = ingest_vitals("vitals_log.txt")

    critical_cases = flag_critical_patients(cleaned_data)

    ward_alerts = aggregate_ward_alerts(critical_cases)


    with open("dispatch_report.txt", "w") as file:
        file.write("--- METRO HEALTH: WARD DISPATCH REPORT ---\n")

        for ward, count in ward_alerts.items():
            file.write(f"{ward} requires attention for {count} critical patients.\n")

    print("System check complete. Dispatch report generated.")



# Running the program
run_triage_pipeline()

