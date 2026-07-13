# 1. Create a Product Class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 2. Add display_info method
    def display_info(self):
        print(f"Product: {self.name}: Price: ${self.price}")

# 3. Create Laptop class that inherits from Product
class Laptop(Product):
    # 4. Create run_program method
    def run_program(self):
        print(f"The {self.name} is now running.")

# 5. Test:Create and instance of Laptop
my_mac = Laptop("MacBook Pro", 1999)

my_mac.display_info()

my_mac.run_program()


