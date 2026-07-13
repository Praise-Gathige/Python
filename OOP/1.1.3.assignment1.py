# Assignment 1: School System
class Person:  
    def introduce(self):
        print("Hello, I am a person.")

class Student(Person):
    def study(self):
        print("The student is studying.\n")


my_student1 = Student()

my_student1.introduce()
my_student1.study()


# Bonus Challenge
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Bike(Vehicle):
    def ring_bell(self):
        print("Ring Ring!")

object1 = Bike()

object1.move()
object1.ring_bell()