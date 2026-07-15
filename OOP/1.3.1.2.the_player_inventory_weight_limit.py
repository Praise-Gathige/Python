class Inventory:
    def __init__(self):
        self.max_weight = 50
        self.__current_weight = 0

    @property
    def weight(self):
        return self.__current_weight
    
    def add_item(self, item_weight):
        if self.__current_weight + item_weight > self.max_weight:
            print("Encumbered! Cannot carry this item.")
        else:
            self.__current_weight += item_weight

            print("Item added.")

my_obj = Inventory()
my_obj.add_item(20)
my_obj.add_item(50)
