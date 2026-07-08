# Phase 2: The ETL Pipeline (Extract, Transform, Load)

def ingest_ledger(filepath):
    clean_transactions = []

    with open(filepath, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(',')

                transaction_id = parts[0].strip()
                account_id = parts[1].strip()
                amount = float(parts[2].strip())
                region_code = parts[3].strip()

                clean_transactions.append((transaction_id, account_id, amount, region_code))

            except (IndexError, ValueError):
                continue
            
        return clean_transactions
    


# Phase 3: The Business Logic (Rules Engine)
def flag_suspicious_activity(transactions_list):
    flagged_txns = []

    for t_id, a_id, amount, region in transactions_list:
        if amount > 10000.00 or region == "XX":
            flagged_txns.append((t_id, a_id,amount,region))
    
    return flagged_txns



# Phase 4: Risk Aggregation (Dictionaries)

def aggregate_risk(flagged_list):
    account_risk_profile = {}

    for _, account_id, _, _ in flagged_list:
        if account_id in account_risk_profile:
            account_risk_profile[account_id] += 1
        else: 
            account_risk_profile[account_id] = 1
    return account_risk_profile




# Grandmaster Challenge: The Master Terminal & Audit Export
def run_daily_audit():
    data = ingest_ledger('daily_ledger.csv')
    suspicious = flag_suspicious_activity(data)
    risk_report = aggregate_risk(suspicious)

    with open("quarantine_report.txt", "w") as file:
        file.write("--- AEGIS FINANCIAL: DAILY RISK REPORT ---\n")
        for account_id, count in risk_report.items():
            file.write(f"Account {account_id} has {count} flagged transactions. \n")
    
    print("Audit complete. Quarantine report generated.")



# Running the program

run_daily_audit()
# if __name__ == "__main__":
#     data = ingest_ledger('daily_ledger.csv')
#     suspicious = flag_suspicious_activity(data)
#     risk_report = aggregate_risk(suspicious)

#     print("Risk Profile: ", risk_report)
        