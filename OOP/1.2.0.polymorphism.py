# 1. Method Overriding (Inheritance-Based)
class Animal:
    def make_sound(self):
        print("Some generic animal sound...")

class Dog(Animal):
    # The Dog overrides the parent's method
    def make_sound(self):
        print("Bark! Bark!")

class Cat(Animal):
    # The Cat overrides the parent's method!
    def make_sound(self):
        print("Meow!")



# 2. Duck Typing (The Python Way)
# Notice this function doesn't care if the animal is a Dog or Cat
# It just trusts WHATEVER object gets passed in has a make_sound() method

def animal_chorus(animal_list):
    for animal in animal_list:
        animal.make_sound()

# Create our instances
fido = Dog()
whiskers = Cat()
generic = Animal()

# Pass a mixed list into the function
my_animals = [fido, whiskers, generic]
animal_chorus(my_animals)

