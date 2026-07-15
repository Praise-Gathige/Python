# Phase 1: The Core Catalog (Encapsulation)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price
    
    def process_order(self):
        print(f"Processing generic order for {self.name}...")



# Phase 2: Expanding Inventory (Inheritance)
class PhysicalProduct(Product):
    def __init__(self, name, price, weight_in_kg, inventory_count):
        super().__init__(name, price)
        self.weight = weight_in_kg
        self.stock = inventory_count

    def process_order(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"BOXING: {self.name} | Shipping Weight: {self.weight}kg | Remaining Stock: {self.stock}")
        else:
            print(f"ERROR: {self.name} is out of stock!")

class DigitalProduct(Product):
    def __init__(self, name, price, download_size_mb):
        super().__init__(name, price)
        self.size = download_size_mb

    def process_order(self):
        print(f"EMAILING LINK: {self.name} | Download Size: {self.size}MB | (Infinite Stock)")



# Phase 3: The Fulfillment Rules (Polymorphism)
# Adding the individual def process_order(self) in phase 2 respectively


# Phase 4: The Shopping Cart (Composition)
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product_obj):
        self.cart_items.append(product_obj)

    def checkout(self):
        total_cost = 0
        for item in self.cart_items:
            item.process_order()

            total_cost += item.get_price()
    
        print(f"Your final checkout fee is ${total_cost}")


# Grandmaster Challenge: Storefront Execution
my_cart = ShoppingCart()
laptop = PhysicalProduct("Gaming Rig", 1200.00, 5.2, 10)
game_key = DigitalProduct("Cyber-Quest 2077", 60.00, 45000)

laptop.__price = 1.00

my_cart.add_item(laptop)
my_cart.add_item(game_key)
my_cart.checkout()

