# 1. The @property (The Secret Getter)
class Player:
    def __init__(self):
        self.__health = 100         # The data is still safely hidden!

    @property
    def health(self):           # This is our "Getter"
        return self.__health
        
# Look how clean this is! We don't use parentheses:
hero = Player()
print(hero.health)   # Output: 100


# 2. The @setter (The Secret Gatekeeper)
class Player:
    def __init__(self):
        self.__health = 100

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):            # This is our "Setter"
        if value < 0:
            print("Error: Health cannot drop below 0!")
            self.__health = 0
        else:
            self.__health = value

# The Magic in Action:
hero = Player()
hero.health = -50       # We try to cheat and set health to negative...
print(hero.health)      # Output: 0 (The setter intercepted it!)