# =====================================================
# Phase 1: The Vault (Encapsulation)
# =====================================================
class BankAccount:
    def __init__(self, account_number, initial_deposit):
        self.account_number = account_number
        # Encapsulation for private attribute
        self.__balance = initial_deposit


    # Methods to interact with the private balance
    def check_balance(self):
        print(f"Current bank balance: ${self.__balance}")
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount}. Current balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return amount
        else:
            print("Transaction Declined: Insufficient Funds.")
            return 0
        

# =====================================================
# Phase 2: The Citizen (Object Composition)
# =====================================================
class Human:
    def __init__(self, name, personal_bank_amount):
        self.name = name
        self.energy = 100
        self.cash_in_pocket = 0
        self.bank_account = personal_bank_amount

    # =====================================================
    # Phase 3: The Daily Grind (Methods & State Changes)
    # =====================================================
    def sleep(self):
        self.energy = 100
        print(f"{self.name} slept well. Energy fully restored!")

    def work(self):
        if self.energy >= 30:
            self.energy -= 30
            self.cash_in_pocket += 150
            print(f"{self.name} worked hard and earned $150. Current energy: {self.energy}")
        else:
            print(f"{self.name} is too exhausted to work. They need to sleep!")

    def visit_bank(self):
        if self.cash_in_pocket > 0:
            self.bank_account.deposit(self.cash_in_pocket)
            self.cash_in_pocket = 0
            print("Bank visit successful. All pocket cash deposited.")
        else:
            print(f"{self.name} has no cash in pocket to deposit.")

    # =====================================================
    # Boss Level Challenge: The Coffee Shop
    # =====================================================
    def buy_coffee(self):
        if self.cash_in_pocket >= 5:
            self.cash_in_pocket -= 5
            self.energy = min(self.energy + 15, 100)
            print(f"{self.name} paid $5 for coffee! Energy restored by 15. (Energy: {self.energy})")

        else:
            print(f"No cash in pocket! Attempting to use debit card...")
            withdrawn_amount = self.bank_account.withdraw(5)
            if withdrawn_amount ==5:
                self.energy = min(self.energy + 15, 100)
                print(f"Debit payment of $5 successfull. Energy restored by 15. (Energy: {self.energy})")   
            else:
                print("Couldn't purchase coffee.")


# =====================================================
# Phase 4: The Simulation Loop (Instantiating the World)
# =====================================================
my_chase_account = BankAccount("CHK-1234", 50)
player = Human("Alex", my_chase_account)

print("=" * 50)
print("--- Welcome to the Life $ Finance Simulator ---")
print("=" * 50)

while True:
    print(f"\n--- Status: {player.name} | Energy: {player.energy} | Pocket Cash: ${player.cash_in_pocket} ---")
    print("[1] Go to Work\n[2] Sleep\n[3] Deposit Cash at Bank\n[4] Check Bank Balance\n[5] Exit Life\n[6] Buy Coffee")
    choice = input("What would you like to do? ").strip()

    if choice == "1":
        player.work()
    elif choice == "2":
        player.sleep()
    elif choice == "3":
        player.visit_bank()
    elif choice == "4":
        player.bank_account.check_balance()
    elif choice == "5":
        print("Exiting life simulator. Goodbye!")
        break
    elif choice == "6":
        player.buy_coffee()
    else:
        print("Invalid choice! Please choose an option from 1-6.")