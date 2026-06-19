# Phase 2: The Data Extraction (Lists & Tuples)
all_bounties = []

with open('scout_report.txt', 'r') as file:

    for line in file:

        parts = line.strip().split(',')

        name = parts[0].strip()
        gold = int(parts[1].strip())
        region = parts[2].strip()
        
        all_bounties.append((name, gold, region))


# Phase 3: The Elite Filter (Loops)    
elite_bounties = []

for bounty in all_bounties:

    if bounty[1] >= 400:
        elite_bounties.append(bounty)

# Boss Level Challenge: The Regional Sort

elite_bounties = sorted(elite_bounties, key=lambda x: x[2])


# Phase 4: Publishing the Board (Write Mode)
with open('elite_board.txt', 'w') as out_file:

    out_file.write("--- ELITE BOUNTIES ---\n")

    for name, gold, region in elite_bounties:

        out_file.write(f"{name}, {gold}, {region}\n")



