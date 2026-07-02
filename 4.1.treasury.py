# Phase 1 - The Utility Functions (Inputs & Returns)
def determine_class(gold_held):
    if gold_held < 100:
        return "Peasant"
    elif 100 <= gold_held <= 1000:
        return "Merchant"
    else:
        return "Noble"
    

def calculate_tax(gold_held, citizen_class):
    if citizen_class == "Peasant":
        tax = gold_held * 0.05
    elif citizen_class == "Merchant":
        tax = gold_held * 0.25
    else:
        tax = gold_held * 0.25
    return float(tax)


# Phase 2: The Batch Processor (Iteration & Lists)
def process_ledger(citizen_ledger):
    audited_records = []
    total_tax_collected = 0.0

    for name, gold in citizen_ledger:
        current_class = determine_class(gold)
        current_tax = calculate_tax(gold, current_class)

        total_tax_collected += current_tax
        audited_records.append((name, current_class, current_tax))
    
    return audited_records, total_tax_collected


# Phase 3: The Royal Scribe (Formatting)
def print_report(records, total_gold):
    print("\n--- DAILY TREASURE REPORT ---\n")

    for name, c_class, tax in records:
        print(f"{name} - Rank: {c_class} | Tax Levied: {tax} gold")
        
    print(f"\nTotal Gold Collected: {total_gold}")


# Grandmaster Challenge: Variable Arguments (*args) & Defaults
def apply_pardons(*args, default_discount=50):
    total_discounts = 0
    for pardon in args:
        total_discounts += pardon
    return total_discounts + default_discount


# Phase 4: The Master Terminal (While Loops)
def run_terminal():
    daily_ledger = []

    while True:
        
        name = input("Enter citizen's name (or type 'DONE' to exit): ").title()
        if name.upper() == "DONE":
            break
        try:
            gold = float(input(f"Enter gold amount for {name}: "))
        except ValueError:
            print("Invalid input. Enter a valid gold amount")

        daily_ledger.append((name, gold))
    
        
    final_records, final_tax = process_ledger(daily_ledger)

    # Grandmaster Challenge Execution 
    pardon_total = apply_pardons(15, 20, 100)
    final_tax -= float(pardon_total)

    print_report(final_records, final_tax)
    print(f"Total gold lost to Royal Pardons: {pardon_total}")


# Run Program
run_terminal()