# Phase 1: The State (Dictionaries)

pet = {
    "name": "Byte",
    "hunger": 50,
    "happiness": 50,
    "energy": 50
}


# Phase 2: The Action Functions (Logic & Rules)

def cap_rule(pet):
    for stats in ['hunger', 'happiness', 'energy']:
        if pet[stats] > 100:
            pet[stats] = 100

        if pet[stats] < 0:
            pet[stats] = 0

def feed(pet):
    pet['hunger'] -= 20
    pet['energy'] += 5
    cap_rule(pet)


def play(pet):
    pet['happiness'] += 20
    pet['hunger'] -= 10
    pet['energy'] -= 15
    cap_rule(pet)


def sleep(pet):
    pet['energy'] += 40
    pet['hunger'] += 10
    cap_rule(pet)


# Boss Level Challenge: The "Time Tick" & Game Over

def time_tick(pet):
    pet['hunger'] += 5
    pet['energy'] -= 5
    cap_rule(pet)



# Phase 3: The Game Loop & Router

while True:

    if pet['hunger'] >= 100 or pet['energy'] <= 0:
        print(f"\nStats: {pet}")
        print("Your pet ran away! GAME OVER")
        break

# Print The Menu

    print(f"\n--- {pet['name']}'s Stats ---")
    print(f"Hunger: {pet['hunger']} | Happiness: {pet['happiness']} | Energy: {pet['energy']}")

    print("What would you like to do with your pet?")
    print(" 1.(Feed)\n 2.(Play)\n 3.(Sleep)\n 4.(Quit)")
    choice = input(" Enter your choice:")

    if choice == "1":
        feed(pet)
        time_tick(pet)
    elif choice == "2":
        play(pet)
        time_tick(pet)
    elif choice == "3":
        sleep(pet)
        time_tick(pet)
    elif choice == "4":
        break
    else:
        print("Invalid input. Please enter a choice present in the menu.")
    
