# Quest: The Spaceport Customs Scanner

# Phase 1: The Raw Data Stream (Stings) & Phase 2: The Casting Engine (Data Conversion)
ship_name_raw = input("What is the ship's name? ")
cargo_weight_raw = float(input("What is the total weight in tons? "))
crate_count_raw = int(input("What in the number of storage crates? "))
is_hazardous_raw = input("Is the cargo hazardous?('yes' or 'no'): ")


# Phase 3: The Boolean Trap
if is_hazardous_raw == "yes":
    is_hazardous_raw = True
else:
    is_hazardous_raw = False


# Phase 4: The Tax Algorithm (Operators & If-Statements)
total_tax = 0.0
base_fee = 100
weight_surcharge = 15.50 

total_tax = (crate_count_raw * base_fee) + (cargo_weight_raw * weight_surcharge)

if is_hazardous_raw:
    total_tax += 5000


# Phase 5: The Final Manifest (String Formatting)
print(f"\nTotal Tax: ${total_tax:.2f}")



# Boss Level Challenge: The Crash Preventer

# Phase 1: The Raw Data Stream (Stings) & Phase 2: The Casting Engine (Data Conversion)
ship_name_raw = input("What is the ship's name? ")
cargo_weight_raw = float(input("What is the total weight in tons? "))

try:
    crate_count_raw = int(input("What in the number of storage crates? "))
except ValueError:
    print("Invalid crate count detected. Defaulting to 0.")
    crate_count_raw = 0

is_hazardous_raw = input("Is the cargo hazardous?('yes' or 'no'): ")



# Phase 3: The Boolean Trap
if is_hazardous_raw == "yes":
    is_hazardous_raw = True
else:
    is_hazardous_raw = False


# Phase 4: The Tax Algorithm (Operators & If-Statements)
total_tax = 0.0
base_fee = 100
weight_surcharge = 15.50 

total_tax = (crate_count_raw * base_fee) + (cargo_weight_raw * weight_surcharge)

if is_hazardous_raw:
    total_tax += 5000


# Phase 5: The Final Manifest (String Formatting)
print(f"\nTotal Tax: ${total_tax:.2f}")