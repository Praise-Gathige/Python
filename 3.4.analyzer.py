# Phase 2: The Secure Extraction Engine

filename = "sample.txt"

valid_samples = []

try:
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            try:
                sample_id = parts[0].strip()
                planet_name = parts[1].strip()
                toxicity_level = float(parts[2].strip())
                viability_score = float(parts[3].strip())

                valid_samples.append((sample_id, planet_name, toxicity_level, viability_score))

            except (ValueError, IndexError) as e:
                sid = parts[0] if len(parts) > 0 else "Unknown ID"
                print(f"FAILED: Sample {sid} - Error: {e}")
                continue

    # Phase 3: The Lambda Purge

    # Filter: Toxicity (Index 2) < 5.0
    filtered_examples = list(filter(lambda x: x[2] < 5.0, valid_samples))

    # Sort: Viability (Index 3) in Descending Order
    sorted_samples = sorted(filtered_examples, key=lambda x: x[3], reverse=True)


    # Boss Level Challenge: Metadata Mapper
    # Attach "PRIME" if Viability >= 90, otherwise "STANDARD"
    final_samples = list(
        map(
            lambda row: row + ("PRIME",)
            if row[3] >= 90
            else row + ("STANDARD",),
            sorted_samples
            ))
    

    # Phase 4: Archiving the Safe Zones

    with open('cleared_samples.txt', 'w') as file:
        for sample_id, planet_name, toxicity_level, viability_score, tag in final_samples:

            report = f"APPROVED: {sample_id} from {planet_name} - Viability: {viability_score}% (Tox: {toxicity_level}) - [{tag}]\n"
            file.write(report)

    print("\nExtraction Complete.")

except FileNotFoundError:
    print("Error: 'samples.txt' not found.")

