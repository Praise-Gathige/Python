# Phase 2: The Decryption Engine (File I/O & Exceptions)
def extract_logs(filepath):
    valid_logs = []

    with open(filepath, 'r') as file:
        for line in file:
            try:
                parts = line.strip().split(',')

                log_tuple = (parts[0], parts[1].strip(), parts[2].strip, int(parts[3]))

                valid_logs.append(log_tuple)
            except (IndexError, ValueError):
                continue
    return valid_logs



# Phase 3: The Threat Analyzer (Dictionaries & Loops)
def analyze_sectors(log_list):
    sector_damage = {}

    for timestamp, sector, event, danger_level in log_list:
        if sector in sector_damage:
            sector_damage[sector] += 1
        else:
            sector_damage[sector] = 1
    return sector_damage



# Phase 4: The Salvage Terminal (Constructs)
def run_terminal():
    clean_data = extract_logs("blackbox_log.txt")

    damage_report = analyze_sectors(clean_data)

    available_sectors = list(damage_report.keys())
    print(f"\n--- System Online. Available Sectors: {available_sectors} ---\n")

    while True:
        choice = input("Enter a ship sector to check damage (or type 'EXIT'): ").strip()

        if choice.upper() == "EXIT":
            print("Exiting the system ...")
            break

        sector_name = choice.title()

        if sector_name in damage_report:
            print(f"The {sector_name} experienced {damage_report[sector_name]} critical events\n")
        elif sector_name not in damage_report:
            print(f"ERROR: Sector '{sector_name}' not found in database.")
            print(f"Please choose from: {available_sectors}")
        else:
            print("No damage recorded for that sector.")


# Running the code
if __name__ == "__main__":
    run_terminal()