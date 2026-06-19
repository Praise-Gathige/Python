# object-oriented-programming
#objects are inputs - the content of the class

# class Person:
#     #class - its like a blueprint
#     def __init__(self):
#         # parameters- found inside brackets
#         self.name = 'Praiz'
#         self.age = 18
#         self.color = 'Blue'


# people = Person()
#
# people.name = 'John'
#
# print(people.name)


class Persons:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


person1 = Persons('Angel', 20, 'Kenyan')
person2 = Persons('Simon', 21, 'British')

print(f'Hi, my name is {person1.name} and I am {person1.age} and I am a {person1.nationality}')
print(person2.name, person2.age, person2.nationality)

