from abc import ABC, abstractmethod

# Logger Interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Text Logger Implementation
class TextLogger(Logger):
    def __init__(self, file_location):
        self.file_location = file_location
    
    def log(self, message):
        with open(self.file_location, 'a') as file:
            file.write(f"{message}\n")

# Abstract Payment Method
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount_to_pay):
        pass

# Credit Card Specific Interface (Segregated Interface)
class CreditCardSpecific(ABC):
    @abstractmethod
    def get_card_details(self):
        pass

# Credit Card Payment
class CreditCardPayment(PaymentMethod, CreditCardSpecific):
    def __init__(self, card_holder_name, cvv, bank, logger=None):
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.bank = bank
        self.logger = logger if logger else TextLogger("/log/file.txt")
    
    def validate_method(self):
        # Validation logic for Credit Card (e.g., Luhn's algorithm)
        pass
    
    def process_payment(self, amount_to_pay):
        self.logger.log(f"Processing credit card payment of ${amount_to_pay}")
        # Update DB or perform payment logic
        self.logger.log("Completed credit card payment")

    def get_card_details(self):
        # Specific function to get card details
        return f"Card Holder: {self.card_holder_name}, CVV: {self.cvv}, Bank: {self.bank}"

# PayPal Payment (No get_card_details here)
class PayPalPayment(PaymentMethod):
    def __init__(self, id, user_name, bank, logger=None):
        self.id = id
        self.user_name = user_name
        self.bank = bank
        self.logger = logger if logger else TextLogger("/log/file.txt")
    
    def validate_method(self):
        # Validation logic for PayPal (e.g., email validation, password check)
        pass
    
    def process_payment(self, amount_to_pay):
        self.logger.log(f"Processing PayPal payment of ${amount_to_pay}")
        # Update DB or perform payment logic
        self.logger.log("Completed PayPal payment")

# Crypto Payment (No get_card_details here)
class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_id, crypto_name, bank, logger=None):
        self.wallet_id = wallet_id
        self.crypto_name = crypto_name
        self.bank = bank
        self.logger = logger if logger else TextLogger("/log/file.txt")
    
    def validate_method(self):
        # Validation logic for crypto (e.g., wallet address format check)
        pass
    
    def process_payment(self, amount_to_pay):
        self.logger.log(f"Processing cryptocurrency payment of {amount_to_pay} BTC")
        # Update DB or perform payment logic
        self.logger.log("Completed cryptocurrency payment")

# Payment Factory
class PaymentFactory:
    @staticmethod
    def payment_method(payment_type, **kwargs):
        if payment_type == "card":
            return CreditCardPayment(kwargs["card_holder_name"], kwargs["cvv"], kwargs["bank"])
        elif payment_type == "paypal":
            return PayPalPayment(kwargs["id"], kwargs["user_name"], kwargs["bank"])
        elif payment_type == "crypto":
            return CryptoPayment(kwargs["crypto_wallet"], kwargs["crypto_name"], kwargs["bank"])
        else:
            raise ValueError("Invalid payment type")

# Example usage
card_payment = PaymentFactory.payment_method("card", card_holder_name="John", cvv="344", bank="JPMorgan")
card_payment.process_payment(100)

# Since it's a CreditCardPayment, we can now access the get_card_details function
if isinstance(card_payment, CreditCardSpecific):
    print(card_payment.get_card_details())

paypal_payment = PaymentFactory.payment_method("paypal", id="user123", user_name="JohnDoe", bank="PayPal Bank")
paypal_payment.process_payment(150)

crypto_payment = PaymentFactory.payment_method("crypto", crypto_wallet="1AB23CD", crypto_name="Bitcoin", bank="CryptoBank")
crypto_payment.process_payment(0.005)
