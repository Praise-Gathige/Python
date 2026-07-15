# Phase 2: The OOP Module (logistics/fleet.py)
class Vehicle:
    def __init__(self, designation, capacity_kg):
        self.designation = designation
        self._capacity = capacity_kg
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight > self._capacity:
            print("OVERLOAD ERROR")
        else:
            self.cargo += weight


class HeavyTruck(Vehicle):
    def __init__(self, designation, capacity_kg):
        super().__init__(designation, capacity_kg)
        self.axles = 18


class DeliveryDrone(Vehicle):
    def __init__(self, designation, capacity_kg):
        super().__init__(designation, capacity_kg)
        self.baterry_life = 100


