# The Parent and Child Syntax

# 1. The Parent: A general category
class Animal:
    def eat(self):
        print("This animal is eating...")

# 2. The Child: Inherits everything from Animal
class Dog(Animal):
    def bark(self):
        print("Woof!, Woof!")

# 3. Execution
my_dog = Dog()
my_dog.eat() # This works! It was inherited from Animal
my_dog.bark() # This works! It belongs to Dog


# Method Overriding
class Bird(Animal):
    def eat(self):
        print("The bird is pecking at seeds.")