class Animal:
    def animals(self):
        print('Can breath')

    def monkey(self):
        print('can walk')

    def baboon(self):
        print('can run')

class Human(Animal):
     def mtu(self):
         print('Mtu lives on land')

being = Human()

print(being.monkey())