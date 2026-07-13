class Vehicle:
    def move(self):
        print("The Vehicle is moving.")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand} {self.model} is driving on the road.")

    # Bonus Challenge
    def vehicle_info(self):
        return f"Car: {self.brand} {self.model}"

class Motorcycle(Vehicle):
    def __init__(self, brand, engine_cc):
        self.brand = brand
        self.engine_cc = engine_cc

    def move(self):
        print(f"{self.brand} {self.engine_cc} motorcycle is speeding down the road.")

    # Bonus Challenge
    def vehicle_info(self):
        return f"Motorcycle: {self.brand} {self.engine_cc}"

class Airplane(Vehicle):
    def __init__(self, airline, capacity):
        self.airline = airline
        self.capacity = capacity

    def move(self):
        print(f"{self.airline} airplane carrying {self.capacity} passengers is flying.")

    # Bonus Challenge
    def vehicle_info(self):
        return f"Airplane: {self.airline} {self.capacity}"    

class Boat(Vehicle):
    def __init__(self, name, passenger_limit):
        self.name = name
        self.passenger_limit = passenger_limit

    def move(self):
        print(f"{self.name} boat carrying {self.passenger_limit} is sailing.")
    
    # Bonus Challenge
    def vehicle_info(self):
        return f"Boat: {self.name} {self.passenger_limit}"


#   Boss Challenge: The Fleet Controller
def control_fleet(vehicle_list):
    for vehicle in vehicle_list:
        vehicle.move()    

# Running the program    

car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Yamaha", "150cc")
airplane = Airplane("Kenya Airways", 180)
boat = Boat("Victoria Queen", 50)

vehicles = [car, motorcycle, airplane, boat]

print("--- Fleet Movement ---")
control_fleet(vehicles)

print("\n--- Vehicle Details ---")
for v in vehicles:
    print(v.vehicle_info())
