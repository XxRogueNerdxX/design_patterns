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

# Payment Method Abstract Class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount_to_pay):
        pass

# Credit Card Payment Class
class CreditCardPayment(PaymentMethod):
    def __init__(self, card_holder_name, cvv, bank, logger=None):
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.bank = bank
        self.logger = logger if logger else TextLogger("/log/credit_card_log.txt")
    
    def process_payment(self, amount_to_pay):
        self.logger.log(f"Processing credit card payment of ${amount_to_pay}")
        self.logger.log("Completed credit card payment")

# PayPal Payment Class
class PayPalPayment(PaymentMethod):
    def __init__(self, id, user_name, bank, logger=None):
        self.id = id
        self.user_name = user_name
        self.bank = bank
        self.logger = logger if logger else TextLogger("/log/paypal_log.txt")
    
    def process_payment(self, amount_to_pay):
        self.logger.log(f"Processing PayPal payment of ${amount_to_pay}")
        self.logger.log("Completed PayPal payment")

# Crypto Payment Class
class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_id, crypto_name, bank, logger=None):
        self.wallet_id = wallet_id
        self.crypto_name = crypto_name
        self.bank = bank
        self.logger = logger if logger else TextLogger("/log/crypto_log.txt")
    
    def process_payment(self, amount_to_pay):
        self.logger.log(f"Processing cryptocurrency payment of {amount_to_pay} BTC")
        self.logger.log("Completed cryptocurrency payment")

# Payment Details (Builder pattern is used to create this)
class PaymentDetails:
    def __init__(self, payment_type, amount, billing_address, user_info):
        self.payment_type = payment_type
        self.amount = amount
        self.billing_address = billing_address
        self.user_info = user_info

# PaymentDetailsBuilder (Builder pattern)
class PaymentDetailsBuilder:
    def __init__(self):
        self.payment_type = None
        self.amount = None
        self.billing_address = None
        self.user_info = None
    
    def set_payment_type(self, payment_type):
        self.payment_type = payment_type
        return self
    
    def set_amount(self, amount):
        self.amount = amount
        return self
    
    def set_billing_address(self, billing_address):
        self.billing_address = billing_address
        return self
    
    def set_user_info(self, user_info):
        self.user_info = user_info
        return self
    
    def build(self):
        if not (self.payment_type and self.amount and self.billing_address and self.user_info):
            raise ValueError("Missing payment details")
        return PaymentDetails(self.payment_type, self.amount, self.billing_address, self.user_info)

# Individual Factory Classes
class CreditCardFactory:
    @staticmethod
    def create(**kwargs):
        return CreditCardPayment(kwargs["card_holder_name"], kwargs["cvv"], kwargs["bank"])

class PayPalFactory:
    @staticmethod
    def create(**kwargs):
        return PayPalPayment(kwargs["id"], kwargs["user_name"], kwargs["bank"])

class CryptoFactory:
    @staticmethod
    def create(**kwargs):
        return CryptoPayment(kwargs["crypto_wallet"], kwargs["crypto_name"], kwargs["bank"])

# Factory Map Dictionary
payment_factories = {
    "credit_card": CreditCardFactory,
    "paypal": PayPalFactory,
    "crypto": CryptoFactory
}

# Process Payment function using both Builder and Factory
def process_payment(payment_info):
    payment_details_builder = PaymentDetailsBuilder()\
        .set_payment_type(payment_info["payment_method"])\
        .set_amount(payment_info["amount"])\
        .set_billing_address(payment_info["billing_address"])\
        .set_user_info(payment_info["user_info"])

    payment_details = payment_details_builder.build()  # Build the complex payment details object

    factory_class = payment_factories[payment_details.payment_type]  # Get the corresponding factory
    payment_instance = factory_class.create(**payment_info)  # Create the payment method object
    payment_instance.process_payment(payment_details.amount)  # Process payment

# Example data
payment_data_card = {
    "payment_method": "credit_card",
    "card_holder_name": "John Doe",
    "cvv": "123",
    "bank": "Bank of America",
    "amount": 100,
    "billing_address": "123 Elm St",
    "user_info": {"email": "john@example.com", "phone": "555-5555"}
}

payment_data_paypal = {
    "payment_method": "paypal",
    "id": "user123",
    "user_name": "johndoe",
    "bank": "PayPal Bank",
    "amount": 150,
    "billing_address": "456 Oak St",
    "user_info": {"email": "john@example.com", "phone": "555-5555"}
}

payment_data_crypto = {
    "payment_method": "crypto",
    "crypto_wallet": "1AB23CD",
    "crypto_name": "Bitcoin",
    "bank": "CryptoBank",
    "amount": 0.005,
    "billing_address": "789 Pine St",
    "user_info": {"email": "john@example.com", "phone": "555-5555"}
}

# Processing payments using the factories and builder
process_payment(payment_data_card)    # For credit card
process_payment(payment_data_paypal)  # For PayPal
process_payment(payment_data_crypto)  # For cryptocurrency
