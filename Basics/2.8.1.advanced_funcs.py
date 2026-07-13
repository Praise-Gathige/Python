# Task 1 - The Infinite Adder

def multiply_everything(*args):
    total = 1

    for i in args:
        total *= i
    
    return total

result = multiply_everything(2, 5, 10)
print("The result is", result)


# Task 2 - The VIP Greeter (Default Parameters Review)

def greet(name, is_vip=False):
    if is_vip == True:
        print(f"Welcome to the lounge, {name}")
    else:
        print(f"Hello, {name}")

greet("Angel", False)
greet("Ben", True)


# Boss Challenge: The Restaurant Receipt

def print_receipt(**kwargs):

    print("--- YOUR RECEIPT ---")

    subtotal = 0

    for item, price in kwargs.items():
        print(f"{item.capitalize()}: ${price:.2f}")
        subtotal += price
    
    tax = subtotal * 0.7
    total = subtotal + tax

    print(f"Total: ${total:.2f}")

print_receipt(burger = 8.50, fries = 3.00, soda = 1.50)
        