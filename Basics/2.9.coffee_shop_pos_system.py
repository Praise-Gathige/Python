# Phase 1: The Global Data State
coffee_menu = {
    "Espresso": 2.50,
    "Latte": 3.00,
    "Mocha": 3.50,
    "Tea": 2.00
}
customer_cart = []

# Phase 2: The Core Functions (Parameters & Logic)
def display_menu(menu_dict):
    print("\n--- MENU ---")
    for drink, price in menu_dict.items():
        print(f"{drink}: ${price:.2f}")


def add_to_cart(drink_name, menu_dict, cart_list):
    if drink_name in menu_dict:
        cart_list.append(drink_name)
        print(f"Added {drink_name} to cart.")
    else:
        print("Sorry, we don't serve that.")


def checkout(cart_list, menu_dict):
    total_due = 0
    for item in cart_list:
        total_due +=menu_dict[item]
    return total_due


# Phase 3: The Main Interface (Control Flow)

while True:
    print("\n--- Welcome to our Coffee Shop ---\n")
    print("1. Show Menu | 2. Order Drink | 3. Checkout")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu(coffee_menu)
    elif choice == "2":
        customer_drink = input("What would you like to order? ").title()
        add_to_cart(customer_drink, coffee_menu, customer_cart)
    elif choice == "3":
        total = checkout(customer_cart, coffee_menu)

        print("--- Your Receipt ---\n")
        print(f"Items: {', '.join(customer_cart)}")
        print(f"Total Due: ${total:.2f}")
        break

    else:
        print("Invalid choice, please try again")




