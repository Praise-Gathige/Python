# Phase 1 - The Global State (Variables & Lists)

player_name = ("Hero")
player_gold = 50
player_health = 100.0
backpack = ["Health Potion", "Wooden Shield"]


# Phase 2 - The Action Functions (Logic & Parameters)

def show_stats():
    print(f"Name: {player_name}") 
    print(f"Gold: {player_gold}") 
    print(f"Health: {player_health}")
    print(f"Backpack: {', '.join(backpack)}")

def buy_item(item_name, cost):
    global player_gold

    if player_gold >= cost:
        player_gold -= cost
        backpack.append(item_name)
        print(f"You bought a {item_name}")
    else:
        print("Not enough gold!")

def use_potion():
    global player_health

    if "Health Potion" in backpack:
        backpack.remove("Health Potion")
        player_health += 25.0

        if player_health > 100.0:
            player_health = 100.0

            print(f"You used a potion. Your health is now {player_health}")
    else:
        print("You don't have any potions!")

# Phase 3 - The Game Loop (Control Flow)

while True:
    print("1. View Stats | 2. Buy Iron Sword (30g) | Use Potion | 4. Quit")

    user_input = int(input("Enter your choice: "))
    
    if user_input == 1:
        show_stats()
    elif user_input == 2:
        buy_item("Iron Sword", 30)
    elif user_input == 3:
        use_potion()
    elif user_input == 4:
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Try again")

    
