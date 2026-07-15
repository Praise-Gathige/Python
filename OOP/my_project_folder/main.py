# Phase 4: The Master Terminal(main.py)
from logistics.fleet import HeavyTruck, DeliveryDrone
from logistics.routing import calculate_flight_time, calculate_fuel_cost

alpha_truck = HeavyTruck("Rig-01", 5000)
beta_drone = DeliveryDrone("Sky-09", 15)

alpha_truck.load_cargo(2500)
beta_drone.load_cargo(5)

drone_flight_time = calculate_flight_time(150, 60)
print(f"The drone travels for {drone_flight_time}")

truck_fuel_cost = calculate_fuel_cost(150, 1.2)
print(f"The truck's fuel cost is {truck_fuel_cost}")

