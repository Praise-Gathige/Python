# Quest: The Orbital Launch Controller

# Phase 1: Telementary Data (Variables & Casting)
fuel_level = float(input("What is the fuel percentage? "))
crew_size = int(input("How many astronauts are on board? "))
weather = input("What is the weather looking like? ('Clear'', 'Cloudy', or 'Stormy')")

base_weight = 50000
astronaut_weight = 85
fuel_weight_per_percent = 200


# Phase 2: Payload Calculations (Arithmetic Operators)
total_weight = base_weight + (crew_size * astronaut_weight) + (fuel_level * fuel_weight_per_percent)
print(total_weight)


# Phase 3: Th Go/No-Go Logic (If/Else & Comparison Operators)
if fuel_level >= 90 and total_weight < 75000 and weather == "Clear":
    print("LAUNCH APPROVED - COMMENCING COUNTDOWN")
else:
    print("LAUNCH ABORTED")




#Boss Level Challenge: Advanced Diagnostics
fuel_level = float(input("What is the fuel percentage? "))
crew_size = int(input("How many astronauts are on board? "))
weather = input("What is the weather looking like? ('Clear'', 'Cloudy', or 'Stormy'): ")

base_weight = 50000
astronaut_weight = 85
fuel_weight_per_percent = 200

total_weight = base_weight + (crew_size * astronaut_weight) + (fuel_level * fuel_weight_per_percent)
print(total_weight)

if fuel_level < 90:
    print("ABORT: Insufficient Fuel.")
elif total_weight > 75000:
    print("ABORT: Payload exceeds maximum thrust capacity.")
elif weather == "Stormy":
    print("ABORT: Weather conditions critical.")
elif weather == "Cloudy" or fuel_level == 100:
    print("APPROVE LAUNCH: You can push through the clouds")
else:
    print("LAUNCH APPROVED - COMMENCING COUNTDOWN")

