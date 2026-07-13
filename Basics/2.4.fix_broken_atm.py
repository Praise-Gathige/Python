global_balance = 500

def withdraw(amount):
    new_balance = global_balance - amount
    print(f"Dispensing ${amount}. Your new balance is ${new_balance}")
    return new_balance

global_balance = withdraw(100)
print(f"Database shows: ${global_balance}")