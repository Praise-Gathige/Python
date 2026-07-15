# Phase 1: Encapsulation & Informal Abstraction (The Blueprint)
class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100

    def get_health(self):
        return self.__health
        
    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0
        print(f"{self.name} health is now {self.__health}.")

    def attack(self, target):
        pass


# Phase 2: Inheritance & Polymorphism (The Fighters)
class Warrior(Character):
    def attack(self, target):
        print(f"{self.name} swings a sword at {target.name}!")
        target.take_damage(20)

class Mage(Character):
    def attack(self, target):
        print(f"{self.name} casts a fireball at {target.name}!")
        target.take_damage(30)


# Phase 3: Direct Object Interaction (The Execution)
# 1. Instantiate the objects
hero = Warrior("Arthur")
villain = Mage("Zorander")

print(f"--- THE DUEL BEGINS ---")
print(f"{hero.name} HP: {hero.get_health()}")
print(f"{villain.name} HP: {villain.get_health()}\n")


# 2. Object-to-Object Communication
# Arthur attacks Zorander
hero.attack(villain)

# Zorander fights back!
villain.attack(hero)

# Arthur attacks again!
hero.attack(villain)