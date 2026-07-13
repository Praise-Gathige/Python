# PHASE 1: THE BLUEPRINT
class BankAccount:

    def __init__(self, owner_name, starting_balance):
        self.owner = owner_name
        self.balance = starting_balance

    # PHASE 2: THE METHODS
    def deposit(self, amount):
        self.balance += amount
        print(f"Your new balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
        
        print(f"Here is your new balance {self.balance}")

# PHASE 3: THE EXECUTION
account_1 = BankAccount("Alice", 500)
account_2 = BankAccount("Bob", 1000)

account_1.deposit(200)
account_1.withdraw(1000)
account_2.withdraw(50)

print(f"{account_1.owner}'s balance is {account_1.balance}")
print(f"{account_2.owner}'s balance after withdrawal is {account_2.balance}")

