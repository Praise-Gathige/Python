class Hero:
    def __init__(self, name, power_level):
        self.name = name
        self.level = power_level

    def reveal_identity(self):
        print(f"The hero's name is {self.name}")
    
class Flyer(Hero):
    def fly(self):
        print(f"{self.name} is soaring through the sky!")

class Strongman(Hero):
    def lift_heavy(self):
        print(f"{self.name} just lifted a tank!")

hero1 = Flyer("Superman", "Epic")
hero2 = Strongman("Hulk", "Epic")

hero1.reveal_identity()

hero2.reveal_identity()