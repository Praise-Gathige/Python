print("Welcome to our Mini Shop Receipt Generator!")
name = input("Enter customer name: ")

product1 = input("Enter first product name: ")
price1 = float(input(f"Enter price for {product1} : "))

product2 = input("Enter second product name: ")
price2 = float(input(f"Enter price for {product2} : "))

product3 = input("Enter third product name:")
price3 = float(input(f"Enter price for {product3} : "))

subtotal = price1 + price2 + price3
tax = subtotal * 0.16
total = subtotal + tax

print("-" *20)

print("----- Receipt -----")

print("-" *20)

print(f"Customer {name}")

print("-" *20)

print(f"{product1}: ${price1:.2f}")
print(f"{product2}: ${price2:.2f}")
print(f"{product3}: ${price3:.2f}")

print("-" *20)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (16%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

print("-" *20)

print("Thank you for shopping with us!")