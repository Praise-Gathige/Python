# Task 1: The modulus checker
num = int(input("Enter a number: "))

if num%2 == 0:
    print("It's even!")
else:
    print("It's odd!")


# Task 2: The Bouncer (Logical & Comparison)
age = int(input("What is your age? "))
is_id_card = input("Do you have an ID card?(yes/no) ")
if is_id_card == "yes":
    is_id_card = True
else:
    is_id_card = False

if age >= 18 and is_id_card:
    print("Access Granted")
else:
    print("Access Denied")



# Mini-Challenge: The Tip Calculator
total_bill = float(input("What is the total bill amount? "))
tip_percentage = float(input("What percentage tip would you like to give? "))
bill_splitting = int(input("How many people are splitting the bill? "))

tip_amount = total_bill * (tip_percentage / 100)

total_bill += tip_amount

people_split_amount = total_bill / bill_splitting

print(f"The tip amount: ${tip_amount:.2f}")
print(f"The new total bill: ${total_bill:.2f}")
print(f"How much each person must pay: ${people_split_amount:.2f}")
