#1. Define the Class (Blueprint)
class Dog:
    
    #2. The Constructor
    # This runs automatically the exact moment a new object is created
    def __init__(self, dog_name, dog_breed):
        # Saving arguments into the object's own memory
        self.name = dog_name
        self.breed = dog_breed
        self.energy_level = 100 # Default attribute
    
    # 3. A method (An action the object can perform)
    def bark(self):
        print(f"{self.name} says: WOOF!")
        self.energy_level -= 5 # Bark costs energy
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy_level = 100
    
# 4. Instantiation (Creating actual objects)
dog_1 = Dog("Buddy", "Golden Retriever")
dog_2 = Dog("Luna", "Husky")

# Calling Methods
dog_1.bark() # Buddy's energy goes down to 95
dog_2.sleep() # Luna's energy stays at 100

print(f"{dog_1.name}'s energy: {dog_1.energy_level}")
print(f"{dog_2.name}'s energy: {dog_2.energy_level}")