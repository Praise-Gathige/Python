def exchange_currency(usd_amount, exchange_rate):
    converted_cash = usd_amount * exchange_rate
    fee = converted_cash * 0.05
    final_payout = converted_cash - fee
    return final_payout

my_wallet = exchange_currency(200, 1.10)

print(f"After fees, your wallet contains: €{my_wallet}")