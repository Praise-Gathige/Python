# Task 1: The Multiplier Table
number = input("Enter a number: ")
num = int(number)

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")


# Task 2: The Annoying Parrot
while True:
    word = input("Enter any word: ")
    if word == "stop":
        break
    else:
        print(word)



# Boss Challenge: The Secure Bank Vault
correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter pin: ")
    if pin == correct_pin:
        print("Vault Unlocked!")
        break
    else: 
        attempts -= 1
        print(f"Incorrect. You have {attempts} tries left.")
if attempts == 0:
    print("ALARM TRIGGERED! Police are on the way.")
        