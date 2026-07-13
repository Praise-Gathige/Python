class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def processing_payment(self, amount):
        last_four_digits = str(self.card_number)[-4:]
        print(f"Processing ${amount} to card ending in {last_four_digits}")


class PayPal:
    def __init__(self, email_address):
        self.email_address = email_address

    def processing_payment(self, amount):
        print(f"Rounting ${amount} through PayPal account {self.email_address}")


class CryptoWallet:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def processing_payment(self, amount):
        print(f"Transferring ${amount} via blockchain to {self.wallet_address}")


def checkout(cart_total, payment_method):
    payment_method.processing_payment(cart_total)



card = CreditCard(3847590182)
points = PayPal("sample@gmail.com")
wallet = CryptoWallet("0x15EDS213")

checkout(250, card)
checkout(100, points)
checkout(480, wallet)