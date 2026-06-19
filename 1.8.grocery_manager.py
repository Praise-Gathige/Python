# Assignment: The Grocery Saver

groceries = ["Apples", "Milk", "Bread", "Eggs", "Coffee"]

with open("grocery.txt", "w") as file:
    for item in groceries:
        file.write(item + "\n")

with open("grocery.txt", "r") as file:
    for line in file:
        print(f"- {line.strip()}")


# Weekly Challenge: Saving a Dictionary

grades = {
    "John": 85,
    "Mary": 92,
    "Kevin": 78
}

with open("gradebook.txt", "w") as file:
    for student, score in grades.items():
        file.write(f"{student}: {score}\n")
    
with open("gradebook.txt", "a") as file:
    file.write(f"Sarah: 95\n")
