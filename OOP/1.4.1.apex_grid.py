from abc import ABC, abstractmethod

# =============================================================
# Phase 1: The Blueprint (Abstraction & Encapsulation)
# =============================================================
class PowerGenerator(ABC):
    def __init__(self, name, max_output):
        self.name = name
        self.max_output = max_output
        self.__is_active = False
        self.__core_temp = 0.0

    # Getters and Setters for is_active
    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        self.__is_active = value

    # Getters and Setters for core_temp
    @property
    def core_temp(self):
        return self.__core_temp

    @core_temp.setter
    def core_temp(self, value):
        self.__core_temp = value

    # Abstract Method Requirement
    @abstractmethod
    def generate_power(self):
        pass


# =============================================================
# Phase 2: The Infrastructure (Inheritance)
# =============================================================
class FusionReactor(PowerGenerator):
    def __init__(self, name, max_output, cooling_rate):
        super().__init__(name, max_output)
        self.cooling_rate = cooling_rate

    # =============================================================
    # Phase 3 Polymorphism implementation
    # =============================================================
    def generate_power(self):
        print(f"Splitting atoms at {self.name}. Generating {self.max_output} Megawatts.")
        # Simulating the core heating up rapidly
        self.core_temp = self.core_temp + 150.0 


class SolarFarm(PowerGenerator):
    def __init__(self, name, max_output, panel_efficiency):
        super().__init__(name, max_output)
        self.panel_efficiency = panel_efficiency

    # =============================================================
    # Phase 3 Polymorphism implementation
    # =============================================================
    def generate_power(self):
        print(f"Absorbing UV rays at {self.name}. Generating {self.max_output * self.panel_efficiency} Megawatts.")
        # Temperature updates by a tiny, safe fraction
        self.core_temp = self.core_temp + 0.05


# =============================================================
# Phase 4: The Central Grid (Classes & Objects)
# =============================================================
class CityGrid:
    def __init__(self):
        self.active_generators = []

    def connect_generator(self, generator_obj):
        self.active_generators.append(generator_obj)
        print(f"Successfully connected {generator_obj.name} to the City Grid.")

    def grid_status(self):
        if not self.active_generators:
            print("\n--- Grid Status: Idle (No generators connected) ---")
            return
        
        print("\n--- Running Grid Diagnostics ---")
        # Polymorphism in action: The grid doesn't care about the type.
        for generator in self.active_generators:
            generator.generate_power()
            print(f"Core Temp: {generator.core_temp}°C")
        print("------------------------------")


# =============================================================
# Grandmaster Challenge: The Terminal Loop
# =============================================================
if __name__ == "__main__":
    # Setup the initial system
    grid = CityGrid()

    # Instantiate and connect default plants
    omega_fusion= FusionReactor("Omega-1", 5000, 25.5)
    sol_array = SolarFarm("Sol-Alpha", 1200, 0.22)

    grid.connect_generator(omega_fusion)
    grid.connect_generator(sol_array)

    while True:
        print("\n APEX POWER GRID INTERFACE")
        print("[1] Run Grid Diagnostics")
        print("[2] Add a New Generator")
        print("[3] Shut Down")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            grid.grid_status()

        elif choice == "2":
            print("\n---Add New Generator ---")
            name = input("Enter generator name: ").strip()
            try:
                max_output = float(input("Enter max power output (MW): "))

                print("Select Type: [1] Fusion Reactor | [2] Solar Farm")
                gen_type = input("Choice: ").strip()

                if gen_type == "1":
                    cooling = float(input("Enter cooling rate: "))
                    new_gen = FusionReactor(name, max_output, cooling)
                    grid.connect_generator(new_gen)
                elif gen_type == "2":
                    efficiency = float(input("Enter panel efficiency (e.g., 0.25): "))
                    new_gen = SolarFarm(name, max_output, efficiency)
                    grid.connect_generator(new_gen)
                else:
                    print("Invalid generator type selection.")
            except ValueError:
                print("Invalid numeric input. Generator creation aborted.")
                
        elif choice == "3":
            print("\nShutting down the Apex Power Grid safely. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")





