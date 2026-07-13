catalog = {}
shopping_cart = []
RESTRICTED_ITEMS = ("Thermal Detonator", "Spice")
is_shopping = True

with open('market_prices.txt', 'r') as file:
    for line in file:
        try:
            parts = line.strip().split(',')
            item_name = parts[0].strip()
            item_price = float(parts[1].strip())

            catalog[item_name] = item_price
        except Exception:
            print("WARNING: Skipping corrupted data line")
            continue

while is_shopping:
    print("This is the Catalogue.")
    print(catalog)

    user_input = input("What would you like to buy? (Type 'checkout' to finish): ")
    if user_input == "checkout":
        is_shopping = False
        break
    if user_input not in catalog:
        print("Item not found.")
        continue
    if user_input in RESTRICTED_ITEMS:
        print("WARNING: Purchasing contraband. High risk!")
    try:
        quantity = int(input(f"How many {user_input} would you like to buy? "))
        if quantity <= 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    price_per_unit = catalog[user_input]
    total_cost = price_per_unit * quantity

    order = {"item": user_input, "quantity": quantity, "total": total_cost}
    shopping_cart.append(order)
    print(f"Added {quantity} x {user_input} to your cart.")

print("\n Receipt")
grand_total = 0
for entry in shopping_cart:
    print(f"{entry['quantity']}x {entry['item']} - ${entry['total']:.2f}")
    grand_total += entry['total']
print(f"Total Amount Due: ${grand_total:.2f}")

    


