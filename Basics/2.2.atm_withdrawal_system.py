name = input("Enter your name: ")

balance = float(input("Enter your account balance: "))

withdrawal_amount = float(input("How much do you want to withdraw? "))

if withdrawal_amount > balance:
    print("Insufficient funds.")

elif withdrawal_amount <= 0:
    print("Invalid withdrawal amount")
    
else:
    if withdrawal_amount > (0.70 * balance):
        print("Large withdrawal detected")

    balance -= withdrawal_amount
    print(f"Your balance is: {balance}")
    