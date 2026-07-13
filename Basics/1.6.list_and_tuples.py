# Task 1: The Armor Inventory

inventory = ["Sword", "Shield", "Boots"]
print(inventory[2])
inventory[2] = "Iron Boots"
print(inventory[2])
inventory.append("Helmet")
print(inventory)

for items in inventory:
    print(items)


# The RGB Color Code(Tuple)

pure_red = (255, 0, 0)
r, g, b = pure_red
print(f"Red: {r}, Green: {g}, Blue: {b}")


# Boss Challenge: The High Score Roster

leaderboard = [("Alice", 9500), ("Bob", 8200), ("Charlie", 7400)]
for name, score in leaderboard:
    print(f"Player: {name} | Score: {score}")