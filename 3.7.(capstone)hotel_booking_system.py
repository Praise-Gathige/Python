# Phase 1: The Database
hotel_rooms = {101: "Available", 102: "Available", 103: "Available", 104: "Available", 105: "Available"}

# Phase 2: The Display & Save Functions
def show_status():
    print("\n--- Current Room Status ---")
    for room, guest in hotel_rooms.items():
        print(f"Room {room}: {guest}")

def save_registry():
    with open("registry.txt", "w") as file:
        for room, guest in hotel_rooms.items():
            file.write(f"Room {room}: {guest}\n")
    print("Registry saved to registry.txt.")

# Phase 3: The Check-In Function
def check_in(room_number, guest_name):
    if room_number not in hotel_rooms:
        print("Error: That room number does not exist.")
    elif hotel_rooms[room_number] == "Available":
        hotel_rooms[room_number] = guest_name
        print(f"Success! {guest_name} has been checked into Room {room_number}.")
    else:
        print("Sorry, that room is currently occupied.")

# Phase 4: The Check-Out Function
def check_out(room_number):
    if room_number not in hotel_rooms:
        print("Error: That room number does not exist.")
    elif hotel_rooms[room_number] != "Available":
        hotel_rooms[room_number] = "Available"
        print(f"Success! Room {room_number} is now vacant.")
    else:
        print("This room is already empty.")

# Phase 5: The Interactive Menu
while True:
    print("\n--- Hotel Reception Menu ---")
    print("1. View Rooms | 2. Check In | 3. Check Out | 4. Save & Exit")
    
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        show_status()
    
    elif choice == "2":
        room_input = input("Enter room number to check in: ")
        if room_input.isdigit():
            room_num = int(room_input)
            name = input("Enter guest name: ")
            check_in(room_num, name)
        else:
            print("Invalid input. Please enter a numeric room number.")

    elif choice == "3":
        room_input = input("Enter room number to check out: ")
        if room_input.isdigit():
            room_num = int(room_input)
            check_out(room_num)
        else:
            print("Invalid input. Please enter a numeric room number.")

    elif choice == "4":
        save_registry()
        print("Exiting system. Goodbye!")
        break
    
    else:
        print("Invalid selection. Please choose 1, 2, 3, or 4.")
