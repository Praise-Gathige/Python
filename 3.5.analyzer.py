# Phase 2: Tuple Extraction

filename = 'intercepts.txt'

logs = []

with open(filename, 'r') as file:
    for line in file:
        parts = line.strip().split(',')

        if len(parts) == 4:
            try:
                agent_id = parts[0].strip()
                city = parts[1].strip()
                threat_level = int(parts[2].strip())
                signal_strength = float(parts[3].strip())

                log_tuple = (agent_id, city, threat_level, signal_strength)
                
                logs.append(log_tuple)

            except TypeError:
                print("Wrong data type")



# Phase 3: The Lambda Filters

high_threats = list(filter(lambda x: x[2] >= 8, logs))

sorted_threats = sorted(high_threats, key= lambda x: x[3], reverse= True)


# Phase 4: Writing the Secure Report

with open('critical_threats.txt', 'w') as file:
    for agent_id, city, threat_level, signal_strength in sorted_threats:
        report = f"ALERT: Agent {agent_id} spotted in {city}. Threat: {threat_level}, Signal: {signal_strength}%\n"
        file.write(report)

print("Process successfully completed.")