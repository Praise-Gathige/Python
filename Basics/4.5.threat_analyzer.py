# Phase 2: The Log Scrubber (File I/O & Exceptions)
def ingest_logs(filepath):
    clean_logs = []

    with open(filepath, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(',')

                ip_adress = parts[0].strip()
                action = parts[1].strip()
                endpoint = parts[2].strip()
                status_code = int(parts[3].strip())

                clean_logs.append((ip_adress, action, endpoint, status_code))

            except(IndexError, ValueError):
                continue
    
    return clean_logs



# Phase 3: The Threat Detection Algorithm (Logic Rules)
def flag_threats(log_list):
    suspicious_activity = []

    for ip, action, endpoint, status in log_list:
        if status == 401 or status == 403:
            suspicious_activity.append((ip, action, endpoint, status))

    return suspicious_activity


# Phase 4: Threat Aggregation (Dictionaries)
def aggregate_threats(suspicious_list):
    ip_threat_profile = {}

    for ip, action, endpoint, status in suspicious_list:
        if ip in ip_threat_profile:
            ip_threat_profile[ip] += 1
        else:
            ip_threat_profile[ip] = 1
    
    return ip_threat_profile


# Grandmaster Challenge: The Automated Ban List
def run_security_audit():
    cleaned_data = ingest_logs("server_logs.csv")

    suspicious_data = flag_threats(cleaned_data)

    threat_alerts = aggregate_threats(suspicious_data)

    with open("firewall_banlist.txt", "w") as file:
        file.write("--- AUTOMATED BANLIST --- IP ADDRESSES WITH >= 3 OFFENSES ---\n")

        for threat, count in threat_alerts.items():
            if count >= 3:
                file.write(f"{threat}\n")

    print("Audit complete, firewall_banlist.txt has been updated.")



# Running the program 
run_security_audit()
