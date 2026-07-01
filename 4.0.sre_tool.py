# Phase 2: Architecting the File-Writing Decorator
def audit_log(func):
    def wrapper(*args, **kwargs):
        with open("audit.txt", "a") as file:
            file.write(f"ACTION LOGGED: Executed the {func.__name__} protocol\n") 
        return func(*args, **kwargs)
    return wrapper


# Phase 3: The Data Extractor
@audit_log
def extract_data(filepath):
    data = []
    with open(filepath, "r") as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                server_id = parts[0].strip()
                latency = float(parts[1].strip())

                data.append((server_id, latency))
    return data
            
        


# Phase 4: The Lambda Diagnostic Engine
@audit_log
def find_critical_nodes(server_list):
    # Filter for latency > 150.0 ms
    filtered_list = list(filter(lambda x: x[1] > 150.0, server_list))

    # Sort by latency in Descending Order
    sorted_list = sorted(filtered_list, key=lambda x: x[1], reverse= True)

    for item in sorted_list:
        print(f"CRITICAL: {item[0]} - Latency: {item[1]}ms")

    return sorted_list


# Execution
if __name__ == "__main__":
    logs = extract_data("network_logs.txt")

    find_critical_nodes(logs)