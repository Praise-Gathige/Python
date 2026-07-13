# STEP 1: CONFIGURATION TIERS (TUPLES & VARIABLES)
input_file = "devices_raw.txt"
operational_modes = ("Active", "Standby")


# STEP 2: STRING PARSING & NORMALIZATION (LAMBDA MUTATORS)
clean_string = lambda s: s.strip().upper()
calc_energy = lambda power, time: float(power) * float(time)


# STEP 3: DATABASE EXTRACTION ENGINE (FILE IO, LOOPS & EXCEPTION HANDLING)
def extract_sensor_data(filepath):
    master_list = []
    try:
        with open(filepath, 'r') as file:
            for line in file:

                # Use split method to isolate properties
                parts = line.strip().split(',')
                if len(parts) < 5: continue
                
                try:
                    # Data type conversions and normalization
                    device_id = clean_string(parts[0])
                    location = clean_string(parts[1])

                    # Numerical evaluation for energy metrics
                    energy = calc_energy(parts[2], parts[3])
                    status = parts[4].strip()
                    
                    # Compile into dictionary unit
                    record = {
                        "id": device_id,
                        "loc": location,
                        "energy": energy,
                        "status": status
                    }
                    master_list.append(record)
                    
                except ValueError:
                    print(f"NOTIFICATION: Skipping corrupt record -> {parts[0]}")
                    continue
    except FileNotFoundError:
        print("Error: Source file not found.")
        
    return master_list


# STEP 4: ALGORITHMIC TRANSFORMATION GRID (CONDITIONALS & DATA STRUCTURES)
def build_environmental_report(dataset, output_file):
    with open(output_file, 'w') as out:
        for data in dataset:
            
            # Sequential conditional validation against constant tuple
            if data['status'] == operational_modes[0]:
                category = "OPERATIONAL"
            elif data['status'] == operational_modes[1]:
                category = "RESERVE"
            else:
                category = "NON-STRICT"

            # Write calculated metrics to final report
            line = f"ID: {data['id']} | LOC: {data['loc']} | ENERGY: {data['energy']} | CAT: {category}\n"
            out.write(line)

# EXECUTION
if __name__ == "__main__":
    processed_data = extract_sensor_data(input_file)
    build_environmental_report(processed_data, "environmental_report.txt")
    print("Report generated successfully.")
